import streamlit as st
import pandas as pd

def main():
    st.title("Survey App")
    st.write("Cats are better than dogs.")

    # Define the survey question and choices
    question = "Do you agree or disagree with the statement?"
    choices = ["Agree", "Disagree"]

    # Create an empty list to store the survey responses
    survey_responses = []

    # Display the survey question and choices
    response = st.radio(question, choices)

    # Prompt for an explanation in a free form text box
    explanation = st.text_area("Please provide a brief explanation for your choice.")

    # Map the response to a label (1 for agree, 0 for disagree)
    label = 1 if response == "Agree" else 0

    # Store the response and explanation in the survey_responses list
    survey_responses.append({"text": explanation, "label": label})

    # Convert the survey_responses list to a DataFrame
    survey_df = pd.DataFrame(survey_responses)

    # Display the collected survey data
    st.write("Survey Responses:")
    st.dataframe(survey_df)

if __name__ == "__main__":
    main()
