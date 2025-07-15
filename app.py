import streamlit as st
import pandas as pd

st.title("📊 Analisis Bahan Kimia dari Excel")

uploaded_file = st.file_uploader("Upload file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("File berhasil dibaca ✅")

        st.subheader("📋 Semua Data:")
        st.dataframe(df)

        st.subheader("⚠ Bahan Kimia Berbahaya Tinggi:")
        bahaya_tinggi = df[df['Bahaya'].str.lower() == 'tinggi']
        st.dataframe(bahaya_tinggi)

    except Exception as e:
        st.error(f"Gagal membaca file: {e}")
else:
    st.info("Silakan upload file Excel dengan kolom: Bahan Kimia, Rumus, Bahaya.")
