from calculadora_dni import calculadora_dni
from calculadora_dni import calculadora_dni
def main ():
    numero_dni = int(input("Introduce tu numero de DNI: "))
    letra = calculadora_dni(numero_dni)
    print(f"DNI CALCULADO: {numero_dni}-{letra}")



main()