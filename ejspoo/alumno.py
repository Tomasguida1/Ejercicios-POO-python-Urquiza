class alumno(): 
    def __init__(self):
        self.nombre = input("el nombre del alumno es: ")
        self.nota = int(input("la nota del alumno es: "))
    def imprimir(self):
        print ("el nombre del alumno es ", self.nombre, " la nota del alumno es ", self.nota)
    def esregular(self):
        if (self.nota  >= 4 ):
            print ("el alumno esta regular")
        else:
            print ("el alumno no esta regular")
        
def main():
    alum = alumno()
    alum.imprimir()
    alum.esregular()
main()