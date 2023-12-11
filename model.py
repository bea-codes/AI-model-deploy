import torch
from torchvision import models
from torchvision import transforms
from PIL import Image


def alexnetPredict(img_path):
    transform = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    img = Image.open(img_path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    alexnet = models.alexnet(pretrained=True)
    alexnet.eval()
    out = alexnet(batch_t)
    with open("imagenet_classes.txt") as file:
        classes = [line.strip() for line in file.readlines()]
    _, indices = torch.sort(out, descending=True)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    prediction = [(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]
    return prediction


if __name__ == "__main__":
    pass
