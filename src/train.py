# ========================================
# BLOK 1: IMPORT LIBRARY
# ========================================
import cv2
import numpy as np
import os

# ========================================
# BLOK 2: SET PATH & NAMA ORANG
# ========================================
# path ke folder dataset training
DATA_PATH = r'D:\Project_Computer_Vision\data_train'  # Pakai raw string (r'') biar backslash aman

names = []  # Akan diisi otomatis sesuai nama folder

# ========================================
# BLOK 3: BUAT MODEL & DETECTOR
# ========================================
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Variabel training
faces = []
ids = []

print("Scanning dataset...")

# ========================================
# BLOK 4: BACA SEMUA FOLDER & FOTO
# ========================================
for idx, folder_name in enumerate(os.listdir(DATA_PATH)):
    folder_path = os.path.join(DATA_PATH, folder_name)
    
        # Cek apakah itu folder
    if not os.path.isdir(folder_path):
        continue
    
    # Tambahkan nama ke list
    names.append(folder_name)  # 'petra', 'yulan'
    print(f"[{idx}] Memproses: {folder_name} (ID: {idx})")
    
    # Baca semua file gambar di folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            
            if image is None:
                print(f"  Gagal baca: {filename}")
                continue
                
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Deteksi wajah di foto
            detected_faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
            
            for (x, y, w, h) in detected_faces:
                face_crop = gray[y:y+h, x:x+w]
                # Optional: resize biar konsisten
                face_crop = cv2.resize(face_crop, (100, 100))
                faces.append(face_crop)
                ids.append(idx)  # ID sesuai urutan folder
                print(f"    + Wajah ditemukan: {filename}")

print(f"\nTotal wajah terdeteksi: {len(faces)}")
if len(faces) == 0:
    print("ERROR: Tidak ada wajah terdeteksi. Cek foto & pencahayaan!")
    exit()

# ========================================
# BLOK 5: TRAIN MODEL
# ========================================
print("Training model LBPH...")
recognizer.train(faces, np.array(ids))
recognizer.save('trainer.yml')  # Simpan di folder project

# Simpan juga list nama ke file teks (biar recognition tahu)
with open('names.txt', 'w') as f:
    for name in names:
        f.write(name + '\n')

print(f"Training selesai!")
print(f"Model disimpan: trainer.yml")
print(f"Nama orang: {names}")