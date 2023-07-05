import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Trabajo/datos_nuevos.csv')

indice_salto = df[df['2022'] == 19].index[0]

df.loc[indice_salto+1:, '2022'] -= 1


indice_salto = df[df['2022'] == 49].index[0]

df.loc[indice_salto+1:, '2022'] -= 1


indice_salto = df[df['2022'] == 91].index[0]

df.loc[indice_salto+1:, '2022'] -= 1



df.to_csv('Trabajo/datos_nuevos.csv', index=False)