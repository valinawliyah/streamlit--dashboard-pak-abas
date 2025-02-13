import streamlit as st
import pandas as pd
import plotly.express as px

max_upload_size = 500

def filter_data(layanan_df):
    # Ubah alamat di kedua dataframe menjadi huruf kecil
    layanan_df['alamat'] = layanan_df[' Kota Domisili Konsumen '].str.lower()
    
    konflik_data = layanan_df[layanan_df['alamat'] == 'kota surabaya']
    return konflik_data

st.title("Dashboard Layanan Konsumen")

layanan_file = st.file_uploader("Upload file CSV Layanan Konsumen", type=["csv"])

if layanan_file:
    layanan_df = pd.read_csv(layanan_file)

    konflik_data = filter_data(layanan_df)

    st.write("Data Layanan dengan Konflik di Bank Surabaya:")
    st.dataframe(konflik_data)

    if not konflik_data.empty:
        # Sesuaikan 'kolom_yang_ditampilkan' dengan kolom yang ingin Anda tampilkan pada histogram
        fig = px.histogram(konflik_data, x="kolom_yang_ditampilkan", title="Distribusi Layanan dengan Konflik")
        st.plotly_chart(fig)
