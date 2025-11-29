#Programa creado por José Muñoz Sánchez

numero_binario = input("Introduce un número binario: ")


def esBinario(numero_binario):
    for caracter in numero_binario:
        if caracter not in '01':
            return False
    return True

if esBinario(numero_binario):
    binarioEnDecimal = int(numero_binario, 2)
    print(binarioEnDecimal)
else:
    print("Quieto bicho. Ese numero no es binario.")