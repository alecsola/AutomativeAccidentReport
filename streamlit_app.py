import streamlit as st
from langchain_community.llms import Ollama
import time

st.title("📝 Accident Report Intake (Offline, Ollama)")

llm = Ollama(model="mistral")  # Swap for llama3 if you prefer

# Store answers
answers = {}

# Start form
with st.form("accident_form"):
    # Yes/No questions
    answers["Are you injured?"] = st.radio("Are you injured?", ["Yes", "No"])
    answers["Is there any property damage?"] = st.radio("Is there any property damage?", ["Yes", "No"])
    answers["Can the insurance recover the VAT on the vehicle?"] = st.radio("Can the insurance recover the VAT on the vehicle?", ["Yes", "No"])
    answers["Is the damage to the vehicle insured?"] = st.radio("Is the damage to the vehicle insured?", ["Yes", "No"])

    # Free text
    answers["What is your phone number?"] = st.text_input("What is your phone number?")
    answers["What is your insurance company?"] = st.text_input("What is your insurance company?")
    answers["What is the policy number of the insurance company?"] = st.text_input("What is the policy number of the insurance company?")
    answers["Who is your agent?"] = st.text_input("Who is your agent?")
    answers["Do you have a greencard? (If yes, what is the number of the greencard?)"] = st.text_input("Do you have a greencard? (If yes, what is the number?)")
    answers["Until when is the greencard valid?"] = st.text_input("Until when is the greencard valid?")

    # Multiselect impact location
    impact_options = [
        "Front", "Left Front", "Right Front", "Middle", "Left Middle", "Right Middle",
        "Top Middle", "Bottom Middle", "Bottom", "Bottom Right", "Bottom Left"
    ]
    answers["Where has the impact occurred?"] = st.multiselect(
        "Where has the impact occurred?",
        impact_options
    )

    # Text areas
    answers["Is there visible damage and where?"] = st.text_area("Is there visible damage and where?")
    answers["Any other remarks?"] = st.text_area("Any other remarks?")

    submitted = st.form_submit_button("Save Report")

    if submitted:
        # Save to file
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"accident_report_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for question, answer in answers.items():
                if isinstance(answer, list):
                    f.write(f"{question}\n{', '.join(answer)}\n\n")
                else:
                    f.write(f"{question}\n{answer}\n\n")

        st.success(f"✅ Report saved to `{filename}`")

        # Optional: Store values in individual variables
        injured = answers["Are you injured?"]
        property_damage = answers["Is there any property damage?"]
        vat_recovery = answers["Can the insurance recover the VAT on the vehicle?"]
        phone = answers["What is your phone number?"]
        insurance_company = answers["What is your insurance company?"]
        policy_number = answers["What is the policy number of the insurance company?"]
        agent = answers["Who is your agent?"]
        greencard_info = answers["Do you have a greencard? (If yes, what is the number of the greencard?)"]
        greencard_valid_until = answers["Until when is the greencard valid?"]
        damage_insured = answers["Is the damage to the vehicle insured?"]
        impact_location = answers["Where has the impact occurred?"]
        visible_damage = answers["Is there visible damage and where?"]
        remarks = answers["Any other remarks?"]

        # Display answers
        st.markdown("### ✅ Summary of Inputs:")
        for question, answer in answers.items():
            if isinstance(answer, list):
                st.write(f"**{question}**: {', '.join(answer)}")
            else:
                st.write(f"**{question}**: {answer}")
