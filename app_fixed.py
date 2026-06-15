import streamlit as st
import joblib
import re
import string

# Load model dan stopwords
# File .pkl diletakkan sejajar dengan app.py di repository GitHub
model = joblib.load("best_model.pkl")
stopwords_indonesia = joblib.load("stopwords_indonesia.pkl")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", " ", text)
    text = re.sub(r"@\w+|#\w+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [word for word in words if word not in stopwords_indonesia and len(word) > 2]

    return " ".join(words)

st.title("Analisis Sentimen Review Aplikasi DANA")
st.write("Aplikasi ini memprediksi sentimen review pengguna aplikasi DANA menggunakan model machine learning terbaik.")

review = st.text_area("Masukkan review aplikasi DANA:")

if st.button("Prediksi Sentimen"):
    if review.strip() == "":
        st.warning("Masukkan review terlebih dahulu.")
    else:
        review_bersih = clean_text(review)
        prediksi = model.predict([review_bersih])[0]

        st.subheader("Hasil Prediksi")
        st.write("Sentimen:", prediksi)

        st.subheader("Teks Setelah Preprocessing")
        st.write(review_bersih)
