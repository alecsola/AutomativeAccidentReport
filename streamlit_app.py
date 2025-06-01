import streamlit as st
from langchain_community.llms import Ollama
import time

st.title("📝 Accident Report Intake (Offline, Ollama)")

llm = Ollama(model="mistral")  # or "llama3" if preferred

# Dictionary to hold structured values
report_data = {}

# Impact options
impact_options = [
    "Front", "Left Front", "Right Front", "Middle", "Left Middle", "Right Middle",
    "Top Middle", "Bottom Middle", "Bottom", "Bottom Right", "Bottom Left"
]

with st.form("accident_form"):
    # Form inputs
    report_data['injury'] = st.radio("Are you injured?", ["yes", "no"])
    report_data['property_damage'] = st.radio("Is there any property damage?", ["yes", "no"])
    report_data['phone_number'] = st.text_input("What is your phone number?")
    report_data['vat_a'] = st.radio("Can the insurance recover the VAT on the vehicle?", ["yes", "no"])
    report_data['insurer_a'] = st.text_input("What is your insurance company?")
    report_data['policy_num'] = st.text_input("What is the policy number of the insurance company?")
    report_data['agent_a'] = st.text_input("Who is your agent?")
    report_data['green_number'] = st.text_input("Do you have a greencard? (If yes, what is the number?)")
    report_data['green_card_until'] = st.text_input("Until when is the greencard valid?")
    report_data['damage_insured_a'] = st.radio("Is the damage to the vehicle insured?", ["yes", "no"])
    
    impact_selection = st.multiselect(
        "Where has the impact occurred?",
        impact_options
    )
    report_data['initial_impact_a'] = ', '.join(impact_selection)

    report_data['visible_damage_a'] = st.text_area("Is there visible damage and where?")
    report_data['remarks_a'] = st.text_area("Any other remarks?")

    submitted = st.form_submit_button("Save Report")

    if submitted:
        # Save to file
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"accident_report_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for key, value in report_data.items():
                f.write(f"{key}: {value}\n")

        st.success(f"✅ Report saved to `{filename}`")

        # Optional preview
        st.markdown("### ✅ Summary of Saved Data:")
        for key, value in report_data.items():
            st.write(f"**{key}**: {value}")
