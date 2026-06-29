import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print("API Key:", os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_roadmap(skill_gap_report):

    prompt = f"""
    You are an expert career mentor.

    Based on the following skill gap report,
    create a practical 30-day learning roadmap.

    Organize the roadmap as follows:

    Week 1:
    - Skills to learn
    - Resources to explore

    Week 2:
    - Intermediate topics
    - Hands-on practice

    Week 3:
    - Mini project ideas
    - Technologies to use

    Week 4:
    - Portfolio improvements
    - Resume enhancements
    - Interview preparation
    - Job application tips

    Skill Gap Report:
    {skill_gap_report}
    """

    response = model.generate_content(prompt)

    return response.text