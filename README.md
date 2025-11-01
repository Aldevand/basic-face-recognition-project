Ringkasan Proyek: Basic Face Recognition System

Proyek ini adalah implementasi dasar dari sistem pengenalan wajah (Face Recognition) menggunakan pustaka OpenCV dan algoritma Local Binary Patterns Histograms (LBPH). Sistem ini dirancang untuk mendeteksi wajah secara real-time dari kamera, melatih model untuk mengenali individu tertentu, dan memberikan label identitas pada wajah yang terdeteksi.

📄 Struktur dan Fungsionalitas Utama

File

Fungsi

Keterangan

train.py

Training Model

Membaca data gambar dari folder pelatihan, mengekstrak fitur wajah menggunakan LBPH, dan menghasilkan file model trainer.yml serta daftar nama names.txt.

face_recog.py

Recognition System

Menggunakan model trainer.yml yang sudah dilatih untuk mendeteksi dan mengenali wajah secara real-time melalui kamera, menampilkan nama individu atau label "Unknown".

detection.py/detection1.py

Basic Detection

Implementasi dasar untuk hanya mendeteksi wajah menggunakan Haar Cascade tanpa proses pengenalan identitas.

trainer.yml

Model Terlatih

Output dari proses training yang menyimpan parameter model LBPH.

names.txt

Daftar ID

Output dari proses training yang menyimpan label ID (nama) individu yang dikenali.

data_train/

Direktori Data (Lokal)

Direktori tempat foto-foto wajah individu disimpan untuk proses pelatihan.

🔒 Catatan Penting Mengenai Data Latih

Untuk menjaga privasi dan integritas, direktori yang berisi gambar-gambar wajah individu (data_train/) tidak diikutsertakan (private) dalam repositori ini. Repositori hanya mencakup kode sumber, model (trainer.yml), dan daftar nama (names.txt) yang merupakan hasil dari proses pelatihan.

✅ Kesimpulan tentang Optimalisasi Model

Efektivitas dan akurasi sistem pengenalan wajah ini secara langsung berkorelasi dengan kualitas data pelatihan. 

 Berdasarkan prinsip dasar Machine Learning, model akan mencapai tingkat optimalitas dan generalisasi yang lebih tinggi jika dipenuhi dua syarat utama:

Kuantitas Data yang Memadai: Jumlah sampel wajah (foto/gambar) yang banyak dan beragam untuk setiap individu.

Kualitas Data yang Bagus: Data harus mencakup variasi kondisi dunia nyata, seperti perubahan pencahayaan, sudut pandang wajah (pose), ekspresi, dan resolusi yang konsisten.

Dengan data latih yang kuantitas dan kualitasnya terjamin, false positive (salah kenal) dan false negative (gagal kenal) dapat diminimalisir secara signifikan, menghasilkan sistem yang lebih robust dan andal.
