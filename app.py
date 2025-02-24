import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🚢 Titanic Dataset Chatbot")

question = st.text_input("Ask a question about the Titanic dataset:")

if st.button("Ask"):
    if question:
        response = requests.get("http://127.0.0.1:8000/ask", params={"question": question})
        answer = response.json().get("answer", "No response")
        st.write("### Answer:", answer)

        # Visualization Examples
        df = pd.read_csv("titanic.csv")
        if "histogram" in question.lower():
            st.write("### Age Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df["Age"].dropna(), bins=20, kde=True, ax=ax)
            st.pyplot(fig)
        elif "male" in question.lower() and "percentage" in question.lower():
            male_count = df[df["Sex"] == "male"].shape[0]
            total_count = df.shape[0]
            percentage = (male_count / total_count) * 100
            st.write(f"### {percentage:.2f}% of the passengers were male.")
