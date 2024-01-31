import xml.etree.ElementTree as ET
import requests
import json
import zipfile
import pandas as pd
import matplotlib.pyplot as plt

#URL del CSV: https://www.ine.es/jaxiT3/files/t/csv_bdsc/2893.csv
response = requests.get('https://www.ine.es/jaxiT3/files/t/csv_bdsc/2893.csv')
if response.status_code == 200:
    with open("./2893.csv", 'wb') as f:
        f.write(response.content)

#Este código lee todo el fichero csv, lo pone como un único string y elimina los puntos de los miles para que los números se interpreten bien con pandas
#Luego escribe el nuevo contenido en el mismo fichero
text = open("./2893.csv", 'r')
text = ''.join([i for i in text])
text = text.replace('.','')
with open("./2893.csv", 'w') as f:
    f.writelines(text)

file_name = '2893.csv'
df = pd.read_csv(file_name, parse_dates=True, sep=';', encoding = "ISO-8859-1", decimal=',')
df.columns = ['Municipios','Sexo','Periodo','Personas']

#Muestro la cantidad de gente por cada municipio de cantabria (ambos sexos)
fig, ax = plt.subplots()
plt.bar(df.sort_values(by='Personas', ascending=0).Municipios[df['Periodo']==2023][df['Sexo']=='Total'].head(15),
        df.sort_values(by='Personas', ascending=0).Personas[df['Periodo']==2023][df['Sexo']=='Total'].head(15))
ax.xaxis.set_tick_params(rotation=90, labelsize=10)
plt.show()