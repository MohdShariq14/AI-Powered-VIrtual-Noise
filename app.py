# What: Ye file tumhara Flask backend code hoga. Yahan tum Flask routes define karoge,
#        jisme tum model ko load karoge aur prediction API banayenge.

# ai_virtual_nose/app/app.py

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
# model = joblib.load('../model.pkl')  # Adjust path as needed
model = joblib.load('D:/aIvIRTUALnOSE/model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # This will render the HTML frontend

@app.route('/predict', methods=['GET'])
def predict():
    # Get values from URL query parameters
    mq2 = float(request.args.get('mq2'))
    mq3 = float(request.args.get('mq3'))
    mq135 = float(request.args.get('mq135'))

    # Prepare the feature array for prediction
    features = np.array([[mq2, mq3, mq135]])

    # Make prediction using the trained model
    prediction = model.predict(features)

    # Return prediction as JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
