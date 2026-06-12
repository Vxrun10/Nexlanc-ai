# 🤖 Nexlanc AI — Smart Resume Analyzer

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-brightgreen?style=for-the-badge)](https://nexlanc-ai.onrender.com/login)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLM%20API-orange?style=for-the-badge)](https://groq.com)

> **Upload your resume → Get AI-powered analysis → Know exactly what skills are missing → Get instant interview questions tailored to your profile.**

🔗 **[Try it Live](https://nexlanc-ai.onrender.com/login)**

---

## 🚀 What It Does

Nexlanc AI is a full-stack AI-powered web application that helps job seekers improve their resumes and prepare for interviews.

- 📄 **Resume Parsing** — Upload your resume (PDF/DOCX) and extract structured candidate information automatically
- 🧠 **AI Skill Gap Analysis** — Identifies missing skills based on your target role using Groq LLM
- ❓ **Auto Interview Question Generator** — Generates personalized interview questions based on your resume content
- 💾 **Database Storage** — Stores candidate data using TiDB Cloud (MySQL-compatible distributed database)
- 🔐 **User Authentication** — Secure login/signup with environment-based credential management
- 🌐 **Deployed on Render** — Live and accessible, not just a local project

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **AI / LLM** | Groq API (LLaMA 3) |
| **Database** | TiDB Cloud (MySQL-compatible) |
| **Frontend** | HTML, CSS, Jinja2 Templates |
| **Deployment** | Render |
| **Libraries** | SQLAlchemy, PyPDF2, python-docx |

---

## ✨ Key Features

- ✅ Upload resume in PDF or DOCX format
- ✅ AI extracts name, skills, experience, and education automatically
- ✅ Groq LLM analyzes skill gaps for target job roles
- ✅ Generates 5–10 tailored interview questions instantly
- ✅ User authentication with secure session management
- ✅ Data persisted in scalable distributed database (TiDB Cloud)
- ✅ Fully deployed and production-ready on Render

---

## 📁 Project Structure

```
Nexlanc-ai/
│
├── app.py              # Main Flask application & routes
├── ai.py               # Groq API integration & LLM logic
├── db.py               # TiDB Cloud database connection
├── models.py           # SQLAlchemy database models
├── requirements.txt    # Python dependencies
├── procfile            # Render deployment config
│
├── templates/          # Jinja2 HTML templates
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── result.html
│
└── static/             # CSS, JS, assets
    ├── style.css
    └── script.js
```

---

## ⚙️ Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Vxrun10/Nexlanc-ai.git
cd Nexlanc-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
DB_URL=your_tidb_connection_string_here
SECRET_KEY=your_flask_secret_key
```

### 4. Run the App
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## 🌐 Live Demo

The app is deployed and live on Render:

👉 **[https://nexlanc-ai.onrender.com/login](https://nexlanc-ai.onrender.com/login)**

> Note: Free tier on Render may take 30–60 seconds to wake up on first visit.

---

## 🔮 Future Improvements

- [ ] Add RAG (Retrieval Augmented Generation) for more accurate skill gap analysis
- [ ] Support for LinkedIn profile URL parsing
- [ ] Job description matching score (0–100%)
- [ ] Export analysis report as PDF
- [ ] Multi-language resume support

---

## 👨‍💻 Author

**Varun Panchal**
- 📧 varunpanchal1008@gmail.com
- 🔗 [GitHub](https://github.com/Vxrun10)
- 💼 [LinkedIn](https://linkedin.com/in/your-linkedin)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project useful, please give it a star!**
