import pandas as pd

# Baca file Excel
df = pd.read_excel('LIST BAHAN KIMIA ORGANIK LPK.xlsx')

# Tampilkan semua data
print("=== Daftar Bahan Kimia dan Tingkat Bahaya ===")
print(df)

# Filter bahan dengan bahaya tinggi
berbahaya = df[df['Bahaya'] == 'Tinggi']

print("\n⚠ Bahan Kimia Berbahaya Tinggi:")
print(berbahaya)
