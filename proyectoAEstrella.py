import math
import time

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

# nos indica a donde se movera, por el momento en cruz
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


# metodo principal 
def main():
    inicio = time.time()
    laberinto = [
    ['l', 'l', 'o', 'l', 'o', 'o', 'o', 'o', 'o', 'l'],
    ['l', 'o', 'l', 'o', 'o', 'o', 'o', 'l', 'o', 'o'],
    ['l', 'l', 'o', 'o', 'o', 'l', 'l', 'o', 'l', 'l'],
    ['l', 'l', 'o', 'l', 'o', 'o', 'l', 's', 'l', 'o'],
    ['l', 'o', 'l', 'l', 'o', 'o', 'l', 'l', 'l', 'l'],
    ['l', 'l', 'o', 'l', 'o', 'l', 'o', 'l', 'o', 'l'],
    ['l', 'o', 'o', 'l', 'l', 'o', 'o', 'o', 'o', 'l'],
    ['l', 'l', 'l', 'o', 'l', 'l', 'o', 'l', 'l', 'o'],
    ['l', 'o', 'o', 'o', 'l', 'o', 'l', 'l', 'o', 'o'],
    ['o', 'l', 'l', 'l', 'l', 'o', 'l', 'e', 'o', 'l'],
    
]

    recorrido = ListaDoble()
    recorrido.agregar_nodo(halla_fila_entrada(laberinto) - 1, halla_columna_entrada(laberinto) - 1)

    # imprimir_laberinto(laberinto)
    # print(f"Tamaño del laberinto filas {len(laberinto)} columnas {len(laberinto[0])}")
    # print(f"Punto de partida original {halla_fila_entrada(laberinto)},{halla_columna_entrada(laberinto)}")
    # print(f"Punto de salida original {halla_fila_salida(laberinto)},{halla_columna_salida(laberinto)}")

    xs = halla_columna_salida(laberinto)  # Columna de la salida
    ys = halla_fila_salida(laberinto)     # Fila de la salida
    xe = halla_columna_entrada(laberinto) # Columna de la entrada
    ye = halla_fila_entrada(laberinto)    # Fila de la entrada
    ct = 0

    while xe != xs or ye != ys:  # Mientras no se haya llegado a la salida
        # print("-------------------------------")
        # print("Posición actualizada")
        mov = movimiento(laberinto, ct)
        print(f'"{mov}",')
        recorriendo_laberinto(mov, laberinto, recorrido)

        # print(f"Nuevo punto de partida {halla_fila_entrada(laberinto)},{halla_columna_entrada(laberinto)}")
        # imprimir_laberinto(laberinto)

        # actualizamos las coordenadas de la entrada
        xe = halla_columna_entrada(laberinto)
        ye = halla_fila_entrada(laberinto)

        ct += 1
        # print(f"Movimiento número: {ct}")

        # condición para evitar un bucle infinito
        if ct > 1000:
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
            print("El algoritmo no encontró la salida dentro de 100 movimientos.")
            break

    # if xe == xs and ye == ys:
        # fin = time.time()
        # tiempo_ejecucion = fin - inicio
        # print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
        # print("¡Salida encontrada!")

if __name__ == "__main__":
    main()
