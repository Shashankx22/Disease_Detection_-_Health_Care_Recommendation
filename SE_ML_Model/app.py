from flask import Flask, render_template, request
from model import predict_disease, get_disease_details

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    details = None
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        top_disease, top_prob = predict_disease(symptoms)

        if top_disease == "No disease found":
            details = {'Symptoms': symptoms, 'Disease': 'Symptom not available', 'Cure': 'N/A', 'Doctor': 'N/A', 'Risk': 'N/A', 'Probability': 'N/A'}
        else:
            details = get_disease_details(top_disease)
            details['Probability'] = f"{top_prob:.4f}"
            details['Symptoms'] = symptoms

    return render_template('index.html', details=details)

if __name__ == "__main__":
    app.run(debug=True)
