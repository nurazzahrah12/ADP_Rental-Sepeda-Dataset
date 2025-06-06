# Proyek Analisis Data: Bike Sharing Dataset

---

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan dataset **Bike Sharing**. Fokus analisis meliputi pengaruh faktor-faktor seperti hari, jam, suhu, kelembaban, dan cuaca terhadap jumlah penyewaan sepeda. Hasil analisis disajikan dalam bentuk **dashboard interaktif** menggunakan **Streamlit**.

---

## Dataset yang Digunakan

1. **day.csv**
   - Data agregat harian penyewaan sepeda
   - Kolom penting: `dteday`, `weekday`, `temp`, `hum`, `cnt`

2. **hour.csv**
   - Data penyewaan per jam
   - Kolom penting: `dteday`, `hr`, `temp`, `hum`, `cnt`

---

## Cara Menjalankan Dashboard

1. Buka terminal atau command prompt
2. Arahkan ke folder proyek:
   ```bash
   cd submission/dashboard
   ```
3. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard.py
   ```
4. Akses dashboard di browser lokal Anda

*Dashboard juga dideploy ke Streamlit Cloud dan tautannya disimpan di file `url.txt`.*

---

## Hasil Analisis

### 1. Eksplorasi & Pembersihan Data
- Memeriksa missing values dan konsistensi data
- Transformasi kolom waktu dan cuaca

### 2. Analisis Pola Mingguan
- Apakah jumlah penyewaan lebih tinggi di hari kerja?
- Visualisasi: **Box plot** weekday vs weekend

### 3. Analisis Pengaruh Suhu
- Hubungan antara suhu dan jumlah peminjaman
- Visualisasi: **Scatter plot**

### 4. Visualisasi Interaktif
- Dibuat dengan Matplotlib, Seaborn, dan Streamlit
- Pengguna dapat eksplorasi tren data secara mandiri

---

## Umpan Balik Reviewer (Intisari)

**Catatan penting:**
- Dokumentasi markdown di notebook sangat baik.
- Dashboard berhasil dideploy dan mudah dipahami.

**Saran pengembangan:**
- Coba tambahkan analisis lanjutan seperti:
  - **RFM Analysis** (Recency, Frequency, Monetary)
  - **Geoanalysis** menggunakan `folium` atau `matplotlib`
  - **Clustering manual** (grouping/binned analysis)
- Analisis lanjutan bisa memperkaya wawasan tanpa harus pakai machine learning.

---

## Kesimpulan

Analisis ini memberikan wawasan tentang tren penyewaan sepeda berdasarkan waktu dan cuaca. Dashboard interaktif memungkinkan pengguna untuk mengeksplorasi data dengan fleksibel. Proyek ini merupakan landasan kuat untuk masuk ke proyek machine learning di tahap berikutnya.
