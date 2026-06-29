import streamlit as st

from utils import extract_text
from resume_agent import analyze_resume
from skill_gap_agent import skill_gap_analysis
from roadmap_agent import generate_roadmap

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.write(
    "Analyze your resume, identify skill gaps, and generate a personalized learning roadmap."
)

pdf = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

role = st.text_input(
    "Target Career Role",
    placeholder="AI Engineer, Data Analyst, Web Developer..."
)

if pdf and role:

    resume_text = extract_text(pdf)

    with st.spinner("Analyzing Resume..."):
        analysis = analyze_resume(resume_text)

    with st.spinner("Finding Skill Gaps..."):
        skill_gap = skill_gap_analysis(
            resume_text,
            role
        )

    with st.spinner("Generating Roadmap..."):
        roadmap = generate_roadmap(skill_gap)

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Resume Analysis",
            "🎯 Skill Gap Analysis",
            "🗺️ Learning Roadmap"
        ]
    )

    with tab1:
        st.write(analysis)

    with tab2:
        st.write(skill_gap)

    with tab3:
        st.write(roadmap)

    st.success("✅ Career analysis completed successfully!")

elif pdf and not role:
    st.info("Please enter a target career role.")