# 🤟 Gesture Translation Hand (Indonesian Sign Language Translator)

Proyek ini adalah sistem penerjemah bahasa isyarat berbasis Python yang dapat mengenali gesture huruf (A–Z) menggunakan **MediaPipe** dan **model machine learning (LSTM atau Random Forest)**. Saat ini sistem baru mendukung **gesture satu tangan**.

## ✨ Fitur Utama

- 🔍 Deteksi gesture huruf A–Z dari satu tangan secara real-time (Belum capture semua Huruf/kata)
- 🧠 Menggunakan model Machine Learning (RandomForest `.pkl` dan kemungkinan akan dikembankan lagi menggunakan LSTM `.h5`)
- 🎥 Pemrosesan gambar real-time menggunakan MediaPipe
- 🔊 Konversi hasil deteksi menjadi suara Bahasa Indonesia menggunakan gTTS
- 📁 Struktur dataset per huruf untuk pelatihan model

## 🛠️ Instalasi

1. **Clone repositori**
   ```bash
   git clone https://github.com/Valzien/Gesture-Translation.git
   cd Gesture-Translation

Aktifkan virtual environment dan install dependensi

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Jalankan program utama
   ```bash
   python main.py
   ```

🚧 Roadmap Pengembangan
 Deteksi gesture satu tangan (A–Z)

 Dukungan dua tangan

 Gesture dinamis (misal: "halo")

 Interface pengguna berbasis GUI atau web

 Deteksi kata/kalimat dari urutan gesture

🤝 Kontribusi
Terbuka untuk kontribusi! Silakan buat pull request atau issue untuk diskusi fitur baru atau perbaikan bug.

📄 Lisensi
MIT License

🎯 Proyek ini bertujuan menjadi solusi teknologi untuk membantu komunikasi teman tuli melalui penerjemahan gesture tangan secara real-time.