import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leer el dataframe
df = pd.read_csv('Trabajo/datos_nuevos.csv')


#Relacion poblacion sobrecargada de trabajo y costo de vida

# Crear el gráfico de dispersión con regresión
sns.regplot(x='Overworked Population', y='Cost of Living Index', data=df, scatter=True)
plt.xlabel('Poblacion sobrecargada de trabajo')
plt.ylabel('Costo de vida')
plt.title('Gráfico de dispersión con regresión - Poblacion sobrecargada de trabajo - Costo de vida')
plt.show()

#Correlacion entre variables
correlation = df['Overworked Population'].corr(df['Cost of Living Index'])
print(f"Correlation entre poblacion sobrecargada y costo de vida: {correlation}")

#Grafico de lineas
df_ordenado = df.sort_values('Overworked Population',ascending=True)
plt.plot(df_ordenado['Overworked Population'], df_ordenado['Cost of Living Index'])
plt.xlabel('Poblacion sobrecargada de trabajo')
plt.ylabel('Costo de vida')
plt.title('Gráfico de Líneas - Poblacion sobrecargada de trabajo - Costo de vida')
plt.show()




#Relacion minimo de vacaciones ofrecidas (dias) y costo de vida

# Crear el gráfico de dispersión con regresión
sns.regplot(x='Minimum Vacations Offered (Days)', y='Cost of Living Index', data=df, scatter=True)
plt.xlabel('Minimo de dias de vacaciones ofrecidos')
plt.ylabel('Costo de vida')
plt.title('Gráfico de dispersión con regresión - Dias de vacaciones ofrecidos - Costo de vida')
plt.show()

#Correlacion entre variables
correlation = df['Minimum Vacations Offered (Days)'].corr(df['Cost of Living Index'])
print(f"Correlation vacaciones ofrecidas y costo de vida: {correlation}")

#Crear grafico de lineas
df_ordenado = df.sort_values('Minimum Vacations Offered (Days)',ascending=True)
plt.plot(df_ordenado['Minimum Vacations Offered (Days)'], df_ordenado['Cost of Living Index'])
plt.xlabel('Minimo de dias de vacaciones ofrecidos')
plt.ylabel('Costo de vida')
plt.title('Gráfico de Líneas - Dias de vacaciones ofrecidos - Costo de vida')
plt.show()

#Relacion costo de vida y dias de vacaciones tomados
# Crear el gráfico de dispersión con regresión
sns.regplot(x='Vacations Taken (Days)', y='Cost of Living Index', data=df, scatter=True)
plt.xlabel('Cantidad de dias de vacaciones tomados')
plt.ylabel('Cost of Living Index')
plt.title('Gráfico de dispersión con regresión - Dias de vacaciones tomados - Costo de vida')
plt.show()

#Correlacion entre variables
correlation = df['Vacations Taken (Days)'].corr(df['Cost of Living Index'])
print(f"Correlation entre dias tomados y costo de vida: {correlation}")

#Crear grafico de lineas
df_ordenado = df.sort_values('Vacations Taken (Days)',ascending=True)
plt.plot(df_ordenado['Vacations Taken (Days)'], df_ordenado['Cost of Living Index'])
plt.xlabel('Dias de vacaciones tomados')
plt.ylabel('Costo de vida')
plt.title('Gráfico de Líneas - Dias de vacaciones tomados - Costo de vida')
plt.show()


#Relacion costo de vida y empleabilidad
## Crear el gráfico de dispersión con regresión
sns.regplot(x='Unemployment', y='Cost of Living Index', data=df, scatter=True)
plt.xlabel('Empleabilidad')
plt.ylabel('Costo de vida')
plt.title('Gráfico de dispersión con regresión - Empleabilidad - Costo de vida')
plt.show()

#Correlacion entre variables
correlation = df['Unemployment'].corr(df['Cost of Living Index'])
print(f"Correlation entre empleabilidad y costo de vida: {correlation}")

#Crear grafico de lineas
df_ordenado = df.sort_values('Unemployment',ascending=True)
plt.plot(df_ordenado['Unemployment'], df_ordenado['Cost of Living Index'])
plt.xlabel('Empleabilidad')
plt.ylabel('Costo de vida')
plt.title('Gráfico de Líneas - Empleabilidad - Costo de vida')
plt.show()

#Costo de vida y acceso atencion medica
# Crear el gráfico de dispersión con regresión
sns.regplot(x='Healthcare', y='Cost of Living Index', data=df, scatter=True)
plt.xlabel('Acceso a salud')
plt.ylabel('Costo de vida')
plt.title('Gráfico de dispersión con regresión - Acceso a salud - Costo de vida')
plt.show()


#Correlacion entre varuables
correlation = df['Healthcare'].corr(df['Cost of Living Index'])
print(f"Correlation entre acceso a salud y costo de vida: {correlation}")

#Crear grafico de lineas
df_ordenado = df.sort_values('Healthcare',ascending=True)
plt.plot(df_ordenado['Healthcare'], df_ordenado['Cost of Living Index'])
plt.xlabel('Acceso a salud')
plt.ylabel('Costo de vida')
plt.title('Gráfico de Líneas - Acceso a salud - Costo de vida')
plt.show()

#Costo de vida y calidad de aire
# Crear el gráfico de dispersión con regresión
sns.regplot(x='Air Quality', y='Cost of Living Index', data=df, scatter=True)
plt.xlabel('Calidad del aire')
plt.ylabel('Costo de vida')
plt.title('Gráfico de dispersión con regresión - Calidad de aire - Costo de vida')
plt.show()

#Correlacion entre variables
correlation = df['Air Quality'].corr(df['Cost of Living Index'])
print(f"Correlation entre calidad de aire y costo de vida: {correlation}")

#Crear grafico de lineas
df_ordenado = df.sort_values('Air Quality',ascending=True)
plt.plot(df_ordenado['Air Quality'], df_ordenado['Cost of Living Index'])
plt.xlabel('Calidad de aire')
plt.ylabel('Costo de vida')
plt.title('Gráfico de Líneas - Calidad de aire - Costo de vida')
plt.show()

