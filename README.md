# 🧠 Face Recognition System 

Proyek ini merupakan implementasi dasar dari **sistem pengenalan wajah (Face Recognition)** menggunakan pustaka **OpenCV** dan algoritma **Local Binary Patterns Histograms (LBPH)**.  
Sistem ini mampu **mendeteksi dan mengenali wajah secara real-time** dari kamera, menampilkan label identitas (nama) pada wajah yang terdeteksi, serta menghitung jumlah wajah yang muncul di layar.

---

## 🎯 Tujuan Proyek

1. **Mendeteksi wajah secara otomatis** menggunakan *Haar Cascade Classifier*.  
2. **Melatih model pengenalan wajah** menggunakan algoritma *Local Binary Patterns Histogram (LBPH)*.  
3. **Melakukan identifikasi real-time** terhadap wajah yang terdeteksi dari kamera.  
4. **Menampilkan nama dan nilai confidence** sebagai indikator tingkat keyakinan model.

---

## 📁 Struktur Proyek

| File / Direktori | Fungsi | Keterangan |
|------------------|--------|------------|
| `train.py` | 🧩 **Training Model** | Membaca dataset dari folder `data_train/`, mendeteksi wajah dengan *Haar Cascade*, mengekstrak fitur menggunakan **LBPH**, dan menghasilkan model `trainer.yml` serta daftar nama `names.txt`. |
| `face_recog.py` | 🎥 **Recognition System** | Menggunakan model `trainer.yml` untuk mengenali wajah secara **real-time** melalui kamera, menampilkan nama individu dan confidence score. |
| `detection.py` / `detection1.py` | 🧠 **Basic Detection** | Implementasi awal deteksi wajah menggunakan *Haar Cascade Classifier* tanpa proses pengenalan identitas. |
| `trainer.yml` | 💾 **Model Terlatih** | File hasil pelatihan model LBPH yang disimpan dalam format terkompresi. |
| `names.txt` | 🧾 **Daftar Label ID** | Berisi daftar nama individu yang dikenali oleh sistem. |
| `data_train/` | 📸 **Dataset Lokal** | Folder berisi kumpulan foto wajah individu yang digunakan untuk proses training. *(Tidak disertakan di repositori publik demi privasi)* |

---

## ⚙️ Teknologi dan Metode

### 🧱 1. Haar Cascade Classifier
Digunakan untuk **deteksi wajah**.  
Metode ini berbasis pada *feature detection*, yaitu mengenali pola visual seperti mata, hidung, dan mulut menggunakan serangkaian filter (*cascade of classifiers*).  
Kelebihannya adalah deteksi cepat dan efisien pada citra *grayscale*.

### 🧩 2. Local Binary Patterns Histogram (LBPH)
Digunakan untuk **ekstraksi fitur dan klasifikasi wajah**.  
LBPH bekerja dengan langkah-langkah berikut:
- Mengubah gambar menjadi *grayscale*.  
- Membandingkan nilai piksel dengan tetangganya untuk menghasilkan pola biner lokal (*Local Binary Pattern*).  
- Mengubah hasilnya menjadi histogram tekstur yang mewakili ciri khas setiap wajah.  

LBPH dikenal stabil terhadap perubahan pencahayaan dan cocok untuk implementasi pengenalan wajah sederhana.

### 🔁 3. Real-Time Recognition
- Setiap frame dari webcam dianalisis menggunakan OpenCV.  
- Area wajah diberi *bounding box* berwarna (hijau untuk dikenali, merah untuk tidak dikenal).  
- Nama individu dan confidence score ditampilkan di atas wajah.  
- Sistem terus memproses hingga pengguna menekan tombol **‘q’**.

---

## 🔍 Insight dan Observasi

Dari hasil pengujian sistem terhadap beberapa kondisi nyata, model mampu mengenali wajah dengan baik ketika:
- Pencahayaan kamera cukup terang.  
- Wajah menghadap langsung ke kamera.  
- Dataset latih memiliki variasi ekspresi dan sudut pandang.

Namun, dari pengamatan selama eksperimen:
> 🔑 **Kunci utama performa sistem ada pada kualitas dan kuantitas dataset.**

Beberapa temuan penting:
- Jumlah foto per individu yang lebih banyak → meningkatkan keakuratan.  
- Variasi pencahayaan dan ekspresi → membantu model mengenali lebih fleksibel.  
- Gambar dengan resolusi rendah atau buram → menyebabkan penurunan akurasi.

Dengan dataset yang cukup dan representatif, tingkat **false positive** (salah kenal) dan **false negative** (tidak dikenali) dapat ditekan seminimal mungkin.

---

## ✅ Kesimpulan

Sistem ini berhasil mengimplementasikan tiga tahap utama:
1. **Deteksi wajah real-time** menggunakan Haar Cascade.  
2. **Pelatihan model wajah** menggunakan LBPH.  
3. **Pengenalan individu** dari input kamera.

Proyek ini dapat dijadikan **dasar untuk pengembangan sistem pengenalan wajah yang lebih lanjut**, seperti:
- Sistem absensi otomatis,  
- Keamanan berbasis kamera (CCTV smart system),  
- Autentikasi pengguna dengan wajah.

---

## ✅ Result/Output
<img width="1366" height="768" alt="Screenshot (1854)" src="https://github.com/user-attachments/assets/183c72f1-ee49-4cf4-989e-02bdc99a5d81" />
<img width="1366" height="768" alt="Screenshot (1848)" src="https://github.com/user-attachments/assets/f36e98ee-552f-4ae4-a911-4743246422f1" />
<img width="1366" height="768" alt="Screenshot (1872)" src="https://github.com/user-attachments/assets/9a575c0d-29a9-4e63-b639-d3f5d190c8f4" />
<img width="1366" height="768" alt="Screenshot (1874)" src="https://github.com/user-attachments/assets/870a618d-4777-459c-b017-97159211a2c1" />

---

## 🧩 Teknologi yang Digunakan
- **Python 3.11+**  
- **OpenCV (cv2)**  
- **NumPy**  
- **Haar Cascade Classifier**  
- **LBPH Face Recognizer**

---

📌 *Dikembangkan sebagai proyek dasar Computer Vision menggunakan OpenCV dan LBPH Face Recognizer oleh Petra.*
