from flask import Flask, render_template,request,redirect,session
from db import engine, Base,SessionLocal
import models
import PyPDF2
import docx
import json
from ai import analyze_resume
import os

app = Flask(__name__)
app.secret_key="Deal2026"


@app.route("/")
def home():
    if "user" in session:
      return redirect("/dashboard")
    return redirect("/login")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    db=SessionLocal()
    
    if request.method =="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        
        exsisting_user = db.query(models.User).filter_by(email=email).first()
        if exsisting_user:
            return"User Already Exsist"
        
        user = models.User(email= email, password=password)
        db.add(user)
        db.commit()
        
        return redirect("login")
    return render_template("signup.html")

#LogIn

@app.route("/login",methods=["GET","POST"])
def login():
    db=SessionLocal()
    if request.method =="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        
        user = db.query(models.User).filter_by(email=email, password=password).first()
        
        
        if user:
            session["user"] = user.email
            return redirect("/dashboard")
        else:
            return "Invalid Credentials"
    return render_template("login.html")

#Dashboard

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")
    
    result = None
    resume_text = ""
    
    if request.method == "POST":
        
        user_goal = request.form.get("role")
        user_text = request.form.get("resume")
        file = request.files.get("file")
        
        # File Handling
        if file and file.filename != "":   
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = {"error": f"PDF Error: {str(e)}"}
                    
            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"Docx error: {str(e)}"}
        
        if resume_text and user_goal:
            try:
                result = analyze_resume(resume_text, user_goal)
                
                db = SessionLocal()
                user = db.query(models.User).filter_by(email=session["user"]).first()
                
                report = models.Reports(
                    user_id=user.id,
                    resume_text=resume_text,
                    result=json.dumps(result)
                )
                
                db.add(report)
                db.commit()
                
            except Exception as e:
                result = {"error": f"AI ERROR: {str(e)}"}

    #  THIS handles GET requests (and fallback)
    return render_template(
        "Dashboard.html",
        user=session["user"],
        result=result
    )

#history
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")
    
    db = SessionLocal()
    user = db.query(models.User).filter_by(email=session["user"]).first()
    
    reports = db.query(models.Reports).filter_by(user_id=user.id).all()
    
    parsed_reports = []

    for r in reports:
        try:
            parsed_result = json.loads(r.result)
        except:
            parsed_result = {}

        parsed_reports.append({
            "resume": r.resume_text,
            "result": parsed_result
        })

    return render_template("history.html", reports=parsed_reports)
    
#logout route
@app.route("/logout") 
def logout():
    session.pop("user",None)  
    return redirect("/login")
    
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)   
    app.run()