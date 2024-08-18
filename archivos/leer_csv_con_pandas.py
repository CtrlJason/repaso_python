import pandas as pd
df = pd.read_csv("archivos\\datos.csv")
# print(df["Edad"]) #Se utilizan los corchetes pasa saber que datos hay en una columna especifica
print(df)
datos_ordenados = df.sort_values("Edad") #Usamos sort_values para organizar datos por el parametro
print(datos_ordenados)