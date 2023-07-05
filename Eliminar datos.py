import numpy as np 
import pandas as pd


#Leer el data frame
df = pd.read_csv('Trabajo/datos_unidos.csv')

#Eliminar las tablas que no usaremos
df = df.drop('Country2', axis=1)
df = df.drop('City and Country', axis=1)
df = df.drop('2021', axis=1)
df = df.drop('Remote Jobs', axis=1)
df = df.drop('Multiple Jobholders', axis=1)
df = df.drop('Access to Mental Healthcare', axis=1)
df = df.drop('Inclusivity & Tolerance', axis=1)
df = df.drop('Affordability', axis=1)
df = df.drop('Happiness, Culture & Leisure', axis=1)
df = df.drop('City Safety', axis=1)
df = df.drop('Outdoor Spaces', axis=1)
df = df.drop('Wellness and Fitness', axis=1)
df = df.drop('TOTAL SCORE', axis=1)
df = df.drop('Inflation', axis=1)
df = df.drop('Paid Parental Leave (Days)', axis=1)
df = df.drop('Covid Impact', axis=1)
df = df.drop('Covid Support', axis=1)
df = df.drop('Groceries Index', axis=1)
df = df.drop('Restaurant Price Index', axis=1)
df = df.drop('Rank', axis=1)
df = df.drop('Rent Index', axis=1)
df = df.drop('Cost of Living Plus Rent Index',axis=1)
df = df.drop('Local Purchasing Power Index', axis=1)
df = df.drop('Country_y', axis=1)

#Pasar las columnas de tipo object a numero
df['Overworked Population'] = pd.to_numeric(df['Overworked Population'].str.rstrip('%'), errors='coerce')
df['Vacations Taken (Days)'] = pd.to_numeric(df['Vacations Taken (Days)'], errors='coerce')

#Renombrar la columna country_x a country
df.rename(columns={'Country_x': 'Country'}, inplace=True)

#Guardar todo en el csv
df.to_csv('Trabajo/datos_nuevos.csv', index=False)

df = pd.read_csv('Trabajo/datos_nuevos.csv')
print(df.dtypes)


df = pd.read_csv('Trabajo/datos_nuevos.csv')


# Filas a eliminar
filas_a_eliminar = [16]

# Eliminar las filas
df = df.drop(filas_a_eliminar)


df.to_csv('Trabajo/datos_nuevos.csv', index=False)

# Filas a eliminar
filas_a_eliminar = [27]

# Eliminar las filas
df = df.drop(filas_a_eliminar)


df.to_csv('Trabajo/datos_nuevos.csv', index=False)



# Filas a eliminar
filas_a_eliminar = [50]


# Eliminar las filas
df = df.drop(filas_a_eliminar)


df.to_csv('Trabajo/datos_nuevos.csv', index=False)



# Filas a eliminar
filas_a_eliminar = [98]


# Eliminar las filas
df = df.drop(filas_a_eliminar)


df.to_csv('Trabajo/datos_nuevos.csv', index=False)


# Filas a eliminar
filas_a_eliminar = [92]


# Eliminar las filas
df = df.drop(filas_a_eliminar)


df.to_csv('Trabajo/datos_nuevos.csv', index=False)

num_filas = df.shape[0]

print("Número de filas:", num_filas)
