import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📐 Trigonometry Learning App")

# Initialize session state for score history
if "scores" not in st.session_state:
    st.session_state.scores = []

topic = st.selectbox("Select Topic", ["Ratios", "Graphs", "Applications", "Analytics"])

# ------------------ RATIOS ------------------
if topic == "Ratios":
    st.write("sinθ = Opp/Hyp, cosθ = Adj/Hyp, tanθ = Opp/Adj")

    st.subheader("Quiz")

    score = 0

    q1 = st.radio("1. sin(90°)?", ["0", "1", "-1"])
    q2 = st.radio("2. cos(0°)?", ["0", "1", "-1"])
    q3 = st.radio("3. tan(45°)?", ["0", "1", "2"])
    q4 = st.radio("4. sin(0°)?", ["0", "1", "-1"])
    q5 = st.radio("5. cos(90°)?", ["0", "1", "-1"])

    if st.button("Submit Quiz"):
        if q1 == "1":
            score += 1
        if q2 == "1":
            score += 1
        if q3 == "1":
            score += 1
        if q4 == "0":
            score += 1
        if q5 == "0":
            score += 1

        st.success(f"Your Score: {score}/5")

        # Save score
        st.session_state.scores.append(score)

        if score == 5:
            st.balloons()

# ------------------ GRAPHS ------------------
elif topic == "Graphs":
    st.header("Graph of sin(x)")

    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("y = sin(x)")

    st.pyplot(fig)

# ------------------ APPLICATIONS ------------------
elif topic == "Applications":
    st.header("Height and Distance")

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

        st.write(f"Total Attempts: {len(scores)}")
        st.write(f"Average Score: {sum(scores)/len(scores):.2f}")

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
    d = st.number_input("Distance from building (meters):", min_value=0.0)
    angle = st.slider("Angle of elevation (degrees):", 1, 90)

    if st.button("Calculate Height"):
        h = d * np.tan(np.radians(angle))
        st.success(f"Estimated Height: {h:.2f} meters")
