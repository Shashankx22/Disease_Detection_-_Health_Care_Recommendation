import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
file_path = 'dataset_mini_prj.csv'
data = pd.read_csv(file_path)

# Preprocess the symptoms: Convert symptoms to lowercase
data['symptoms'] = data['symptoms'].str.lower()

# Extract features using CountVectorizer
vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','), binary=True)
X = vectorizer.fit_transform(data['symptoms'])

# Target variable
y = data['disease']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load or train the model
try:
    final_model = joblib.load('model.pkl')
except FileNotFoundError:
    final_model = LogisticRegression(max_iter=1000)
    final_model.fit(X_train, y_train)
    joblib.dump(final_model, 'model.pkl')

# Evaluation function
def evaluate_model():
    y_pred = final_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy on test set: {accuracy}")
    print("Classification Report:\n", report)

def predict_disease(symptoms, threshold=0.1):
    symptoms = symptoms.lower()
    symptoms_list = [symptoms] if ',' not in symptoms else symptoms.split(',')

    symptoms_vector = vectorizer.transform([','.join(symptoms_list)])
    similarities = cosine_similarity(symptoms_vector, X).flatten()

    most_similar_idx = similarities.argmax()
    top_prob = similarities[most_similar_idx]

    if top_prob < threshold:
        return "No disease found", top_prob
    else:
        top_disease = data.iloc[most_similar_idx]['disease']
        return top_disease, top_prob

def get_disease_details(disease):
    if disease == "No disease found" or disease is None:
        return {'Symptoms': 'N/A', 'Disease': 'No disease found', 'Cure': 'N/A', 'Doctor': 'N/A', 'Risk': 'N/A', 'Probability': 'N/A'}
    details = data[data['disease'] == disease]
    if details.empty:
        return {'Symptoms': 'N/A', 'Disease': disease, 'Cure': 'N/A', 'Doctor': 'N/A', 'Risk': 'N/A', 'Probability': 'N/A'}
    details = details.iloc[0]
    return {
        'Symptoms': details['symptoms'],
        'Disease': details['disease'],
        'Cure': details['cure'],
        'Doctor': details['doctor'],
        'Risk': details['risk'],
        'Probability': 'N/A'  # Probability is handled in predict_disease function
    }

# Example usage:
if __name__ == "__main__":
    # Example input
    input_symptoms = "fever,cough,sore throat"

    # Predict the disease
    disease, probability = predict_disease(input_symptoms)
    print(f"Predicted Disease: {disease}, Probability: {probability}")

    # Get details of the predicted disease
    disease_details = get_disease_details(disease)
    print(f"Disease Details: {disease_details}")

    # Evaluate the model
    evaluate_model()

    # Optional: Evaluate the model on the test set
    y_pred = final_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy on test set: {accuracy}")
    print("Classification Report:\n", report)
