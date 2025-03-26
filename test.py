from dotenv import load_dotenv
import os

# Lade die Umgebungsvariablen
load_dotenv()

# Hole den API-Schlüssel
api_key = os.getenv("OPENAI_API_KEY")

# Überprüfen, ob die Variable geladen wurde
if api_key:
    print(f"✅ API-Schlüssel geladen: {api_key[:5]}... (gekürzt)")
else:
    print("❌ API-Schlüssel nicht gefunden")