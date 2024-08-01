tarifa_hora = int(input("Cuanto gana por hora?: "))
horas_trabajadas = int(input("Cuantas horas trabajo?: "))
total = tarifa_hora * horas_trabajadas
extra = (tarifa_hora * horas_trabajadas)/2

if horas_trabajadas > 40:
    total = total + extra
    print(f"Su salario total es de: {total}")
else:
    print(f"Su salario total es de: {total}")
print(extra)
