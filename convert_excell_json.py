import pandas as pd

df = pd.read_excel('LIST BAHAN KIMIA ORGANIK LPK.xlsx')
df.to_json('LIST BAHAN KIMIA ORGANIK LPK.json', orient='records', force_ascii=False, indent=2)

