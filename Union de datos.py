#Importamos las librerias
import numpy as np 
import pandas as pd

#Definimos nombres para los archivos
datos_balance = pd.read_csv('Trabajo/Cities with the Best Work-Life Balance 2022.csv')
datos_coste = pd.read_csv('Trabajo/costofliving.csv')

#Separamos pais y ciuidad en datos_coste
datos_coste[['City_','Country','Country2']] = datos_coste.City.str.split(", ",expand=True,n=2)
print(datos_coste.Country.unique())

#Reemplazamos los estados por USA
datos_coste['Country']= datos_coste['Country'].str.strip()
mask = datos_coste['Country'].str.len() < 4
datos_coste['Country'] = np.where(mask, 'United States', datos_coste['Country'])
datos_coste['Country'] = datos_coste['Country'].str.replace('[^a-zA-Z0-9]', ' ', regex=True).str.strip()
print(datos_coste.Country.unique())


#Renombramos columnas
datos_coste = datos_coste.rename(columns={'City' : 'City and Country',
                                          'City_' : 'City',
                                          'Country_x' : 'Country'})

print(datos_coste.columns)

#Unimos bases de datos en funnción de la columna Ciudad
datos_unidos = pd.merge(datos_balance,datos_coste,on='City')

#Verificamos unión y pasamos a un nuevo archivo csv
print(datos_unidos)
datos_unidos.to_csv('Trabajo/datos_unidos.csv', index=False)



