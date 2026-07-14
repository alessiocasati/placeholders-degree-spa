import json
import qrcode
import os
from dotenv import load_dotenv

# --- CONFIGURAZIONE ---
# 1. Carica le variabili dal file .env.local
load_dotenv(".env.local")

# 2. Leggi la variabile (se non esiste, restituisce None)
BASE_URL = os.getenv("BASE_URL")

# Controllo di sicurezza: blocca lo script se ti sei dimenticato di impostare l'URL
if not BASE_URL:
    print("❌ Errore critico: BASE_URL non trovato. Controlla il file .env.local!")
    exit(1)

# Il percorso al tuo file JSON secondo la struttura che abbiamo definito
JSON_PATH = "resources/data/guests.json" 
OUTPUT_DIR = "resources/img/qrcodes"  # Cartella dove salvare i QR Code generati

def main():
    # 1. Crea la cartella per i file finali se non esiste
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"📁 Creata la cartella '{OUTPUT_DIR}'")

    # 2. Leggi il file degli invitati
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            guests = json.load(file)
    except FileNotFoundError:
        print(f"❌ Errore: File {JSON_PATH} non trovato.")
        return

    print(f"🔍 Trovati {len(guests)} invitati nel database. Inizio la generazione...\n")

    # 3. Cicla ogni invitato e genera il suo QR
    for guest in guests:
        # Assumiamo che il tuo JSON abbia un campo 'id' (es. "zio-mario")
        guest_id = guest.get('id') 
        guest_name = guest.get('name', guest_id)

        if not guest_id:
            print(f"⚠️ Saltato un record senza 'id': {guest}")
            continue
            
        # Crea l'URL personalizzato concatenando la base e l'hash
        custom_url = f"{BASE_URL}#{guest_id}"
        
        # Inizializza l'oggetto QRCode con alta ridondanza per la stampa
        qr = qrcode.QRCode(
            version=1,
            # ERROR_CORRECT_H (High) permette al QR di essere letto anche se coperto al 30%
            error_correction=qrcode.constants.ERROR_CORRECT_H, 
            box_size=10, # Dimensione dei pixel del QR
            border=4,    # Bordo bianco di sicurezza (zona di quiete)
        )
        
        qr.add_data(custom_url)
        qr.make(fit=True)

        # Genera l'immagine in bianco e nero
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Salva il file nominandolo con l'ID dell'invitato
        filename = f"{OUTPUT_DIR}/{guest_id}.png"
        img.save(filename)
        
        print(f"✅ Generato: {filename} (Destinazione: {guest_name})")

    print(f"\n🎉 Successo! Tutti i QR Code pronti per la tipografia sono nella cartella '{OUTPUT_DIR}'.")

if __name__ == "__main__":
    main()