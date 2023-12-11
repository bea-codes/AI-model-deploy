import os
from flask import Flask, redirect, request, render_template
from werkzeug.utils import secure_filename
from model import alexnetPredict

UPLOAD_FOLDER = "./images"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # values = request.form.get("input")
    # prediction_result = values
    file = request.files["file_input"]
    is_allowed = allowed_file(file.filename)
    if is_allowed == False:
        return redirect('/')
    if file and is_allowed:
        filename = secure_filename(file.filename)
        print(filename)
        file.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"], filename
            )
        )
    
    alexnetPredict(f"./images/{filename}")

    return render_template("index.html", prediction_result=[file.filename])


if __name__ == "__main__":
    app.run()
    # app.run(host="0.0.0.0", port=8000)
