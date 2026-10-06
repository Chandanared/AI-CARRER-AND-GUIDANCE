
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Career Guidance",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Career Guidance System")
st.write(
    "Discover suitable career paths and the skills you need to learn."
)

st.header("Student Profile")

name = st.text_input("Enter your name")

education = st.selectbox(
    "Select your education level",
    ["B.Tech CSE", "Intermediate", "Diploma", "Other"]
)

interests = st.multiselect(
    "Choose your interests",
    [
        "Artificial Intelligence",
        "Web Development",
        "Data Science",
        "Cybersecurity",
        "App Development"
    ]
)

level = st.selectbox(
    "Select your current programming level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Recommend My Career"):
    if not name or not interests:
        st.warning("Please enter your name and select your interests.")
    else:
        st.subheader(f"Career Guidance for {name}")

        career_data = {
            "Artificial Intelligence": (
                "AI Engineer",
                ["Python", "Machine Learning", "Mathematics"]
            ),
            "Web Development": (
                "Web Developer",
                ["HTML", "CSS", "JavaScript"]
            ),
            "Data Science": (
                "Data Analyst",
                ["Python", "SQL", "Data Visualization"]
            ),
            "Cybersecurity": (
                "Cybersecurity Analyst",
                ["Networking", "Linux", "Security Fundamentals"]
            ),
            "App Development": (
                "App Developer",
                ["Python or Java", "Mobile Development", "Databases"]
            )
        }

        for interest in interests:
            career, skills = career_data[interest]

            st.markdown(f"### 💼 {career}")
            st.write("**Recommended skills to learn:**")
            st.write(", ".join(skills))

        st.info(
            f"Your current programming level is {level}. "
            "Start with the fundamentals and practise with small projects."
        )

        st.caption(
            "These are preliminary rule-based suggestions, "
            "not predictions from a trained AI model."
        )