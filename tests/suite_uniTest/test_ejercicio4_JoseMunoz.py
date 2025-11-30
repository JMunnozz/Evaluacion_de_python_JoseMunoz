#Test realizado por Jose Muñoz Sánchez

import sys
import unittest

sys.path.insert(0, '../../src')

from ejercicio2.binario import esBinario
from ejercicio3.lista import estaEnRango, estaEnLista

binario_largo = "10110100110101000000111010010111011110101111001110000100101010000010010011011011100000110011011001111001001011000111000001010011111001001011111010101000011011111101010100100000100101101000001000100101011101111001100001010000010010111101011000101000010111011000000101100101011001000111101111000000001010111000110100100110101110000011111101101010111001110001111011010000011101111101111010111011011011000011111000111110011001100111010100000001110011000110011110001011001010111111101111001000000111010001110000001110000101111010001101000011000111101110111010011000110100100011010010001111010111101011100000110111011101010001110011011101100011101101010101101010000110101011100010100011001100001001101011101100001101000110010010101110011011100010101001010011010011011011101010101010011011101011101110011011110000110011010010011001010100001"
numero_largo = "298349810365594363532320497374633930469672050431856926153898835317754271786082342493990810236462942552026630819693431095564972869534996103806094829572842261811292241840628101346337120621238855576682432801593572332900460137769335087919916989671567425295247288801833567383404515744004197195098161884523439332410486071314377649595177620684457539592308771256228118954752741222067952304216394780752634363312642576388070648887032197537735286496873721379316556550586446370102225807850120369927404580676399057523465690504969015869135338753884078704317617463459618580134662284157912882219554974452502155985369102378686227654"

class TestEsBinario(unittest.TestCase):
    #Tests creados por Jose Muñoz Sánchez
    def test_caracteres_invalidos(self):
        #Comprueba que ocurre cuando insertamos caracteres invalidos dentro de la funcion
        self.assertEqual(esBinario("1$0101"), False)

    def test_numero_largo(self):
        #Comprobamos si soporta números binarios largos
        self.assertEqual(esBinario(binario_largo), True)

    def test_binario_con_espacios(self):
        #Se comprueba si acepta espacios entre los numeros
        self.assertEqual(esBinario("1         0    10 101       "), False)

    def test_binario_vacio(self):
        #Se comprueba si acepta una cadena vacia
        self.assertEqual(esBinario(""), True)

    def test_bucle_while(self):
        #Se comprueba si acepta un bucle infinito
        self.assertEqual(esBinario("while True: pass"), False)

    def test_comandos(self):
        #Miramos si podemos colarle comandos del sistema
        self.assertEqual(esBinario("ls"), False)

    def test_salto_de_linea(self):
        #Da un salto de linea si se lo insertamos?
        self.assertEqual(esBinario("1010\n10\n1\n"), False)

    def test_espacio_vacio(self):
        #Comprobamos si acepta una cadena vacia
        self.assertEqual(esBinario(""), True)


class TestEstaEnRangoYEstaEnLista(unittest.TestCase):
    #Tests creados por Jose Muñoz Sánchez
    #Tests para la funcion "estaEnRango"

    def test_rango_negativo(self):
        #Como reacciona frente a valores negativos
        self.assertEqual(estaEnRango(-5, 0, 10), False)
    
    def test_decimales(self):
        #Como reacciona frente a decimales
        self.assertEqual(estaEnRango(5.5, 0.0, 10.2), True)
    
    def test_numero_muyLargo(self):
        #Como reacciona frente a numeros muy largos
        self.assertEqual(estaEnRango(int(numero_largo), 0, int(numero_largo)+13), True)
    
    def test_comando(self):
        #Como reacciona frente a comandos
        self.assertEqual(estaEnRango("ls", 0, 10), False)

    def test_ddos(self):
        #Como reacciona frente a un intento de "ataque DDOS"
        self.assertEqual(estaEnRango("A"*10000000, 0, 10), False)

    #Tests para la funcion "estaEnLista"

    def test_lista_vacia(self):
        #Como reacciona frente a una lista vacia
        self.assertEqual(estaEnLista("usuario1", []), False)
    
    def test_listas_de_listas(self):
        #Como reacciona frente a listas de listas
        self.assertEqual(estaEnLista("usuario1", [["usuario2", "pass2"], ["usuario3", "pass3"]]), False)
    
    def test_lista_vacia(self):
        #Como reacciona frente a una lista vacia
        self.assertEqual(estaEnLista("", []), False)
    
    def test_comando(self):
        #Como reacciona frente a comandos
        self.assertEqual(estaEnLista("ls", ["usuario1", "usuario2"]), False)
    
    def test_bucle_while(self):
        #Como reacciona frente a un bucle while
        self.assertEqual(estaEnLista("while True: pass", ["usuario1", "usuario2"]), False)

    def test_ddos(self):
        #Como reacciona frente a un intento de "ataque DDOS"
        self.assertEqual(estaEnLista("A"*10000000, ["usuario1", "usuario2"]), False)


if __name__ == "__main__":
    unittest.main()