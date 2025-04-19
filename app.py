import streamlit as st
import joblib
from model.masking import mask_pii

# Load model and vectorizer
model = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Streamlit UI
st.title("📧 Email Classifier with PII Masking")
st.write("Paste an email below. It will be masked and classified.")

email_text = st.text_area("Enter your email text here:")

if st.button("Classify Email"):
    if not email_text.strip():
        st.warning("Please enter some text.")
    else:
        masked_email = mask_pii(email_text)
        features = vectorizer.transform([masked_email])
        prediction = model.predict(features)[0]

        st.subheader("🔒 Masked Email")
        st.write(masked_email)

        st.subheader("📌 Predicted Type")
        st.success(prediction)
