{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76dd3972-0dc1-4433-9812-bcca21d87add",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "from model.masking import mask_pii\n",
    "\n",
    "# Load model and vectorizer\n",
    "model = joblib.load(\"model/classifier.pkl\")\n",
    "vectorizer = joblib.load(\"model/vectorizer.pkl\")\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"📧 Email Classifier with PII Masking\")\n",
    "st.write(\"Paste an email below. It will be masked and classified.\")\n",
    "\n",
    "email_text = st.text_area(\"Enter your email text here:\")\n",
    "\n",
    "if st.button(\"Classify Email\"):\n",
    "    if not email_text.strip():\n",
    "        st.warning(\"Please enter some text.\")\n",
    "    else:\n",
    "        masked_email = mask_pii(email_text)\n",
    "        features = vectorizer.transform([masked_email])\n",
    "        prediction = model.predict(features)[0]\n",
    "\n",
    "        st.subheader(\"🔒 Masked Email\")\n",
    "        st.write(masked_email)\n",
    "\n",
    "        st.subheader(\"📌 Predicted Type\")\n",
    "        st.success(prediction)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
