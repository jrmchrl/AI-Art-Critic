from fastapi import FastAPI, UploadFile, File
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import io
import openai
from dotenv import load_dotenv
import os

# Lade Umgebungsvariablen aus der .env Datei
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# FastAPI-Anwendung initialisieren
app = FastAPI()

# Modell laden
def load_model():
    model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
    model.fc = torch.nn.Linear(model.fc.in_features, 4)  # 4 Klassen
    model.load_state_dict(torch.load("models/art_style_model.pth", map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

# Transformationen für die Bildvorbereitung
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Klassenlabel
class_names = ["Renaissance", "Barock", "Impressionismus", "Moderne Kunst"]

# 💡 Hier kommt die Rezensionserstellung hin
# Funktion zur Erstellung der Rezension (neue API mit ChatCompletion)
def generate_review(style):
    prompt = f"Schreibe eine kunstkritische Rezension im Stil {style}. Beschreibe die Ästhetik, die Farben und die Emotionen, die das Kunstwerk vermittelt."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein Kunstkritiker, der detaillierte Rezensionen verfasst."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

@app.get("/")
async def root():
    return {"message": "AI Art Critic API is running"}

@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    try:
        # Bild lesen
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        
        # Bildvorbereitung
        image = transform(image).unsqueeze(0)

        # Vorhersage
        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)
            predicted_class = class_names[predicted.item()]

        # Rezension generieren
        review = generate_review(predicted_class)

        return {
            "style": predicted_class,
            "review": review,
            "message": "Bild erfolgreich analysiert"
        }
    except Exception as e:
        return {"error": str(e)}