from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model pipeline
model_pipeline = joblib.load('model_pipeline.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])

        # Create DataFrame from input features
        features = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })

        # Make prediction
        prediction = model_pipeline.predict(features)

        # Render the result on the same page
        return render_template('index.html', prediction_text='Predicted Price: ${:.2f}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)