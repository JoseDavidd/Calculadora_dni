def calculadora_dni():
    numero_dni = int(input("Introduce tu numero de DNI: "))
    letra_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    formula = numero_dni % len(letra_dni)
    return letra_dni[formula]
print(f"{numero_dni}-{formula}")
calculadora_dni()


#Esta letra se obtiene a partir del número completo del DNI dividido entre el número 23.
#  Al resto resultante de dicha división, que está comprendido entre 0 y 22, 
# se le asigna la letra de control según una equivalencia. No se utilizan las letras: I, Ñ, O, U.



