# Disease_Detection_and_Health_Care_Recommendation<br /><br />


Mini Project on Machine Learning based Disease Detection and Health-Care Recommendation System<br /><br />




Welcome to the Disease Detection and Health Care Recommendation System project repository. This project is a machine learning-based web application that allows users to enter symptoms and receive predictions for possible diseases along with recommended treatments, risk levels, and suggested doctors. It aims to provide early detection and optimal care recommendations to users based on their symptoms.<br /><br />



Features<br /><br />


Symptom Input: Users can enter symptoms in a text box and submit them for analysis.<br />

Disease Prediction: The application uses a trained machine learning model to predict possible diseases based on the entered symptoms.<br />

Health Care Recommendations: Provides recommended treatments, doctors, and risk levels associated with the predicted diseases.<br />

Probability of Prediction: Displays the probability of the predicted disease.<br />

Responsive Design: The user interface is designed to be responsive and user-friendly.<br />


Project Structure<br />

SE_ML_Model<br />

     static<br />

        css<br />

          styles.css  <br />

          bg.gif<br />

     templates<br />

         index.html<br />

     app.py<br />

     model.py<br />

     dataset.csv<br />



static/: Contains static files like CSS and background images.<br />

templates/: Contains HTML templates for the web pages.<br />

app.py: The main Flask application file.<br />

model.py: Contains the machine learning model and related functions.<br />

dataset.csv: The dataset used to train the machine learning model.<br />


Requirements
To run this project, you need:

Python 3.x installed on your machine.
Flask, a web framework for Python.
Pandas for handling the dataset.
Scikit-learn (or another machine learning library) for model training and predictions.


How to Run
Download the repository to your local machine.

Ensure you have the necessary Python packages installed. These include Flask for running the web application, Pandas for dataset handling, and Scikit-learn for machine learning tasks. You may manually install these if they are not already available.

Run the application by executing the app.py file. Make sure your Python environment is properly set up.

Open your browser and navigate to the link provided after running the app.py file. Typically, the application will be hosted on:

http://127.0.0.1:5000/

Start using the web app by entering symptoms, and the system will predict possible diseases and offer healthcare recommendations.



 
