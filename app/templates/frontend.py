import streamlit as st
import requests

st.title("🖼️ AI-Kunstkritiker")
st.write("Lade ein Kunstwerk hoch und erhalte eine kunstkritische Rezension.")

uploaded_file = st.file_uploader("Bild hochladen", type=["jpg", "png"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/analyze/", files=files)
    data = response.json()
    
    st.image(uploaded_file, caption="Hochgeladenes Kunstwerk")
    
    # Prüfen, ob die Schlüssel vorhanden sind
    if "style" in data:
        st.write("Stil:", data["style"])
    else:
        st.write("❌ Fehler: Kein Stil erkannt.")

    if "review" in data:
        st.write("Rezension:", data["review"])
    else:
        st.write("ℹ️ Keine Rezension verfügbar.")
        
    if "message" in data:
        st.write("Status:", data["message"])
    else:
        st.write("ℹ️ Keine Statusmeldung verfügbar.")