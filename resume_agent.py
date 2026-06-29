import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6I_ZVDbfsZEsA9lXbhqwSbab-Gu1HojjrCdCqDIgY0X2Q")

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_resume(text):

    prompt = f"""
    Analyze this resume and provide:

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