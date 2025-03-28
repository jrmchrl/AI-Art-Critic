# 🎨 AI-Art-Critic

AI-Art-Critic ist eine Anwendung zur automatischen Kunstkritik basierend auf Bildanalysen und maschinellem Lernen. Die App verwendet ein lokales Modell zur Stilerkennung und Textgenerierung, um detaillierte kunstkritische Rezensionen zu erstellen.

## 🚀 Features
- Automatische Stilerkennung (Renaissance, Barock, Impressionismus, Moderne Kunst)
- Generierung kunstkritischer Rezensionen
- FastAPI-Backend
- Streamlit-Frontend
- Keine Abhängigkeit von externen API-Diensten

---

## 🛠️ Installation
### 1. Klone das Repository
```bash
git clone https://github.com/username/AI-Art-Critic.git
cd AI-Art-Critic
```

### 2. Erstelle eine virtuelle Umgebung
```bash
python -m venv venv
source venv/bin/activate  # für Linux/Mac
venv\Scripts\activate   # für Windows
```

### 3. Installiere die Abhängigkeiten
```bash
pip install -r requirements.txt
```

### 4. Umgebungsvariablen setzen
Erstelle eine `.env`-Datei im Projektverzeichnis mit folgendem Inhalt:
```
OPENAI_API_KEY=dein_api_schlüssel
```

---

## ⚙️ Training des Modells
Um das Modell für Kunstkritik zu trainieren, führe den folgenden Befehl aus:
```bash
python scripts/train.py
```
Das trainierte Modell wird im Ordner `models/` gespeichert.

---

## 🚀 Anwendung starten
### 1. FastAPI-Backend
Starte die API mit Uvicorn:
```bash
uvicorn app.main:app --reload
```
Die API ist dann verfügbar unter:
```
http://127.0.0.1:8000
```

### 2. Streamlit-Frontend
Starte die Benutzeroberfläche:
```bash
streamlit run app/templates/frontend.py
```
Die Benutzeroberfläche ist dann verfügbar unter:
```
http://localhost:8501
```

---

## 📝 Nutzung
Lade ein Bild über die Benutzeroberfläche hoch und erhalte eine kunstkritische Rezension basierend auf dem erkannten Kunststil.

---

## ✅ Beispiel-API-Aufruf über cURL
```bash
curl -X POST "http://127.0.0.1:8000/analyze/" -F "file=@path_to_image.jpg"
```

---

## 💡 Wichtige Hinweise
- Achte darauf, dass die `.env`-Datei nicht ins Repository eingecheckt wird. Füge die Datei zur `.gitignore` hinzu.
- Stelle sicher, dass die Modelle korrekt trainiert und im `models/`-Ordner abgelegt sind.

---

## 💻 Entwicklerhinweise
Falls du Änderungen am Modell vornimmst, trainiere es erneut mit:
```bash
python scripts/train.py
```

Viel Spaß mit der AI-Art-Critic! 🎨

