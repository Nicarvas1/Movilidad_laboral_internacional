import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Trabajo/datos_nuevos.csv')

df = df.drop('Country', axis=1)
df = df.drop('2022', axis=1)
df = df.drop('City', axis=1)

df.to_csv('Trabajo/correlacion.csv', index=False)

df = pd.read_csv('Trabajo/correlacion.csv')

plt.figure(figsize = (15,8))
sns.heatmap(df.corr(),annot=True, cbar=True, cmap='Blues', fmt='.1f')
plt.show()