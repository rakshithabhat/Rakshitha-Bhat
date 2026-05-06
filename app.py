import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trigonometry App", layout="wide")

st.title("📐 Trigonometry Learning App")

# Sidebar navigation
st.sidebar.title("Navigation")
topic = st.sidebar.radio("Go to", ["Ratios", "Graphs", "Applications", "Analytics"])

# Initialize session state
if "scores" not in st.session_state:
    st.session_state.scores = []

# ------------------ RATIOS ------------------
if topic == "Ratios":
    st.header("📘 Trigonometric Ratios")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Concept")
        st.write("""
        sinθ = Opposite / Hypotenuse  
        cosθ = Adjacent / Hypotenuse  
        tanθ = Opposite / Adjacent  
        """)

    with col2:
        st.subheader("Real World Use")
        st.write("Used in measuring heights, distances, and navigation.")

    st.divider()

    st.subheader("🧠 Quiz")

    score = 0

    q1 = st.radio("1. sin(90°)?", ["0", "1", "-1"])
    q2 = st.radio("2. cos(0°)?", ["0", "1", "-1"])
    q3 = st.radio("3. tan(45°)?", ["0", "1", "2"])
    q4 = st.radio("4. sin(0°)?", ["0", "1", "-1"])
    q5 = st.radio("5. cos(90°)?", ["0", "1", "-1"])

    if st.button("Submit Quiz"):

        explanations = []

        if q1 == "1":
            score += 1
            explanations.append("Q1: Correct — sin(90°) = 1.")
        else:
            explanations.append("Q1: sin(90°) = 1 because sine is maximum at 90°.")

        if q2 == "1":
            score += 1
            explanations.append("Q2: Correct — cos(0°) = 1.")
        else:
            explanations.append("Q2: cos(0°) = 1 because cosine starts at maximum.")

        if q3 == "1":
            score += 1
            explanations.append("Q3: Correct — tan(45°) = 1.")
        else:
            explanations.append("Q3: tan(45°) = 1 (opposite = adjacent).")

        if q4 == "0":
            score += 1
            explanations.append("Q4: Correct — sin(0°) = 0.")
        else:
            explanations.append("Q4: sin(0°) = 0 because no vertical height.")

        if q5 == "0":
            score += 1
            explanations.append("Q5: Correct — cos(90°) = 0.")
        else:
            explanations.append("Q5: cos(90°) = 0 because adjacent becomes zero.")

        st.success(f"Your Score: {score}/5")
        st.session_state.scores.append(score)

        st.subheader("📘 Explanations")
        for exp in explanations:
            st.write(exp)

        if score == 5:
            st.balloons()

# ------------------ GRAPHS ------------------
elif topic == "Graphs":
    st.header("📈 Trigonometric Graph")

    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("y = sin(x)")

    st.pyplot(fig)

# ------------------ APPLICATIONS ------------------
elif topic == "Applications":
    st.header("🏗 Height & Distance")

    d = st.number_input("Distance from building (meters):", min_value=0.0)
    angle = st.slider("Angle of elevation (degrees):", 1, 90)

    if st.button("Calculate Height"):
        h = d * np.tan(np.radians(angle))
        st.success(f"Estimated Height: {h:.2f} meters")

# ------------------ ANALYTICS ------------------
elif topic == "Analytics":
    st.header("📊 Performance Analytics")

    if len(st.session_state.scores) > 0:
        scores = st.session_state.scores

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Attempts", len(scores))
            st.metric("Average Score", f"{sum(scores)/len(scores):.2f}")

        with col2:
            fig, ax = plt.subplots()
            ax.plot(scores, marker='o')
            ax.set_title("Score Progress")
            ax.set_xlabel("Attempt")
            ax.set_ylabel("Score")
            st.pyplot(fig)

        if scores[-1] < 3:
            st.warning("You need more practice on basics!")
        else:
            st.success("Good performance! Keep going!")

    else:
        st.info("No quiz attempts yet.")
