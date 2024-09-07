def decorador(funcion): # La funcion que se quiera decorar se almacena en (funcion)
    def funcion_modificada(): # Se crea una funcion modificadora
        print("Antes de llamar a la funcion") # Primer decorador
        funcion() # Se llama a la funcion que queremos decorar
        print("Despues de llamar a la funcion") # Segundo decorador
    return funcion_modificada

# def saludo(): # Creamos la funcion que queremos decorar
#     print("Hola Jason") # Lo que se ejecuta en el decorador
    
# def despedida():
#     print("Hasta pronto Jason")
# saludo_modificado = decorador(saludo) # Almacenamos la funcion decoradora con el parametro de la funcion que queremos decorar en una variable que se transforma en una funcion
# saludo_modificado() # Se llama a la funcion decoradora, esta ya tendra el parametro de la funcion que queremos decorar
# desdepedia_modificada = decorador(despedida) # Nota: se puede llamar a la funcion sin almacenarla en una variable usando: funcion(parametro)() <-- Esto seria la llamada de la funcion.
# desdepedia_modificada() 
# El codigo anterior es una forma pero existe otra mas optima de hacerlo

@decorador # Esto llama directamente a la funcion decorador y le asigna el parametro despues del "@decorador"
def saludo():
    print("Hola Jason")
    
@decorador    
def despedida():
    print("Hasta pronto Jason")
    
saludo()
despedida()