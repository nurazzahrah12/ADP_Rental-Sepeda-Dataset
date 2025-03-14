# Proyek Analisis Data: **Bike Sharing Dataset**  
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan dataset **Bike Sharing**. Analisis ini akan mengeksplorasi faktor-faktor yang memengaruhi jumlah peminjaman sepeda serta menyajikan hasilnya dalam bentuk dashboard interaktif menggunakan **Streamlit**.  

## **Dataset yang Digunakan**  
Dataset yang digunakan dalam proyek ini berisi informasi mengenai jumlah peminjaman sepeda berdasarkan faktor-faktor seperti hari, jam, suhu, kelembaban, dan kondisi cuaca. Dataset yang digunakan meliputi:  

1. **day.csv**  
   - Berisi data agregasi harian terkait jumlah penyewaan sepeda  
   - Kolom utama: `dteday` (tanggal), `weekday` (hari dalam seminggu), `temp` (suhu), `hum` (kelembaban), `cnt` (total penyewaan)  

2. **hour.csv**  
   - Berisi data penyewaan sepeda per jam  
   - Kolom utama: `dteday` (tanggal), `hr` (jam), `temp` (suhu), `hum` (kelembaban), `cnt` (total penyewaan)  

## **Cara Menjalankan Dashboard**  
Untuk menjalankan dashboard interaktif yang dibuat menggunakan **Streamlit**, ikuti langkah-langkah berikut:  

1. **Buka terminal atau command prompt**  
2. **Navigasikan ke folder proyek**  
   ```bash
   cd submission/dashboard
   ```
3. **Jalankan aplikasi Streamlit**  
   ```bash
   streamlit run dashboard.py
   ```
4. **Dashboard akan terbuka secara otomatis di browser**  

## **Hasil Analisis & Temuan Utama**  
Dalam proyek ini, dilakukan beberapa analisis utama untuk memahami pola penggunaan sepeda berdasarkan dataset yang tersedia. Analisis yang dilakukan meliputi:  

### **1. Eksplorasi Data & Pembersihan Data**  
   - Memeriksa dataset untuk melihat missing values dan inkonsistensi  
   - Melakukan transformasi data agar lebih siap untuk dianalisis  

### **2. Analisis Pola Mingguan**  
   - **Pertanyaan**: Apakah jumlah pengguna lebih banyak di hari kerja dibandingkan akhir pekan?  
   - **Metode**: Menggunakan visualisasi perbandingan jumlah penyewaan sepeda antara weekday vs weekend dalam bentuk **box plot**  
   - **Hasil**: [Diisi dengan insight dari data]  

### **3. Analisis Pengaruh Suhu terhadap Peminjaman Sepeda**  
   - **Pertanyaan**: Bagaimana pengaruh suhu terhadap jumlah peminjaman sepeda?  
   - **Metode**: Menggunakan **scatter plot** untuk melihat hubungan antara suhu dan jumlah penyewaan sepeda  
   - **Hasil**: [Diisi dengan insight dari data]  

### **4. Visualisasi Data Interaktif**  
   - Data disajikan dalam bentuk grafik dan dashboard interaktif menggunakan **Matplotlib**, **Seaborn**, dan **Streamlit**  
   - Dashboard memungkinkan pengguna untuk mengeksplorasi tren penggunaan sepeda berdasarkan berbagai faktor  

## **Kesimpulan & Manfaat Analisis**  
Proyek ini memberikan wawasan tentang faktor-faktor yang memengaruhi penggunaan sepeda, termasuk pola mingguan dan pengaruh suhu. Wawasan ini dapat membantu pengelola sistem penyewaan sepeda dalam:  
✅ Mengoptimalkan jumlah sepeda yang tersedia pada hari dan jam tertentu  
✅ Mengantisipasi permintaan sepeda berdasarkan perubahan cuaca  
✅ Meningkatkan pengalaman pengguna dengan memahami pola peminjaman sepeda  
