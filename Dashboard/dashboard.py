# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load Data
# day_df = pd.read_csv("D:\DBS\Submission\Dashboard\hour_df_clean.csv") 

# # Konversi kolom tanggal ke datetime
# day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# # Title Dashboard
# st.title("📊 Dashboard Analisis Peminjaman Sepeda 🚲")

# # Sidebar Filter
# st.sidebar.header("Filter Data")
# season = st.sidebar.selectbox("Pilih Musim", ["Semua", "Spring", "Summer", "Fall", "Winter"])
# if season != "Semua":
#     season_map = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
#     day_df = day_df[day_df["season"] == season_map[season]]

# # **1️⃣ Visualisasi Jumlah Peminjaman Sepeda Harian**
# st.subheader("📅 Tren Peminjaman Sepeda Harian")
# plt.figure(figsize=(10, 5))
# sns.lineplot(data=day_df, x="dteday", y="cnt", marker="o")
# plt.xticks(rotation=45)
# plt.xlabel("Tanggal")
# plt.ylabel("Jumlah Peminjaman")
# plt.grid(True)
# st.pyplot(plt)

# # **2️⃣ Perbandingan Peminjaman antara Hari Kerja dan Akhir Pekan**
# st.subheader("🏢🚲 Perbandingan Hari Kerja vs Akhir Pekan")
# plt.figure(figsize=(6, 4))
# sns.boxplot(x=day_df["workingday"], y=day_df["cnt"])
# plt.xticks([0, 1], ["Akhir Pekan", "Hari Kerja"])
# plt.xlabel("Tipe Hari")
# plt.ylabel("Jumlah Peminjaman")
# st.pyplot(plt)

# # **3️⃣ Pengaruh Suhu terhadap Peminjaman**
# st.subheader("🌡️ Pengaruh Suhu terhadap Jumlah Peminjaman")
# plt.figure(figsize=(8, 5))
# sns.scatterplot(data=day_df, x="temp", y="cnt", alpha=0.5)
# plt.xlabel("Suhu Normalisasi")
# plt.ylabel("Jumlah Peminjaman")
# plt.grid(True)
# st.pyplot(plt)

# st.write("**Kesimpulan:** Dari visualisasi di atas, kita dapat melihat tren peminjaman sepeda berdasarkan waktu, hari kerja vs akhir pekan, serta pengaruh suhu terhadap jumlah peminjaman.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("day_df_clean.csv")
hour_df = pd.read_csv("hour_df_clean.csv")

# Konversi kolom tanggal ke datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Sidebar Navigation
st.sidebar.title("Navigasi Dashboard")
page = st.sidebar.radio("Pilih Tampilan", ["Daily Analysis", "Hourly Analysis"])

st.title("📊 Dashboard Analisis Peminjaman Sepeda 🚲")

if page == "Daily Analysis":
    st.subheader("📅 Tren Peminjaman Sepeda Harian")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=day_df, x="dteday", y="cnt", marker="o")
    plt.xticks(rotation=45)
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Peminjaman")
    plt.grid(True)
    st.pyplot(plt)

elif page == "Hourly Analysis":
    st.subheader("⏳ Tren Peminjaman Sepeda Per Jam")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hour_df, x="hr", y="cnt", marker="o", ci=None)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Peminjaman")
    plt.grid(True)
    st.pyplot(plt)

# Sidebar Filter
st.sidebar.header("Filter Data")
season = st.sidebar.selectbox("Pilih Musim", ["Semua", "Spring", "Summer", "Fall", "Winter"])
if season != "Semua":
    season_map = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
    day_df = day_df[day_df["season"] == season_map[season]]

# **1️⃣ Visualisasi Jumlah Peminjaman Sepeda Harian**
st.subheader("📅 Tren Peminjaman Sepeda Harian")
plt.figure(figsize=(10, 5))
sns.lineplot(data=day_df, x="dteday", y="cnt", marker="o")
plt.xticks(rotation=45)
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Peminjaman")
plt.grid(True)
st.pyplot(plt)

# **2️⃣ Perbandingan Peminjaman antara Hari Kerja dan Akhir Pekan**
st.subheader("🏢🚲 Perbandingan Hari Kerja vs Akhir Pekan")
plt.figure(figsize=(6, 4))
sns.boxplot(x=day_df["workingday"], y=day_df["cnt"])
plt.xticks([0, 1], ["Akhir Pekan", "Hari Kerja"])
plt.xlabel("Tipe Hari")
plt.ylabel("Jumlah Peminjaman")
st.pyplot(plt)

# **3️⃣ Pengaruh Suhu terhadap Peminjaman**
st.subheader("🌡️ Pengaruh Suhu terhadap Jumlah Peminjaman")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=day_df, x="temp", y="cnt", alpha=0.5)
plt.xlabel("Suhu Normalisasi")
plt.ylabel("Jumlah Peminjaman")
plt.grid(True)
st.pyplot(plt)

st.write("**Kesimpulan:** Dari visualisasi di atas, kita dapat melihat tren peminjaman sepeda berdasarkan waktu, hari kerja vs akhir pekan, serta pengaruh suhu terhadap jumlah peminjaman.")
