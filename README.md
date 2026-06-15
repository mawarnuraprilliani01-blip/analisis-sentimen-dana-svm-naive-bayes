# Analisis Sentimen Review Aplikasi DANA Menggunakan SVM dan Naive Bayes

## 1. Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap review pengguna aplikasi DANA. Review pengguna diklasifikasikan ke dalam kategori sentimen berdasarkan isi teks review. Model machine learning yang digunakan adalah **Support Vector Machine (SVM)** dan **Naive Bayes**.

Proyek ini dibuat sebagai tugas Machine Learning dengan mengikuti tahapan **CRISP-DM**, yaitu Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, dan Deployment.

## 2. Business Understanding

Aplikasi dompet digital seperti DANA banyak digunakan dalam aktivitas sehari-hari, seperti transfer uang, pembayaran tagihan, pembelian pulsa, dan transaksi online. Banyak pengguna memberikan ulasan melalui Google Play Store. Ulasan tersebut dapat berisi kepuasan, keluhan, kritik, atau saran.

Permasalahan yang ingin diselesaikan dalam proyek ini adalah bagaimana mengklasifikasikan review pengguna aplikasi DANA ke dalam sentimen tertentu secara otomatis menggunakan machine learning.

Tujuan proyek:

- Mengolah data review aplikasi DANA berbahasa Indonesia.
- Membangun model klasifikasi sentimen menggunakan SVM dan Naive Bayes.
- Membandingkan performa kedua model.
- Membuat aplikasi sederhana untuk memprediksi sentimen dari input review baru.

## 3. Data Understanding

Dataset yang digunakan berasal dari Kaggle:

**DANA Sentiment Analysis from Playstore Indonesia**  
https://www.kaggle.com/datasets/alexmariosimanjuntak/dana-app-sentiment-review-on-playstore-indonesia

Dataset berisi review pengguna aplikasi DANA dari Google Play Store Indonesia. Beberapa atribut yang digunakan dalam analisis antara lain:

- `content`: isi review pengguna
- `score`: rating pengguna
- `sentimen`: label sentimen review

Dataset ini cocok digunakan untuk analisis sentimen karena berisi teks review dan label sentimen.

## 4. Data Preparation

Tahapan persiapan data yang dilakukan:

1. Menghapus data kosong.
2. Mengambil kolom review dan label sentimen.
3. Membersihkan teks review dengan beberapa langkah:
   - Mengubah teks menjadi huruf kecil.
   - Menghapus URL.
   - Menghapus mention dan hashtag.
   - Menghapus angka.
   - Menghapus tanda baca.
   - Menghapus karakter selain huruf.
   - Menghapus spasi berlebih.
   - Menghapus stopword bahasa Indonesia.
4. Mengubah teks menjadi fitur numerik menggunakan **TF-IDF Vectorizer**.
5. Membagi data menjadi data latih dan data uji.

## 5. Modeling

Model yang digunakan dalam proyek ini:

### 5.1 Support Vector Machine (SVM)

SVM digunakan sebagai metode klasifikasi utama karena termasuk metode yang telah dipelajari di kelas. Pada proyek ini digunakan model **LinearSVC** karena cocok untuk klasifikasi teks berbasis TF-IDF.

### 5.2 Naive Bayes

Naive Bayes digunakan sebagai metode pembanding dan menjadi eksplorasi metode tambahan. Naive Bayes sering digunakan dalam klasifikasi teks karena bekerja berdasarkan probabilitas kemunculan kata pada setiap kelas.

## 6. Evaluation

Evaluasi model dilakukan menggunakan beberapa metrik:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Hasil evaluasi model:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| SVM | 0.775295 | 0.765807 | 0.775295 | 0.767569 |
| Naive Bayes | 0.748963 | 0.755694 | 0.748963 | 0.717220 |

Berdasarkan hasil evaluasi, model **SVM** memiliki performa lebih baik dibandingkan Naive Bayes. Oleh karena itu, model SVM digunakan sebagai model terbaik untuk deployment.

## 7. Deployment

Deployment dilakukan menggunakan **Streamlit**. Aplikasi memungkinkan pengguna memasukkan review aplikasi DANA, lalu sistem akan memprediksi sentimennya.

File deployment terdiri dari:

- `app.py`
- `requirements.txt`
- `model/best_model.pkl`
- `model/stopwords_indonesia.pkl`
- `model/hasil_evaluasi.pkl`

## 8. Struktur Folder

```text
Analisis-Sentimen-DANA/
├── app.py
├── requirements.txt
├── README.md
├── Analisis_Sentimen_DANA.ipynb
└── model/
    ├── best_model.pkl
    ├── stopwords_indonesia.pkl
    └── hasil_evaluasi.pkl
```

## 9. Cara Menjalankan Aplikasi Secara Lokal

Install library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

## 10. Link Deployment

Tambahkan link aplikasi setelah berhasil deploy:

```text
Link Streamlit: isi link deploy kamu di sini
```

## 11. Kesimpulan

Proyek ini berhasil membangun model analisis sentimen review aplikasi DANA menggunakan dua metode, yaitu SVM dan Naive Bayes. Berdasarkan hasil evaluasi, SVM memberikan performa terbaik dibandingkan Naive Bayes. Model terbaik kemudian digunakan dalam aplikasi sederhana berbasis Streamlit agar pengguna dapat memprediksi sentimen review secara langsung.
