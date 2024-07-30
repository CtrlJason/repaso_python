alimentacion = int(input("Cuanto gasta en alimentación: "))
transporte = int(input("Cuanto gasta en trasporte: "+"$"))
entretenimiento = int(input("Cuanto gasta en entretenimiento: "))
otros = int(input("Cuanto gasta en otros: "))
total = alimentacion+transporte+entretenimiento+otros
print(f"Su total de gastos de este mes es de: {total}$")
