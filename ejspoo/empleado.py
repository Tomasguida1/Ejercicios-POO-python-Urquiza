class empleado(): 
    def __init__(self):
        self.nombre = input("el nombre del empleado es: ")
        self.sueldo = int(input("el sueldo del empleado es: "))
    def imprimir(self):
        print ("el nombre del empleado es ", self.nombre, " el sueldo es ", self.sueldo)
    def pagarimpuestos(self):
        if (self.sueldo  > 3000 ):
            print ("el empleado debe pagar impuestos")
        else:
            print ("el empleado no debe pagar impuestos")
        
def main():
    emp = empleado()
    emp.imprimir()
    emp.pagarimpuestos()
main()