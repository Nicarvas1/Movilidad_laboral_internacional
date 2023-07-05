import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Trabajo/datos_nuevos.csv')



# Ordenar el DataFrame por la columna 'Overworked Population' de menor a mayor
df_ordenado = df.sort_values('Overworked Population',ascending=True)

# Obtener las ciudades y la sobrecarga de trabajo ordenada
cities = df_ordenado['City']
sobrecarga_trabajo = df_ordenado['Overworked Population']

# Crear el gráfico de barras
plt.figure(figsize=(12, 6)) 
plt.bar(cities, sobrecarga_trabajo)
plt.xticks(rotation=90)  
plt.xlabel("Ciudad")
plt.ylabel("Poblacion sobrecargada de trabajo")
plt.title("Sobrecarga de trabajo por ciudad")
plt.tight_layout() 
plt.show()




# Ordenar el DataFrame por la columna 'Minimum Vacations Offered (Days)' de menor a mayor
df_ordenado = df.sort_values('Minimum Vacations Offered (Days)', ascending=True)
cities = df_ordenado['City']
minimo_vacaiones = df_ordenado['Minimum Vacations Offered (Days)']

plt.figure(figsize=(12, 6)) 
plt.bar(cities, minimo_vacaiones)
plt.xticks(rotation=90)  
plt.xlabel("Ciudad")
plt.ylabel("Minimo de vacaciones ofrecidas (dias)")
plt.title("Dias de vacaciones ofrecidos por ciudad")
plt.tight_layout() 
plt.show()




# Ordenar el dataframe por la columna 'Vacations Taken (Days)' de menor a mayor
df['Vacations Taken (Days)'] = pd.to_numeric(df['Vacations Taken (Days)'], errors='coerce')
df_ordenado = df.sort_values('Vacations Taken (Days)', ascending=True)

# Extraer los datos ordenados
cities = df_ordenado['City']
vacaciones_tomadas = df_ordenado['Vacations Taken (Days)']

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(cities, vacaciones_tomadas)
plt.xticks(rotation=90)
plt.xlabel("Ciudad")
plt.ylabel("Dias de vacaciones tomados")
plt.title("Días de vacaciones tomados por ciudad")
plt.tight_layout()
plt.show()

# Ordenar el DataFrame por la columna 'Unemployment' de menor a mayor
df_ordenado = df.sort_values('Unemployment',ascending=True)
cities = df_ordenado['City']
desempleo = df_ordenado['Unemployment']

plt.figure(figsize=(12, 6)) 
plt.bar(cities, desempleo)
plt.xticks(rotation=90)  
plt.xlabel("Ciudad")
plt.ylabel("Empleabilidad")
plt.title("Empleabilidad por ciudad")
plt.tight_layout() 
plt.show()


# Ordenar el DataFrame por la columna 'Healthcare' de menor a mayor
df_ordenado = df.sort_values('Healthcare',ascending=True)
cities = df_ordenado['City']
salud = df_ordenado['Healthcare']

plt.figure(figsize=(12, 6)) 
plt.bar(cities, salud)
plt.xticks(rotation=90)  
plt.xlabel("Ciudad")
plt.ylabel("Acceso a salud")
plt.title("Acceso a salud por ciudad")
plt.tight_layout() 
plt.show()


# Ordenar el DataFrame por la columna 'Air Quality' de menor a mayor
df_ordenado = df.sort_values('Air Quality',ascending=True)
cities = df_ordenado['City']
calidad_aire = df_ordenado['Air Quality']

plt.figure(figsize=(12, 6)) 
plt.bar(cities, calidad_aire)
plt.xticks(rotation=90)  
plt.xlabel("Ciudad")
plt.ylabel("Calidad de aire")
plt.title("Calidad de aire por ciudad")
plt.tight_layout() 
plt.show()


# Ordenar el DataFrame por la columna 'Cost of Living Index' de menor a mayor
df_ordenado = df.sort_values('Cost of Living Index',ascending=True)
cities = df_ordenado['City']
costo_de_vida = df_ordenado["Cost of Living Index"]

plt.figure(figsize=(12, 6)) 
plt.bar(cities, costo_de_vida)
plt.xticks(rotation=90)  
plt.xlabel("Ciudad")
plt.ylabel("Costo de vida")
plt.title("Costo de vida por Ciudad")
plt.tight_layout() 
plt.show()



