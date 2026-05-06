import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

st.set_page_config(page_title="TrigLearn", layout="wide")

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
    st.title("🔐 Login - TrigLearn")

    role = st.selectbox("Login as", ["Student", "Teacher"])
    name = st.text_input("Enter your name")

    if st.button("Login"):
        if name.strip() != "":
            st.session_state.logged_in = True
            st.session_state.user = name
            st.session_state.role = role
            st.rerun()
        else:
            st.warning("Enter valid name")

else:
    st.title("📐 TrigLearn")

    st.sidebar.success(f"{st.session_state.role}: {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.role = ""
        st.rerun()

    if st.session_state.role == "Student":

        page = st.sidebar.radio("Navigate", ["Learn", "Quiz", "Applications", "My Analytics"])

        if page == "Learn":
            st.header("📘 Trigonometric Ratios")
            st.write("sinθ = Opp/Hyp\ncosθ = Adj/Hyp\ntanθ = Opp/Adj")
            st.video("https://www.youtube.com/watch?v=PUB0TaZ7bhA")

        elif page == "Quiz":
            st.header("🧠 Quiz")

            score = 0

            q1 = st.radio("1. sin(90°)?", ["0", "1", "-1"])
            q2 = st.radio("2. cos(0°)?", ["0", "1", "-1"])
            q3 = st.radio("3. tan(45°)?", ["0", "1", "2"])
            q4 = st.radio("4. sin(0°)?", ["0", "1", "-1"])
            q5 = st.radio("5. cos(90°)?", ["0", "1", "-1"])

            if st.button("Submit Quiz"):
                if q1 == "1": score += 1
                if q2 == "1": score += 1
                if q3 == "1": score += 1
                if q4 == "0": score += 1
                if q5 == "0": score += 1

                st.success(f"Score: {score}/5")

                new_row = pd.DataFrame({
                    "name": [st.session_state.user],
                    "score": [score]
                })

                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(FILE, index=False)

        elif page == "Applications":
            st.header("🏗 Height Calculation")

            d = st.number_input("Distance", min_value=0.0)
            angle = st.slider("Angle", 1, 90)

            if st.button("Calculate"):
                h = d * np.tan(np.radians(angle))
                st.success(f"Height = {h:.2f}")

        elif page == "My Analytics":
            st.header("📊 My Performance")

            user_data = df[df["name"] == st.session_state.user]

            if len(user_data) > 0:
                st.metric("Attempts", len(user_data))
                st.metric("Average Score", f"{user_data['score'].mean():.2f}")

                fig, ax = plt.subplots()
                ax.plot(user_data["score"], marker='o')
                st.pyplot(fig)
            else:
                st.info("No attempts yet")

    elif st.session_state.role == "Teacher":

        st.header("👩‍🏫 Teacher Dashboard")

        if len(df) > 0:

            st.subheader("All Student Records")
            st.dataframe(df)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Attempts", len(df))
            with col2:
                st.metric("Average Score", f"{df['score'].mean():.2f}")

            student_group = df.groupby("name")["score"].mean().reset_index()

            fig, ax = plt.subplots()
            ax.bar(student_group["name"], student_group["score"])
            ax.set_ylabel("Average Score")

            st.pyplot(fig)

        else:
            st.info("No student data available")
            st.subheader("Overall Performance")

            st.metric("Total Attempts", len(df))
            st.metric("Overall Avg", f"{df['score'].mean():.2f}")
        else:
            st.info("No data available")
