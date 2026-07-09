from openai import OpenAI
import json
import os

try:
    import importlib
    _dotenv = importlib.import_module("dotenv")
    load_dotenv = _dotenv.load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False

# Load environment variables
load_dotenv()


def resume_analyzer(resume_text, user_goal):
    # .env ko har haal mein force load karein taake key miss na ho
    load_dotenv()
    
    # 🌟 Sabse aasan shortcut: Agar .env dhoondne mein masla ho, toh or ke aage direct apni openrouter key paste kar sakte ho
    api_key_val = os.getenv("OPENROUTER_API_KEY") or "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"
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key_val
    )

    # Check karein ke request chat ki hai ya resume analyzer ki
    is_chat_request = "Skills and Field Mentorship" in user_goal or "General" in user_goal or user_goal.strip() == ""

    if is_chat_request:
        system_prompt = "You are an expert AI Career Mentor and Technical Recruiter. Answer the user's professional question directly, accurately, and concisely in English."
        prompt = resume_text  
    else:
        system_prompt = "You are a strict technical hiring manager. You must evaluate the resume text based strictly on the user's career goal and return the response ONLY as a clean, valid JSON object."
        
        prompt = f"""
        Target Career Goal: "{user_goal}"
        
        Strict Rules:
        1. Keep the evaluation highly professional, sharp, and corporate standard.
        2. Do not assume or hallucinate facts that are not present in the resume.
        3. Output MUST be format strictly as a JSON object with the exact keys specified below.

        JSON Output Schema Format:
        {{
            "skills": ["Python", "Flask"],
            "missing_skills": ["SQLAlchemy", "Docker"],
            "roadmap": {{
                "phase 1 steps": ["Learn basic syntax", "Build a small app"],
                "phase 2 steps": ["Deploy to cloud", "Learn databases"]
            }},
            "interview_questions": ["Question 1?", "Question 2?"]
        }}

        Candidate Resume Data:
        "{resume_text}"
        """

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        
        content = response.choices[0].message.content.strip()

        # Agar simple chat hai, toh direct text return karo
        if is_chat_request:
            return content

        # Agar resume analysis hai, toh JSON string nikaalo
        start = content.find("{")
        end = content.rfind("}") + 1
        
        if start != -1 and end != -1:
            json_string = content[start:end]
            return json.loads(json_string)
        else:
            raise ValueError("AI did not return valid JSON tags.")

    except Exception as e:
        # 🌟 Agar chat fail ho, toh user ko batayein ke error kya hai taake system block na ho
        if is_chat_request:
            return f"System error occur. Connection issue or invalid API key. Detail: {str(e)}"
        else:
            return {
                "skills": [],
                "missing_skills": [],
                "roadmap": {},
                "interview_questions": [],
                "error": str(e)
            }