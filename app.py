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
        explanations.append("Q1: Correct ✅ — sin(90°) = 1 (maximum value of sine).")
    else:
        explanations.append("Q1: ❌ sin(90°) = 1 because sine is maximum at 90°.")

    if q2 == "1":
        score += 1
        explanations.append("Q2: Correct ✅ — cos(0°) = 1.")
    else:
        explanations.append("Q2: ❌ cos(0°) = 1 because cosine starts at maximum.")

    if q3 == "1":
        score += 1
        explanations.append("Q3: Correct ✅ — tan(45°) = 1.")
    else:
        explanations.append("Q3: ❌ tan(45°) = 1 (opposite = adjacent).")

    if q4 == "0":
        score += 1
        explanations.append("Q4: Correct ✅ — sin(0°) = 0.")
    else:
        explanations.append("Q4: ❌ sin(0°) = 0 because no vertical height.")

    if q5 == "0":
        score += 1
        explanations.append("Q5: Correct ✅ — cos(90°) = 0.")
    else:
        explanations.append("Q5: ❌ cos(90°) = 0 because adjacent side becomes zero.")

    st.success(f"Your Score: {score}/5")

    st.session_state.scores.append(score)

    st.subheader("📘 Explanations")
    for exp in explanations:
        st.write(exp)

    if score == 5:
        st.balloons()
