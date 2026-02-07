from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    year = request.form["year"]
    return f"Car Year is: {year}"

if __name__ == "__main__":
    app.run()
