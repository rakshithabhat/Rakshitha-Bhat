import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

st.set_page_config(page_title="TrigLearn", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1, h2, h3 {
    color: #1f4e79;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>📐 TrigLearn</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Master Trigonometry with Interactive Learning</p>", unsafe_allow_html=True)

FILE = "scores.csv"

if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["name", "score"])

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""
if "role" not in st.session_state:
    st.session_state.role = ""

if not st.session_state.logged_in:

    st.markdown("### 🔐 Login to Continue")

    role = st.selectbox("Select Role", ["Student", "Teacher"])
    name = st.text_input("Enter Name")

    if st.button("Login"):
        if name.strip():
            st.session_state.logged_in = True
            st.session_state.user = name
            st.session_state.role = role
            st.rerun()
        else:
            st.warning("Please enter your name")

else:

    st.sidebar.success(f"{st.session_state.role}: {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.role = ""
        st.rerun()

    if st.session_state.role == "Student":

        page = st.sidebar.radio("Navigation", ["Dashboard", "Learn", "Quiz", "Applications"])

        if page == "Dashboard":
            st.subheader("📊 Your Dashboard")

            user_data = df[df["name"] == st.session_state.user]

            if len(user_data) > 0:
                col1, col2 = st.columns(2)
                col1.metric("Attempts", len(user_data))
                col2.metric("Average Score", f"{user_data['score'].mean():.2f}")

                fig, ax = plt.subplots()
                ax.plot(user_data["score"], marker='o')
                ax.set_title("Progress Over Time")
                st.pyplot(fig)
            else:
                st.info("Start a quiz to see your progress")

        elif page == "Learn":
            st.subheader("📘 Learn Trigonometry")
            st.markdown("### Key Concepts")
            st.write("""
            - sinθ = Opp/Hyp  
            - cosθ = Adj/Hyp  
            - tanθ = Opp/Adj  
            """)
            st.markdown("### 🎥 Video Lesson")
            st.video("https://www.youtube.com/watch?v=PUB0TaZ7bhA")

        elif page == "Quiz":
            st.subheader("🧠 Practice Quiz")

            score = 0

            q1 = st.radio("sin(90°)?", ["0", "1", "-1"])
            q2 = st.radio("cos(0°)?", ["0", "1", "-1"])
            q3 = st.radio("tan(45°)?", ["0", "1", "2"])
            q4 = st.radio("sin(0°)?", ["0", "1", "-1"])
            q5 = st.radio("cos(90°)?", ["0", "1", "-1"])

            if st.button("Submit Quiz"):
                if q1 == "1": score += 1
                if q2 == "1": score += 1
                if q3 == "1": score += 1
                if q4 == "0": score += 1
                if q5 == "0": score += 1

                st.success(f"Your Score: {score}/5")

                new_row = pd.DataFrame({
                    "name": [st.session_state.user],
                    "score": [score]
                })

                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(FILE, index=False)

        elif page == "Applications":
            st.subheader("🏗 Real-World Application")

            d = st.number_input("Distance (m)", min_value=0.0)
            angle = st.slider("Angle (°)", 1, 90)

            if st.button("Calculate"):
                h = d * np.tan(np.radians(angle))
                st.success(f"Height ≈ {h:.2f} m")

    elif st.session_state.role == "Teacher":

        st.subheader("👩‍🏫 Teacher Dashboard")

        if len(df) > 0:

            st.markdown("### 📋 Student Records")
            st.dataframe(df)

            col1, col2 = st.columns(2)
            col1.metric("Total Attempts", len(df))
            col2.metric("Average Score", f"{df['score'].mean():.2f}")

            st.markdown("### 📊 Performance by Student")

            grouped = df.groupby("name")["score"].mean().reset_index()

            fig, ax = plt.subplots()
            ax.bar(grouped["name"], grouped["score"])
            st.pyplot(fig)

        else:
            st.info("No data available")
