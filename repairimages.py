import os
from PIL import Image

for root, dirs, files in os.walk("data"):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp")):
            path = os.path.join(root, file)
            try:
                # Bild öffnen
                with Image.open(path) as img:
                    img.verify()  # Bildintegrität prüfen
                    print(f"✅ Bild in Ordnung: {path}")
            except Exception as e:
                print(f"❌ Fehler mit Bild: {path}, {e}")
                # Versuch der Reparatur durch Neuspeicherung
                try:
                    with Image.open(path) as img:
                        new_path = f"{path}_fixed.png"
                        img.save(new_path)
                        print(f"🔧 Bild repariert und gespeichert unter: {new_path}")
                except Exception as repair_error:
                    print(f"⚠️ Reparatur fehlgeschlagen: {repair_error}")