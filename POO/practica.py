class Cuenta_Bancaria():
    def __init__(self, nombre, deposito):
        self.nombre = nombre
        self.deposito = deposito # Se usa el nombre self.recarga para hacer referencia a deposito
        
    def depositar(self, cantidad):
        self.deposito += cantidad # Toma lo que esta almacenado en deposito en este caso 2500 y lo suma con la cantidad que le envia el usuario en este caso 2000
        return self.deposito # Devuelve la suma a cantidad para poder ver o usar el nuevo valor.
    
    def ver_saldo(self):
        return self.deposito
    
cliente = Cuenta_Bancaria("Yeison", 2500)
# Al ejecutarse la funcion la variable nuevo_saldo sera igual al valor del return de la funcion en este caso nuevo_saldo = self.deposito
nuevo_saldo = cliente.depositar(2000) # Si no hay nada en el return va a valer = none (nada o estara vacio)
saldo = cliente.ver_saldo()


print(type(nuevo_saldo))# Se ve que ahora es un valor entero
print(nuevo_saldo)# Se imprime el valor actual
print(f"Su saldo es de {saldo}")