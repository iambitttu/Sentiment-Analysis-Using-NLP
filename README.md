# Sentiment Analysis Model

## 1. Data Preprocessing Steps

  - Tokenization: Splitting the text into individual words or tokens.
  - Lowercasing: Converting all text to lowercase to ensure consistency.
  - Removing special characters: Eliminating non-alphanumeric characters, punctuation, and symbols.
  - Stopword removal: Removing common words (e.g., "the", "is", "and") that do not carry significant meaning.
  - Lemmatization: Converting words to their base or root form to reduce inflectional forms.

## 2. Model Architecture and Parameters

- The model used for sentiment analysis is Logistic Regression.
- The model architecture consists of a TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer and a logistic regression classifier.
- Parameters:
  - TF-IDF Vectorizer:
    - max_features: 5000
    - ngram_range: (1, 2)
  - Logistic Regression:
    - C (Inverse of regularization strength): 1.0
    - Solver: 'lbfgs'
    - Multi_class: 'auto'

## 3. Training Process

- The model was trained using the following hyperparameters:
  - Batch size: 1
  - Number of epochs: 10
    
## 4. Evaluation Results and Analysis:

  - The model achieved satisfactory performance
  - Precision, recall, and F1-score indicate balanced performance across classes.
  - Further analysis could be conducted on misclassified instances to identify potential areas for improvement.

## 5. Instructions for Using the Deployed Model

- The deployed model can be accessed via the Streamlit web application.
- Enter text into the provided text area.
- Click the "Predict" button to receive the sentiment prediction.
