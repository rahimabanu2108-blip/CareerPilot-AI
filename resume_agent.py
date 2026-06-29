import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_resume(text):
    prompt = f"""
    You are an expert resume analyzer and career advisor.

    Analyze the following resume and provide:

    1. Skills
    2. Education
    3. Projects
    4. Strengths
    5. Areas for Improvement

    Resume:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text