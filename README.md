# 🧠 Basic Face Recognition System

Proyek ini merupakan implementasi dasar dari **sistem pengenalan wajah (Face Recognition)** menggunakan pustaka **OpenCV** dan algoritma **Local Binary Patterns Histograms (LBPH)**.  
Sistem ini dirancang untuk:

- Mendeteksi wajah secara **real-time** dari kamera.  
- Melatih model untuk mengenali individu tertentu.  
- Memberikan label identitas pada wajah yang terdeteksi.

---

## 📁 Struktur dan Fungsionalitas Utama

| File / Direktori | Fungsi | Keterangan |
|------------------|--------|------------|
| `train.py` | **Training Model** | Membaca data gambar dari folder pelatihan (`data_train/`), mengekstrak fitur wajah menggunakan **LBPH**, dan menghasilkan file model `trainer.yml` serta daftar nama `names.txt`. |
| `face_recog.py` | **Recognition System** | Menggunakan model `trainer.yml` untuk mendeteksi dan mengenali wajah secara **real-time** melalui kamera, serta menampilkan nama individu atau label *"Unknown"*. |
| `detection.py` / `detection1.py` | **Basic Detection** | Implementasi dasar untuk mendeteksi wajah menggunakan **Haar Cascade** tanpa proses pengenalan identitas. |
| `trainer.yml` | **Model Terlatih** | Output hasil pelatihan yang menyimpan parameter model **LBPH**. |
| `names.txt` | **Daftar ID** | Output hasil pelatihan yang menyimpan label ID (nama individu) yang dikenali. |
| `data_train/` | **Direktori Data (Lokal)** | Tempat penyimpanan foto-foto wajah individu yang digunakan untuk proses pelatihan. *(Tidak disertakan di repo publik)* |

---

## 🔒 Catatan Penting Mengenai Data Latih

Untuk menjaga **privasi dan integritas data**, direktori yang berisi gambar wajah individu (`data_train/`) **tidak diikutsertakan** dalam repositori ini.  

Repositori hanya mencakup:
- Kode sumber utama (`.py` files)  
- Model hasil pelatihan (`trainer.yml`)  
- Daftar nama individu (`names.txt`)

---

## ✅ Optimalisasi dan Kesimpulan

Efektivitas serta akurasi sistem pengenalan wajah sangat bergantung pada **kualitas dan kuantitas data pelatihan**.  
Berdasarkan prinsip dasar *Machine Learning*, model akan mencapai performa optimal jika memenuhi dua syarat utama berikut:

1. **Kuantitas Data yang Memadai**  
   Jumlah sampel wajah (foto) yang banyak dan beragam untuk setiap individu.

2. **Kualitas Data yang Bagus**  
   Data harus mencakup variasi kondisi dunia nyata seperti:
   - Perubahan pencahayaan  
   - Sudut pandang wajah (pose)  
   - Ekspresi wajah  
   - Resolusi gambar yang konsisten  

Dengan data latih yang baik, tingkat **false positive** (salah kenal) dan **false negative** (gagal kenal) dapat diminimalisir, menghasilkan sistem yang lebih **robust** dan **andal**.

---

📌 *Dikembangkan sebagai proyek dasar Computer Vision menggunakan OpenCV dan LBPH Face Recognizer.*
