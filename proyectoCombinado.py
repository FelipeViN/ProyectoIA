import math
import time

# Funcion que Genera el Codigo
def generar_codigo_robot(instrucciones):
    movimientos_robot = {
        "Me muevo arriba": "avanza(); delay(200);",
        "Me muevo abajo": "retrocede(); delay(200);",
        "Me muevo a la izquierda": "izquierda(); delay(200);",
        "Me muevo a la derecha": "derecha(); delay(200);",
        "Me muevo arriba a la izquierda": "izquierda(); avanza(); delay(200);",
        "Me muevo arriba a la derecha": "derecha(); avanza(); delay(200);",
        "Me muevo abajo a la izquierda": "izquierda(); retrocede(); delay(200);",
        "Me muevo abajo a la derecha": "derecha(); retrocede(); delay(200);"
    }

    # Código base para el robot
    codigo_robot = """
#include "NewPing.h"

#define PIN_TRIG 12
#define PIN_ECHO 8
#define MAX_DISTANCIA 100

NewPing sonar(PIN_TRIG, PIN_ECHO, MAX_DISTANCIA);

// Motor 1
int ENA = 9;
int IN1 = 7;
int IN2 = 6;
// Motor 2
int IN3 = 5;
int IN4 = 4;
int ENB = 3;

void setup() {
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(ENA, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
    pinMode(ENB, OUTPUT);
    Serial.begin(9600);
}

void loop() {
"""

    # Agregar movimientos al loop
    for instruccion in instrucciones:
        if instruccion in movimientos_robot:
            codigo_robot += f"    {movimientos_robot[instruccion]}\n"

    # Finalizar el código
    codigo_robot += """
    parar(); // Detiene el robot al finalizar la secuencia
}

void avanza() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENA, 200);
    analogWrite(ENB, 200);
}

void retrocede() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 200);
    analogWrite(ENB, 200);
}

void derecha() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 120);
    analogWrite(ENB, 0);
}

void izquierda() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENA, 0);
    analogWrite(ENB, 120);
}

void parar() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
}
"""
    return codigo_robot

# metodo que encuentra la columna de salida
def halla_columna_salida(laberinto):
    i, j = 0, 0
    for fila in laberinto:
        i += 1
        for caracter in fila:
            j += 1
            if caracter == 's':  
                break
        if laberinto[i - 1][j - 1] == 's':
            break
        j = 0
    return j

# metodo que encuentra la fila de salida
def halla_fila_salida(laberinto):
    i, j = 0, 0
    for fila in laberinto:
        i += 1
        for caracter in fila:
            j += 1
            if caracter == 's':
                break
        if laberinto[i - 1][j - 1] == 's':
            break
        j = 0
    return i

# metodo que encuentra la columna de entrada
def halla_columna_entrada(laberinto):
    i, j = 0, 0
    for fila in laberinto:
        i += 1
        for caracter in fila:
            j += 1
            if caracter == 'e':  
                break
        if laberinto[i - 1][j - 1] == 'e':
            break
        j = 0
    return j

# metodo que encuentra la fila de entrada
def halla_fila_entrada(laberinto):
    i, j = 0, 0
    for fila in laberinto:
        i += 1
        for caracter in fila:
            j += 1
            if caracter == 'e':
                break
        if laberinto[i - 1][j - 1] == 'e':
            break
        j = 0
    return i

# calculo de hn
def hn(X1, Y1, laberinto):
    X2 = halla_fila_salida(laberinto)
    Y2 = halla_columna_salida(laberinto)
    resultado = math.sqrt((math.pow((X1 - X2), 2)) + (math.pow((Y1 - Y2), 2)))
    return resultado

# nos indica a donde se movera.
def movimiento(laberinto, n):
    n += 1
    columnaE = halla_columna_entrada(laberinto) - 1
    filaE = halla_fila_entrada(laberinto) - 1

    fnAb, fnIz, fnAr, fnDe = 0, 0, 0, 0
    fnAbIz, fnAbDe, fnArIz, fnArDe = 0, 0, 0, 0  # Diagonales

    hayAbajo = filaE + 1 < len(laberinto) 
    hayIzquierda = columnaE - 1 >= 0 
    hayArriba = filaE - 1 >= 0 
    hayDerecha = columnaE + 1 < len(laberinto[0])

    # Diagonales
    hayAbajoIzquierda = hayAbajo and hayIzquierda and laberinto[filaE + 1][columnaE - 1] != 'o'
    hayAbajoDerecha = hayAbajo and hayDerecha and laberinto[filaE + 1][columnaE + 1] != 'o'
    hayArribaIzquierda = hayArriba and hayIzquierda and laberinto[filaE - 1][columnaE - 1] != 'o'
    hayArribaDerecha = hayArriba and hayDerecha and laberinto[filaE - 1][columnaE + 1] != 'o'
    
    hayAbajo = hayAbajo and laberinto[filaE + 1][columnaE] != 'o'
    hayIzquierda = hayIzquierda and laberinto[filaE][columnaE - 1] != 'o'
    hayArriba = hayArriba and laberinto[filaE - 1][columnaE] != 'o'
    hayDerecha = hayDerecha and laberinto[filaE][columnaE + 1] != 'o'
    
    if hayAbajo:
        if laberinto[filaE+1][columnaE] =='s': return "Me muevo abajo"
    if hayIzquierda:
        if laberinto[filaE][columnaE-1] =='s': return "Me muevo a la izquierda"
    if hayArriba:
        if laberinto[filaE-1][columnaE] =='s': return "Me muevo arriba"
    if hayDerecha:
        if laberinto[filaE][columnaE+1] =='s': return "Me muevo a la derecha"
        
    if hayAbajoIzquierda:
        if laberinto[filaE+1][columnaE-1] =='s': return "Me muevo abajo a la izquierda"
    if hayArribaIzquierda:
        if laberinto[filaE-1][columnaE-1] =='s': return "Me muevo arriba a la izquierda"
    if hayArribaDerecha:
        if laberinto[filaE-1][columnaE+1] =='s': return "Me muevo arriba a la derecha"
    if hayAbajoDerecha:
        if laberinto[filaE+1][columnaE+1] =='s': return "Me muevo abajo a la derecha"

    if hayAbajo:
        fnAb = hn(filaE + 1, columnaE, laberinto) + n
    if hayIzquierda:
        fnIz = hn(filaE, columnaE - 1, laberinto) + n
    if hayArriba:
        fnAr = hn(filaE - 1, columnaE, laberinto) + n
    if hayDerecha:
        fnDe = hn(filaE, columnaE + 1, laberinto) + n

    if hayAbajoIzquierda:
        fnAbIz = hn(filaE + 1, columnaE - 1, laberinto) + n
    if hayAbajoDerecha:
        fnAbDe = hn(filaE + 1, columnaE + 1, laberinto) + n
    if hayArribaIzquierda:
        fnArIz = hn(filaE - 1, columnaE - 1, laberinto) + n
    if hayArribaDerecha:
        fnArDe = hn(filaE - 1, columnaE + 1, laberinto) + n

    movimientos = []
    if hayAbajo:
        movimientos.append(("Me muevo abajo", fnAb))
    if hayIzquierda:
        movimientos.append(("Me muevo a la izquierda", fnIz))
    if hayArriba:
        movimientos.append(("Me muevo arriba", fnAr))
    if hayDerecha:
        movimientos.append(("Me muevo a la derecha", fnDe))
    if hayAbajoIzquierda:
        movimientos.append(("Me muevo abajo a la izquierda", fnAbIz))
    if hayAbajoDerecha:
        movimientos.append(("Me muevo abajo a la derecha", fnAbDe))
    if hayArribaIzquierda:
        movimientos.append(("Me muevo arriba a la izquierda", fnArIz))
    if hayArribaDerecha:
        movimientos.append(("Me muevo arriba a la derecha", fnArDe))

    if movimientos:
        # Selecciona el movimiento con el menor costo fn
        return min(movimientos, key=lambda x: x[1])[0]

    return "No hay salida"


# mueve la posición de 'e' que determina realmente donde estamos en el laberinto
def recorriendo_laberinto(cadena, laberinto, recorrido):
    filaE = halla_fila_entrada(laberinto) - 1
    columnaE = halla_columna_entrada(laberinto) - 1

    if cadena == "No hay salida":
        laberinto[filaE][columnaE] = 'o'
        recorrido.retroceder()
        filaE, columnaE = recorrido.get_fila_actual(), recorrido.get_columna_actual()
        laberinto[filaE][columnaE] = 'e'
        print("No hay salida, retrocediendo a la posición anterior.")
        return

    if cadena == "Me muevo abajo":
        recorrido.agregar_nodo(filaE + 1, columnaE)
        laberinto[filaE + 1][columnaE] = 'e'
    elif cadena == "Me muevo arriba":
        recorrido.agregar_nodo(filaE - 1, columnaE)
        laberinto[filaE - 1][columnaE] = 'e'
    elif cadena == "Me muevo a la izquierda":
        recorrido.agregar_nodo(filaE, columnaE - 1)
        laberinto[filaE][columnaE - 1] = 'e'
    elif cadena == "Me muevo a la derecha":
        recorrido.agregar_nodo(filaE, columnaE + 1)
        laberinto[filaE][columnaE + 1] = 'e'
    elif cadena == "Me muevo abajo a la izquierda":
        recorrido.agregar_nodo(filaE + 1, columnaE - 1)
        laberinto[filaE + 1][columnaE - 1] = 'e'
    elif cadena == "Me muevo abajo a la derecha":
        recorrido.agregar_nodo(filaE + 1, columnaE + 1)
        laberinto[filaE + 1][columnaE + 1] = 'e'
    elif cadena == "Me muevo arriba a la izquierda":
        recorrido.agregar_nodo(filaE - 1, columnaE - 1)
        laberinto[filaE - 1][columnaE - 1] = 'e'
    elif cadena == "Me muevo arriba a la derecha":
        recorrido.agregar_nodo(filaE - 1, columnaE + 1)
        laberinto[filaE - 1][columnaE + 1] = 'e'

    laberinto[filaE][columnaE] = 'l'
    
# clase nodo, para poder almacenar las coordenas por donde vamos pasando en el laberinto
class Nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.anterior = None
        self.siguiente = None

# lista doblemente ligada que es la que almacenara nuestros movimientos en el laberinto
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def agregar_nodo(self, fila, columna):
        nuevo = Nodo(fila, columna)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.actual = nuevo
        else:
            self.actual.siguiente = nuevo
            nuevo.anterior = self.actual
            self.actual = nuevo

    def retroceder(self):
        if self.actual is not None and self.actual.anterior is not None:
            self.actual = self.actual.anterior

    def get_fila_actual(self):
        return self.actual.fila

    def get_columna_actual(self):
        return self.actual.columna


# metodo imprimir laberinto
def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(fila))
    print()


def main():
    inicio = time.time()
    # Laberinto
    laberinto = [
        ['l', 'l', 'o', 'l', 'o', 'o', 'o', 'o', 'o', 'l'],
        ['l', 'o', 'l', 'o', 'o', 'o', 'o', 'l', 'o', 'o'],
        ['l', 'l', 'o', 'o', 'o', 'l', 'l', 'o', 'l', 'l'],
        ['l', 'l', 'o', 'l', 'o', 'o', 'l', 's', 'l', 'o'],
        ['l', 'o', 'l', 'l', 'o', 'o', 'l', 'l', 'l', 'l'],
        ['l', 'l', 'o', 'l', 'o', 'l', 'o', 'e', 'o', 'l'],
        ['l', 'o', 'o', 'l', 'l', 'o', 'o', 'o', 'o', 'l'],
        ['l', 'l', 'l', 'o', 'l', 'l', 'o', 'l', 'l', 'o'],
        ['l', 'o', 'o', 'o', 'l', 'o', 'l', 'l', 'o', 'o'],
        ['o', 'l', 'l', 'l', 'l', 'o', 'l', 'l', 'o', 'l'],
    ]
    # Imprimir laberinto
    recorrido = ListaDoble()
    # Agregar la entrada a la lista de recorrido
    recorrido.agregar_nodo(halla_fila_entrada(laberinto) - 1, halla_columna_entrada(laberinto) - 1)

    xs = halla_columna_salida(laberinto)  # Columna de la salida
    ys = halla_fila_salida(laberinto)     # Fila de la salida
    xe = halla_columna_entrada(laberinto) # Columna de la entrada
    ye = halla_fila_entrada(laberinto)    # Fila de la entrada
    ct = 0                                # Contador de movimientos

    # Lista para guardar las instrucciones
    instrucciones_astar = []

    while xe != xs or ye != ys:  # Mientras no se haya llegado a la salida
        mov = movimiento(laberinto, ct) # Movimiento a realizar
        instrucciones_astar.append(mov)  # Guardar cada movimiento en la lista
        recorriendo_laberinto(mov, laberinto, recorrido) # Mover la posición de 'e' en el laberinto

        # Actualizamos las coordenadas de la entrada
        xe = halla_columna_entrada(laberinto)
        ye = halla_fila_entrada(laberinto)

        ct += 1

        # Condición para evitar un bucle infinito
        if ct > 1000:
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
            print("El algoritmo no encontró la salida dentro de 100 movimientos.")
            break

    # Imprimir la lista de instrucciones
    print( instrucciones_astar)
    # Pasamos las Instrucciones al codigo que nos ayuda a mover el robot
    codigo = generar_codigo_robot(instrucciones_astar)
    print(codigo)
    # Retornar la lista de instrucciones
    return instrucciones_astar


if __name__ == "__main__":
    instrucciones_astar = main()


