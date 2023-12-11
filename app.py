import os
from flask import Flask, redirect, request, render_template
from werkzeug.utils import secure_filename

import torch
from torchvision import models
from torchvision import transforms
from PIL import Image

UPLOAD_FOLDER = "./images"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)
alexnet = models.alexnet(pretrained=True)
alexnet.eval()


def alexnetPredict(img_path):
    img = Image.open(img_path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    out = alexnet(batch_t)
    with open("imagenet_classes.txt") as file:
        classes = [line.strip() for line in file.readlines()]

    _, indices = torch.sort(out, descending=True)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    prediction = [(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]
    return prediction


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
        return redirect("/")
    if file and is_allowed:
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    class_predictions = alexnetPredict(f"./images/{filename}")

    return render_template("index.html", prediction_result=class_predictions)


if __name__ == "__main__":
    app.run()
    # app.run(host="0.0.0.0", port=8000)
