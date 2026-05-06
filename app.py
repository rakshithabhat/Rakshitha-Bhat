import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📐 Trigonometry Learning App")

topic = st.selectbox("Select Topic", ["Ratios", "Graphs", "Applications"])

if topic == "Ratios":
    st.write("sinθ = Opp/Hyp, cosθ = Adj/Hyp, tanθ = Opp/Adj")

    q = st.radio("sin(90°)?", ["0", "1", "-1"])
    if st.button("Submit"):
        if q == "1":
            st.success("Correct")
        else:
            st.error("Wrong")

elif topic == "Graphs":
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)

elif topic == "Applications":
    d = st.number_input("Distance from building")
    angle = st.slider("Angle", 1, 90)

    if st.button("Calculate"):
        h = d * np.tan(np.radians(angle))
        st.success(f"Height = {h:.2f}")
