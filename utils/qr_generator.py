import json
import qrcode
import os
from dotenv import load_dotenv
from PIL import Image

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
LOGO_PATH = "resources/img/logo/laurel.png"
LOGO_SIZE_RATIO = 0.22  # % della larghezza del QR occupata dal logo (max consigliato ~0.25-0.28)


def add_logo(qr_img, logo_path, logo_size_ratio=LOGO_SIZE_RATIO):
    """Incolla un logo al centro dell'immagine QR, con bordo bianco di sicurezza."""
    if not os.path.exists(logo_path):
        print(f"⚠️  Logo non trovato in '{logo_path}', QR generato senza logo.")
        return qr_img

    qr_img = qr_img.convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    qr_width, qr_height = qr_img.size
    logo_max_size = int(qr_width * logo_size_ratio)
    logo.thumbnail((logo_max_size, logo_max_size))

    # Bordo bianco intorno al logo, per non "sporcare" i moduli neri adiacenti
    border_size = 10
    logo_with_border = Image.new(
        "RGBA",
        (logo.width + border_size * 2, logo.height + border_size * 2),
        (255, 255, 255, 255)
    )
    logo_with_border.paste(logo, (border_size, border_size), logo)

    pos = (
        (qr_width - logo_with_border.width) // 2,
        (qr_height - logo_with_border.height) // 2
    )
    qr_img.paste(logo_with_border, pos, logo_with_border)
    return qr_img


def main():
    # 1. Crea la cartella per i file finali se non esiste
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"📁 Creata la cartella '{OUTPUT_DIR}'")

    # 2. Leggi il file degli invitati
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"❌ Errore: File {JSON_PATH} non trovato.")
        return

    # Entra nella chiave "guests"
    guests = data.get("guests", {})

    print(f"🔍 Trovati {len(guests)} invitati nel database. Inizio la generazione...\n")

    # Itera su (chiave, valore) invece che su una lista
    for guest_id, guest in guests.items():
        guest_name = guest.get('name', guest_id)

        if guest_id == "user":
            print(f"⚠️ Saltato l'invitato di default 'user'.")
            continue

        # Crea l'URL personalizzato concatenando la base e l'hash
        custom_url = f"{BASE_URL}#{guest_id}"

        # Inizializza l'oggetto QRCode con alta ridondanza per la stampa
        qr = qrcode.QRCode(
            version=1,
            # ERROR_CORRECT_H (High): tollera fino al ~30% di area coperta,
            # indispensabile per poter inserire il logo al centro
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,  # Dimensione dei pixel del QR
            border=4,     # Bordo bianco di sicurezza (zona di quiete)
        )

        qr.add_data(custom_url)
        qr.make(fit=True)

        # Genera l'immagine in bianco e nero
        img = qr.make_image(fill_color="black", back_color="white")

        # Inserisce la corona d'alloro al centro (se presente)
        img = add_logo(img, LOGO_PATH)

        # Salva il file nominandolo con l'ID dell'invitato
        filename = f"{OUTPUT_DIR}/{guest_id}.png"
        img.save(filename)

        print(f"✅ Generato: {filename} (Destinazione: {guest_name})")

    print(f"\n🎉 Successo! Tutti i QR Code pronti per la tipografia sono nella cartella '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    main()