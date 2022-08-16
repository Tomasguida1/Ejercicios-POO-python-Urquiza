class persona(): 
    def __init__(self):
        self.nombre = input("el nombre de la persona es: ")
        self.edad = int(input("la edad de la persona es: "))
    def imprimir(self):
        print ("el nombre de la persona es ", self.nombre, " la edad es ", self.edad)
    def esmayor(self):
        if (self.edad  >= 18 ):
            print ("la persona es mayor de edad")
        else:
            print ("la persona no es mayor de edad")
        
def main():
    pers = persona()
    pers.imprimir()
    pers.esmayor()
main()