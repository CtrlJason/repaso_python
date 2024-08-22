import winsound
from pathlib import Path

# Se utiliza Path para trabajar con ubicaciones absolutas y relativas, en este caso relativas
ruta_archivo = Path(__file__).parent/"estudiantes_registrados.txt" # En este caso se utiliza Path(__file__).parent/ para obtener la ubicacion de un archivo y viajar entre carpetas atravez de un "/"

#Variables
ruta_sonido_registro = "C:/Windows/Media/chimes.wav"
ruta_sonido_cierre = "C:/Windows/Media/Windows Notify System Generic.wav"

# Contructor para almacenar los datos
class Estudiante(): # Este metodo constructor me verifica si el estudiante se ha regristrado
    def __init__(self, nombre, apellido , edad, semestre):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.semestre = semestre
        
    def estudiar(self):
        print(f"\nEl estudiante {self.nombre} {self.apellido} con la edad de {self.edad} años se encuentra cursando: {self.semestre} Semestre - INTER\n(+) Se ha registrado exisosamente")
        winsound.PlaySound(ruta_sonido_registro, winsound.SND_FILENAME)
        # Guardado de los registros en un archivo TXT
        with open(ruta_archivo,"a",encoding="UTF-8") as arch_studens: # Se debe poner , "w" para que se cree y escriba el archivo
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
try: # try realiza una verificacion de un evento, en este caso el evento es que se leea el archivo, si el archivo existe el programa continua sino manda una excepcion
    with open(ruta_archivo, "r"):
        pass
except FileNotFoundError: # en caso de que el programa llegue a except para que no se bloquee se agregan argumentos para que el programa pueda continuar
    with open(ruta_archivo, "w") as arch_studens:
        arch_studens.writelines("Estudiantes registrados en INTER:\n<-------------------------------------->\n")

# Bucle para preguntar al usuario o usuarios que se van a registrar
while True:
    user_inicio = int(input("Desea iniciar el programa de inscripcion? \n1. Si \n2. No \n : "))
    if user_inicio == 1:
        programa_inscripcion_datos()
    elif user_inicio == 2:
        print("\nPrograma de inscripcion finalizado")
        winsound.PlaySound(ruta_sonido_cierre, winsound.SND_FILENAME)
        break
    else:
        print("\nOpcion no valida\n")
