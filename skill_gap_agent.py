import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def skill_gap_analysis(resume_text, target_role):

    prompt = f"""
    You are an expert career advisor.

    Target Role:
    {target_role}

    Resume:
    {resume_text}

    Analyze the resume and provide:

    1. Current Skills
    2. Missing Skills
    3. Important Tools and Technologies to Learn
    4. Learning Priority (High, Medium, Low)
    5. Career Advice

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text