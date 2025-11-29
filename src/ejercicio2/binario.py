#Programa creado por José Muñoz Sánchez

strbinario = input("Introduce un número binario: ")


def esBinario(strbinario):
    for caracter in strbinario:
        if caracter not in '01':
            return False
    return True

if esBinario(strbinario):
    binarioEnDecimal = int(strbinario, 2)
    print(strbinario)
else:
    print("Quieto bicho. Ese numero no es binario.")