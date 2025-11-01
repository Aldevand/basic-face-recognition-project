import cv2

# 1. Load model deteksi wajah (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Buka kamera
cap = cv2.VideoCapture(0)  # 0 = kamera default

# Cek apakah kamera terbuka
if not cap.isOpened():
    print("Error: Kamera tidak bisa dibuka!")
    exit()

print("Tekan 'q' untuk keluar.")

while True:
    # 3. Baca frame dari kamera
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame!")
        break

    # 4. Ubah ke grayscale (wajah lebih mudah dideteksi)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Deteksi wajah
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,      # Ukuran pencarian
        minNeighbors=5,       # Tingkat akurasi
        minSize=(30, 30)      # Ukuran wajah minimal
    )

    # 6. Gambar kotak di setiap wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Kotak biru
        cv2.putText(frame, 'Wajah', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # 7. Tampilkan hasil
    cv2.imshow('Deteksi Wajah - Tekan Q untuk keluar', frame)

    # 8. Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 9. Bersihkan
cap.release()
cv2.destroyAllWindows()
print("Program selesai!")