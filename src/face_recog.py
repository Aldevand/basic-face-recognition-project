# ========================================
# BLOK 1: IMPORT LIBRARY
# ========================================
import cv2
import numpy as np
import os

# ========================================
# BLOK 2: LOAD MODEL & NAMA ORANG
# ========================================
# Cek apakah file model ada
if not os.path.exists('../model/trainer.yml'):
    print("ERROR: File 'trainer.yml' tidak ditemukan!")
    print("   Jalankan 'train.py' dulu untuk training.")
    exit()

if not os.path.exists('../model/names.txt'):
    print("ERROR: File 'names.txt' tidak ditemukan!")
    print("   Pastikan training selesai.")
    exit()

# Load model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('../model/trainer.yml')

# Baca nama dari file
with open('../model/names.txt', 'r') as f:
    names = [line.strip() for line in f.readlines()]


print(f"Model berhasil dimuat!")
print(f"Orang yang dikenali: {names}")

# Load detector wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("ERROR: Gagal load haarcascade_frontalface_default.xml")
    exit()


# ========================================
# BLOK 3: BUKA KAMERA
# ========================================
cap = cv2.VideoCapture(0)

# Set resolusi (biar cepat & stabil)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Kurangi lag

# Coba buka kamera
if not cap.isOpened():
    print("ERROR: Kamera tidak bisa dibuka!")
    print("   Coba ganti 0 jadi 1 di VideoCapture(1)")
    exit()

print("\nKamera aktif! Hadap kamera dengan cahaya baik.")
print("Tekan 'q' untuk keluar.\n")


# ========================================
# BLOK 4: LOOP RECOGNITION REAL-TIME
# ========================================
while True:
    # Baca frame
    ret, frame = cap.read()
    if not ret:
        print("Gagal baca frame. Mencoba ulang...")
        continue

    # Flip horizontal
    frame = cv2.flip(frame, 1)

    # Ubah ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)  # Wajah minimal
    )

    # Proses setiap wajah
    for (x, y, w, h) in faces:
        # Crop wajah
        face_crop = gray[y:y+h, x:x+w]
        
        # Resize ke ukuran training (100x100)
        try:
            face_crop = cv2.resize(face_crop, (100, 100))
        except:
            continue  # Skip kalau error resize

        # PREDICT
        id_, confidence = recognizer.predict(face_crop)

        # Threshold: <110 = dikenali
        if confidence < 110:
            nama = names[id_]
            warna = (0, 255, 0)  # HIJAU
            teks = f"{nama} ({int(confidence)})"
        else:
            nama = "Unknown"
            warna = (0, 0, 255)  # MERAH
            teks = f"{nama} ({int(confidence)})"

        # Gambar kotak
        cv2.rectangle(frame, (x, y), (x+w, y+h), warna, 2)
        
        # Teks nama + confidence
        cv2.putText(frame, teks, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, warna, 2)

    # Tampilkan jumlah wajah
    cv2.putText(frame, f'Wajah: {len(faces)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow('Face Recognition - Petra & Yulan', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Keluar atas permintaan pengguna.")
        break


# ========================================
# BLOK 5: BERSIHKAN & TUTUP
# ========================================
cap.release()
cv2.destroyAllWindows()
print("Program selesai. Kamera ditutup.")