import os
from PIL import Image
import torchvision.transforms as transforms

data_dir = "data"
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

for style in os.listdir(data_dir):
    style_dir = os.path.join(data_dir, style)
    for img_name in os.listdir(style_dir):
        img_path = os.path.join(style_dir, img_name)
        try:
            img = Image.open(img_path).convert("RGB")
            img = transform(img)
            print(f"Processed: {img_name}")
        except Exception as e:
            print(f"Fehler bei {img_name}: {e}")