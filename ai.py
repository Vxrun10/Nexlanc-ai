from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, user_goal):
    prompt = f"""
You are a senior software engineer and hiring manager.

Evaluate the resume based on the user's goal.

User goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- Remove irrelevant tools (e.g., Excel for backend roles)
- Identify real skill gaps
- Generate roadmap only for missing skills
- Make output different based on goal

Return ONLY valid JSON in this format:

{{
  "skills": [],
  "missing_skills": [],
  "roadmap": [],
  "interview_questions": []
}}

Resume:
{resume_text[:3000]}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON. No explanation."},
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content.strip()

        # ✅ Safe JSON extraction
        start = content.find("{")
        end = content.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError("No JSON found in response")

        parsed = json.loads(content[start:end])

        # ✅ Ensure all keys exist
        return {
            "skills": parsed.get("skills", []),
            "missing_skills": parsed.get("missing_skills", []),
            "roadmap": parsed.get("roadmap", []),
            "interview_questions": parsed.get("interview_questions", [])
        }

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e),
            "raw_output": content if 'content' in locals() else ""
        }
