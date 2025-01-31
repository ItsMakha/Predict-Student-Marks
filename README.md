🎯 Student Marks Prediction
📌 Overview
This project is a machine learning model that predicts students' final grades (G3) based on factors like previous grades (G1, G2), study time, failures, and absences. It utilizes linear regression to make predictions based on historical student performance data.

✨ Features
📊 Uses Linear Regression for predicting student performance
🔍 Analyzes study time, past grades, failures, and absences
🎯 Achieves accuracy evaluation using Scikit-Learn
📈 Provides model coefficients and intercept for interpretation
🛠️ Technologies Used
Python
NumPy (for numerical operations)
Pandas (for data handling)
Scikit-Learn (for machine learning)
📦 Installation
Prerequisites
Ensure you have Python 3.7+ installed.

Steps
Clone this repository:
sh
Copy
Edit
git clone https://github.com/ItsMakha/student-marks-prediction.git
cd student-marks-prediction
Install dependencies:
sh
Copy
Edit
pip install pandas numpy scikit-learn
Place the dataset (student-mat.csv) in the project directory.
Run the script:
sh
Copy
Edit
python predict_marks.py  
View the predictions and model accuracy in the terminal.
🚀 How It Works
Loads student data from a CSV file.
Selects key features (G1, G2, study time, failures, absences).
Splits the data into training and testing sets.
Trains a linear regression model on the training data.
Evaluates the model’s accuracy on test data.
Makes predictions and compares them with actual values.
📸 Example Output
yaml
Copy
Edit
Accuracy: 0.85  
Coefficient: [0.15, 0.90, 0.12, -0.30, 0.05]  
Intercept: 1.75  
Prediction: 14.5, Features: [12, 14, 2, 0, 5], Actual: 15  
🔧 Future Enhancements
Explore more features for better predictions
Implement polynomial regression for better accuracy
Create a web-based UI to input student details and get predictions
