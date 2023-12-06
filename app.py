import string
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    values = request.form.get("input")
    prediction_result = values
    file = request.files["file_input"]
    print(file.filename)
    return render_template("index.html", prediction_result=[prediction_result,file.filename ])


if __name__ == "__main__":
    app.run()
    # app.run(host="0.0.0.0", port=8000)

