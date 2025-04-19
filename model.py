import joblib
from model.masking import mask_pii

# Load the trained classifier model and vectorizer
def load_model():
    model = joblib.load("model/classifier.pkl")
    vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
    return model, vectorizer

# Function to predict email category
def predict_email_category(email_text):
    # Mask PII from the email text
    masked_email = mask_pii(email_text)
    
    # Load the model and vectorizer
    model, vectorizer = load_model()
    
    # Transform the masked email text using the vectorizer
    features = vectorizer.transform([masked_email])
    
    # Predict the category
    prediction = model.predict(features)[0]
    
    return masked_email, prediction
