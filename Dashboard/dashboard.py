import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("all_df.csv")

# Title
st.title("Dashboard Analisis Data Pengguna Sepeda")

# Sidebar for Filters
st.sidebar.header("Filter Data")
selected_month = st.sidebar.selectbox("Pilih Bulan", df["month"].unique())
selected_hour = st.sidebar.slider("Pilih Jam", min_value=0, max_value=23, value=12)

df_filtered = df[(df["month"] == selected_month) & (df["hour"] == selected_hour)]

# Visualisasi Distribusi Pengguna Sepeda
st.subheader("Distribusi Jumlah Pengguna Sepeda")
fig, ax = plt.subplots()
sns.histplot(df_filtered["count"], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Visualisasi Tren Pengguna Sepeda
st.subheader("Tren Pengguna Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df, x="hour", y="count", hue="season", ax=ax)
st.pyplot(fig)


# Jumlah pengguna berdasarkan hari kerja dan hari libur
st.subheader("Jumlah Pengguna Sepeda pada Hari Kerja dan Hari Libur")
holiday_summary = df.groupby('holiday')['count'].sum().reset_index()
holiday_summary['weekday'] = holiday_summary['holiday'].map({0: 'Hari Kerja', 1: 'Hari Libur'})
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weekday', y='count', data=holiday_summary, palette='Blues', ax=ax)
st.pyplot(fig)

# Grafik jumlah pelanggan per bulan
st.subheader("Grafik Jumlah Pelanggan per Bulan")
monthly_counts = df.groupby('month')['count'].max()
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(monthly_counts.index, monthly_counts.values, c="#90CAF9", s=50, marker='o')
ax.plot(monthly_counts.index, monthly_counts.values)
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah')
ax.set_title('Grafik Jumlah Pelanggan per Bulan')
st.pyplot(fig)

# Pie chart perbandingan penyewa sepeda saat cuaca berkabut vs hujan deras
st.subheader("Perbandingan Penyewa Sepeda pada Cuaca Mist vs Heavy Rain")
weather_summary = df.groupby('weathersit')['count'].sum().reset_index()
weather_filtered = weather_summary[weather_summary['weathersit'].isin(['Mist', 'Heavy Rain'])]
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(weather_filtered['count'], labels=weather_filtered['weathersit'], autopct='%1.1f%%', startangle=90, colors=['#90CAF9', '#D3D3D3'])
ax.set_title("Perbandingan Penyewa Sepeda pada saat Mist vs Heavy Rain")
st.pyplot(fig)

# Grafik jumlah pengguna sepeda per musim
st.subheader("Grafik Jumlah Pengguna Sepeda per Musim")
fig, ax = plt.subplots(figsize=(10, 5))
colors = ["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3"]
sns.barplot(y="count", x="season", data=df.sort_values(by="season", ascending=False), palette=colors, ax=ax)
ax.set_title("Grafik Antar Musim")
st.pyplot(fig)
