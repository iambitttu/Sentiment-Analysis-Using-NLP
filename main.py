import streamlit as st
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\bittu\PycharmProjects\sentimentanalysis\model.pkl")

# Define sentiment labels
sentiment_labels = {'P': 'Positive', 'N': 'Negative', 'O': 'Neutral'}

# Create Streamlit app
st.title("Sentiment Analysis")

# Input text area
user_input = st.text_area("Enter your text here:")

# Prediction button
if st.button("Predict"):
    # Perform sentiment prediction
    predicted_sentiment = model.predict([user_input])[0]
    predicted_sentiment_label = sentiment_labels[predicted_sentiment]

    # Display predicted sentiment
    st.write(f"Predicted Sentiment: {predicted_sentiment_label}")
