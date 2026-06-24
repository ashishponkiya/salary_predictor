from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("salary_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    years = float(request.form['years'])

    prediction = model.predict([[years]])[0]

    return render_template(
        'index.html',
        prediction=round(prediction, 2)
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)