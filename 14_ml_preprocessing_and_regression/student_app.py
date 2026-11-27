
import streamlit as st, joblib, pandas as pd
st.title("🎓 Student Marks Predictor")
model = joblib.load("STM_ML.pkl")
hours = st.number_input("Study hours per day", min_value=0.0, max_value=12.0, value=6.0, step=0.5)
if st.button("Predict marks"):
    pred = model.predict(pd.DataFrame({"study_hours": [hours]}))[0]
    st.success(f"Predicted marks: {pred:.1f}")
