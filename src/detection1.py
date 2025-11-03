# ========================================
# BLOK 1: IMPORT LIBRARY
# ========================================
import cv2
import time  # Untuk jeda waktu

# ========================================
# BLOK 2: LOAD MODEL DETEKSI WAJAH
# ========================================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ========================================
# BLOK 3: BUKA KAMERA
# ========================================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Gunakan DirectShow di Windows (lebih stabil)
cap.set(cv2.CAP_PROP_FPS, 30)             # Set frame rate target
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)    # Atur resolusi (lebar)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)   # Atur resolusi (tinggi)

time.sleep(1)  # Jeda 1 detik agar kamera siap

if not cap.isOpened():
    print("ERROR: Kamera gagal dibuka!")
    exit()

print("Kamera aktif. Tekan 'q' untuk keluar.")


# ========================================
# BLOK 4: LOOP UTAMA (Real-Time Processing)
# ========================================
while True:
    # --- 4.1 Baca frame dari kamera ---
    ret, frame = cap.read()
    if not ret:
        print("Gagal baca frame!")
        break

    # (Opsional) kecilkan ukuran frame agar fps lebih tinggi
    frame = cv2.resize(frame, (640, 480))

    # --- 4.2 Ubah ke grayscale ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # --- 4.3 Deteksi wajah ---
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # --- 4.4 Gambar kotak di setiap wajah ---
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Wajah', (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # --- 4.5 Tampilkan jumlah wajah ---
    jumlah_wajah = len(faces)
    cv2.putText(frame, f'Wajah: {jumlah_wajah}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # --- 4.6 Tampilkan frame hasil ---
    cv2.imshow('Deteksi Wajah - Tekan Q untuk keluar', frame)

    # --- 4.7 Keluar jika tekan tombol Q ---
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ========================================
# BLOK 5: BERSIHKAN & TUTUP
# ========================================
cap.release()
cv2.destroyAllWindows()
print("Program selesai. Kamera ditutup.")
