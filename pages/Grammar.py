import os
import streamlit as st
import openai

# Set up OpenAI API
openai.api_key = st.secrets["openai_api_key"]
st.set_page_config(page_title="Grammar Helper", page_icon=":scales:")

def generate_grammar_correction(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please correct the following text for grammar: \"{prompt}\"",
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.3,
    )
    return response.choices[0].text.strip()

st.title("Grammar Correction with OpenAI")
st.markdown("Welcome to the grammar correction app! This app uses OpenAI to improve the grammar of your text.")

user_text = st.text_area("Enter your text here:", "")

if st.button("Correct Grammar"):
    if user_text:
        corrected_text = generate_grammar_correction(user_text)
        st.write("Original text:", user_text)
        st.write("Corrected text:", corrected_text)
    else:
        st.warning("Please enter some text to correct.")
else:
    st.write("Click the button to correct the grammar of your text.")


st.components.v1.html(
    """


    """,
    height=0,
)
