# 🚀 CareerPilot AI: Skill Gap Analyzer & Career Roadmap Generator

## 📌 Overview

CareerPilot AI is an AI-powered career guidance application built as part of the **Kaggle 5-Day AI Agents Intensive Course with Google**.

The application helps users understand their current skill set, identify missing skills for a desired career role, and receive a personalized 30-day learning roadmap.

It uses Google's Gemini AI to analyze resumes and generate intelligent career recommendations through multiple AI agents.

---

## ✨ Features

* 📄 Resume Analysis
* 🎯 Skill Gap Detection
* 🛣️ Personalized 30-Day Learning Roadmap
* 🤖 AI-powered recommendations using Gemini
* 💻 Simple and interactive Streamlit interface

---

## 🏗️ Project Architecture

```
User Uploads Resume
        │
        ▼
 Resume Analysis Agent
        │
        ▼
 Skill Gap Analysis Agent
        │
        ▼
 Learning Roadmap Agent
        │
        ▼
     Streamlit UI
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini AI
* python-dotenv
* PyPDF

---

## 📂 Project Structure

```
CareerPilot-AI/
│
├── app.py
├── resume_agent.py
├── skill_gap_agent.py
├── roadmap_agent.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CareerPilot-AI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 🎯 How It Works

1. Upload your resume (PDF).
2. Enter your target job role.
3. The Resume Analysis Agent extracts key information.
4. The Skill Gap Agent compares your profile with the desired role.
5. The Roadmap Agent generates a personalized 30-day learning plan.

---

## 🚀 Future Improvements

* Resume scoring
* Job recommendation system
* LinkedIn profile analysis
* Course recommendations
* Interview preparation assistant

---

## 👩‍💻 Author

Developed by **Rahima Banu N**

Capstone Project for the **Kaggle 5-Day AI Agents Intensive Course with Google**.
