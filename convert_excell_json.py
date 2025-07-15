import pandas as pd

# Baca file Excel
df = pd.read_excel('LIST BAHAN KIMIA ORGANIK LPK.xlsx')

# Konversi ke JSON
df.to_json('LIST BAHAN KIMIA ORGANIK LPK.json', orient='records', force_ascii=False, indent=2)

print("Konversi selesai! File JSON disimpan.")

