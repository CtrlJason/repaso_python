materias = ["Matematicas", "Fisica", "Historia", "Lengua"]
repetir_materia = []

nota_mate = float(input("Escriba cuanto se saco en Matematicas: "))
nota_fisi = float(input("Escriba cuanto se saco en Fisica: "))
nota_his = float(input("Escriba cuanto se saco en Historia: "))
nota_len = float(input("Escriba cuanto se saco en Lengua: "))

if nota_mate < 3:
    repetir_materia.append(materias[0])
if nota_fisi < 3:
    repetir_materia.append(materias[1])
if nota_his < 3:
    repetir_materia.append(materias[2])
if nota_len < 3:
    repetir_materia.append(materias[3])

print(f"Las materias que debe repetir son: {repetir_materia}")
