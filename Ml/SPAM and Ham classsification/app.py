from flask import Flask, render_template, request, url_for
import pickle

# Load vectorizer and model
with open('vectorizer.lb', 'rb') as f:
    vectorizer = pickle.load(f)

with open('spamclassification.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.form == "POST":
            messg = str(request.form["messg"])
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray()
            pred = model.predict(transformed_data)
            output = str(pred[0])
            return render_template("index.html", prediction=output)
    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}")
    

if __name__ == "__main__":
    app.run(debug=True)
