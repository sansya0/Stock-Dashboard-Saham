import streamlit as st
import yfinance as yf
import pandas as pd
#1. Judul dan Deskripsi
st.write("""
# 📈 Dashboard Harga Saham Sederhana
Aplikasi ini menampilkan harga penutupan (**Closing Price**) dan volume saham!
""")
#2. Sidebar untuk Input User
st.sidebar.header('Input Pengguna')
#Input Kode Saham
ticker_symbol = st.sidebar.text_input("Masukkan Kode Saham (Contoh: AAPL, BBCA.JK, TLKM.JK)", "GOOGL")
#Input Rentang Waktu
start_date = st.sidebar.date_input("Tanggal Mulai", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("Tanggal Akhir", pd.to_datetime("today"))
#3. Ambil Data dari Yahoo Finance
try:
  st.write(f"Sedang mengambil data: **{ticker_symbol}**...")

  ticker_df = yf.download(ticker_symbol, start=start_date, end=end_date)

  if ticker_df.empty:
    st.error(f"❌ Data kosong! Pastikan kode '{ticker_symbol}' benar. (Cek di finance.yahoo.com)")
  else:
    st.success("✅ Data ditemukan!")

    #4. Tampilkan Grafik
    st.write(f"### Pergerakan Harga Penutupan - {ticker_symbol}")
    st.line_chart(ticker_df['Close']) #Plot harga Close

    st.write(f"## Volume Transaksi - {ticker_symbol}")
    st.bar_chart(ticker_df['Volume']) #Plot Volume

    #5. Tampilkan Tabel Data
    if st.checkbox("Tampilkan Data Mentah"):
      st.write(ticker_df)

except Exception as e:
    st.error(f"Terjadi kesalahan. Pastikan kode saham benar.")
    st.code(e)
