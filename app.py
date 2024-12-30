from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model_filename = 'burn_rate_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form input
        features = [float(x) for x in request.form.values()]  # Ensure all 3 features are collected
        features_array = np.array(features).reshape(1, -1)  # Reshape to match model input

        # Make prediction
        prediction = model.predict(features_array)

        # Return the result
        return render_template('index.html', prediction_text=f'Predicted Burn Rate: {prediction[0]:.2f}')
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
