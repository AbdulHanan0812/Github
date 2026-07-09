from openai import OpenAI
import json

def resume_analyzer(resume_text, user_goal):
    
    from openai import OpenAI

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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" 
)

    is_chat_request = "Skills and Field Mentorship" in user_goal or "General" in user_goal

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
            "skills": ["list", "detected", "skills"],
            "missing_skills": ["list", "required", "gaps"],
            "roadmap": ["phase 1 steps", "phase 2 steps"],
            "interview_questions": ["q1", "q2", "q3", "q4", "q5"]
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

       
        if is_chat_request:
            return content

        
        start = content.find("{")
        end = content.rfind("}") + 1
        
        if start != -1 and end != -1:
            json_string = content[start:end]
            return json.loads(json_string)
        else:
            raise ValueError("AI did not return valid JSON tags.")

    except Exception as e:
        
        if is_chat_request:
            return f"Sorry, I am facing an issue connecting to the engine right now. Error: {str(e)}"
        else:
            return {
                "skills": [],
                "missing_skills": [],
                "roadmap": [],
                "interview_questions": [],
                "error": str(e)
            }