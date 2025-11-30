#Programa creado por José Muñoz Sánchez

usuarios = {
    "iperurena": {
    "nombre": "Iñaki",
    "apellido": "Perurena",
    "password": "123123"
},
    "fmuguruza": {
    "nombre": "Fermín",
    "apellido": "Muguruza",
     "password": "654321"
 },
    "aolaizola": {
    "nombre": "Aimar",
    "apellido": "Olaizola",
    "password": "123456"
 }
 }

def estaEnRango(valor, minimo, maximo):
    if( valor >= minimo and valor <= maximo):
         return True
    else:
         return False

def estaEnLista(valor, lista):
     if(valor in lista):
          return True
     else:
          return False

#Funciones creadas por José Muñoz Sánchez

intentos = 0

while estaEnRango(intentos, 0, 2):
    preguntaNombre = input("Introduce un nombre: ")
    preguntaContraseña = input("Introduce la contraseña del usuario: ")

    if estaEnLista(preguntaNombre, usuarios):
        if preguntaContraseña == usuarios[preguntaNombre]["password"]:
            print("Has iniciado sesión correctamente. Tu nombre es "+usuarios[preguntaNombre]["nombre"]+", tu apellido "+usuarios[preguntaNombre]["apellido"]+" y mi nombre José Muñoz")
            break
        else:
            print("Contraseña incorrecta")
            intentos +=1
    else:
        intentos +=1
        print("El nombre de usuario no existe")
if(intentos == 3):
        print("Has superado el número de intentos")    
      
         