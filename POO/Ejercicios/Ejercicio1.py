#Variables
ruta = "C:/Dev_Jason/repaso_python/POO/Ejercicios/estudiantes_registrados.txt"

# Contructor para almacenar los datos
class Estudiante(): # Este metodo constructor me verifica si el estudiante se ha regristrado
    def __init__(self, nombre, apellido , edad, semestre):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.semestre = semestre
        
    def estudiar(self):
        print(f"\nEl estudiante {self.nombre} {self.apellido} con la edad de {self.edad} años se encuentra cursando: {self.semestre} Semestre - INTER\n(+) Se ha registrado exisosamente")
        # Guardado de los registros en un archivo TXT
        with open(ruta,"a",encoding="UTF-8") as arch_studens: # Se debe poner , "w" para que se cree y escriba el archivo
            # arch_studens.writelines("<-------------------------------------->\n") 
            # writelines se usa para crear o escribir lineas de texto
            arch_studens.writelines(f"Estudiante: {self.nombre} {self.apellido}\n Edad: {self.edad} Años\n Semestre: {self.semestre}\n<-------------------------------------->\n")
    
# Funcion para extraer los datos del usuario
def programa_inscripcion_datos():
    user_name = input("Escribe tu nombre: ")
    user_last_name = input("Escribe tu apellido: ")
    user_eye = input("Escribe tu edad: ")
    user_year = input("Que grado cursas actualmente: ")
    user = Estudiante(user_name, user_last_name, user_eye, user_year)
    user.estudiar()

# Creacion del archivo TXT en caso de que no exista
try: # try realiza una verificacion y si esta no se cumple pasa a la excepcion
    with open(ruta, "r"):
        pass
except FileNotFoundError: # en caso de que el programa llegue a except para que no se bloquee se agregan argumentos con el error en cuestion y asi el programa pueda continuar
    with open(ruta, "w") as arch_studens:
        arch_studens.writelines("Estudiantes registrados en INTER:\n<-------------------------------------->\n")

# Bucle para preguntar al usuario o usuarios que se van a registrar
while True:
    user_inicio = int(input("Desea iniciar el programa de inscripcion? \n1. Si \n2. No \n : "))
    if user_inicio == 1:
        programa_inscripcion_datos()
    elif user_inicio == 2:
        print("\nPrograma de inscripcion finalizado")
        break
    else:
        print("\nOpcion no valida\n")
        
