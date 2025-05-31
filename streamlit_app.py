import streamlit as st
from langchain_community.llms import Ollama
import time

st.title("📝 Accident Report Intake (Offline, Ollama)")

llm = Ollama(model="mistral")  # You can swap this for llama3 if installed

# Define the questions
questions = [
    "Are you injured?",
    "Is there any property damage?",
    "What is your phone number?",
    "What is your insurance company?",
    "What is the policy number of the insurance company?",
    "Who is your agent?",
    "Do you have a greencard? (If yes, what is the number of the greencard?)",
    "Until when is the greencard valid?",
    "Is the damage to the vehicle insured?",
    "Where has the impact occurred? (front, left front, right front, middle, left middle, right middle, top middle, bottom middle, bottom, bottom right or bottom left)",
    "Is there visible damage and where?",
    "Any other remarks?"
]

# Store answers here
answers = {}

# UI form
with st.form("accident_form"):
    for q in questions:
        answers[q] = st.text_input(q)

    submitted = st.form_submit_button("Save Report")

    if submitted:
        # Save to file
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"accident_report_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for question, answer in answers.items():
                f.write(f"{question}\n{answer}\n\n")

        st.success(f"✅ Report saved to `{filename}`")

        # Save variables separately (you can use this for further processing)
        (
            injured,
            property_damage,
            phone,
            insurance_company,
            policy_number,
            agent,
            greencard_info,
            greencard_valid_until,
            damage_insured,
            impact_location,
            visible_damage,
            remarks
        ) = [answers[q] for q in questions]

        st.markdown("### ✅ Summary of Inputs:")
        for question, answer in answers.items():
            st.write(f"**{question}**: {answer}")
