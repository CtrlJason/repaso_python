fecha = {
    "dd": 15,
    "mm": 3,
    "aaaa": 2001
}

dia = (input("Cual es la fecha del dia de hoy? escribe el dia en numeros: "))
mes = (input("Escribe el mes en numeros: "))
año = (input("Escribe el año en numeros: "))

fecha_user = {
    "dd": dia,
    "mm": mes,
    "aaaa": año
}

fecha.update(fecha_user)

print(f"Usted puso la fecha {fecha["dd"]}/{fecha["mm"]}/{fecha["aaaa"]}")
