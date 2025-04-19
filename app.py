import streamlit as st
from model import predict_email_category

# Streamlit UI
st.title("📧 Email Classifier with PII Masking")
st.write("Paste an email below. It will be masked and classified.")

email_text = st.text_area("Enter your email text here:")

if st.button("Classify Email"):
    if not email_text.strip():
        st.warning("Please enter some text.")
    else:
        # Call the function from model.py to classify the email
        masked_email, prediction = predict_email_category(email_text)

        # Display the masked email and prediction result
        st.subheader("🔒 Masked Email")
        st.write(masked_email)

        st.subheader("📌 Predicted Type")
        st.success(prediction)
