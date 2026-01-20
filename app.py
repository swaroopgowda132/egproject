from flask import Flask, render_template, request
import pickle # Used to load your trained ML model

app = Flask(_name_)

# Load the trained model (example)
# model = pickle.load(open('laptop_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capture data from the frontend form
    ram = request.form.get('ram')
    brand = request.form.get('brand')
    
    # Example logic: replace with actual model.predict()
    prediction = "Estimated Price: ₹ 55,000" 
    
    return f"<h1>{prediction}</h1>"

if _name_ == "_main_":
    app.run(debug=True)