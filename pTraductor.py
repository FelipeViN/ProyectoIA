# Traductor: Convierte instrucciones en movimientos para el carrito

# Output de instrucciones del A* (ejemplo)
instrucciones = [
    "Me muevo arriba",
    "Me muevo arriba a la derecha",
    "Me muevo arriba a la derecha",
    "Me muevo arriba",
    "Me muevo arriba a la izquierda",
    "Me muevo arriba a la izquierda"
]

# Traducción de las instrucciones a funciones de movimiento del carrito
def traducir_instrucciones_a_codigo(instrucciones):
    codigo = """#include <Arduino.h>

int IN1 = 7;
int IN2 = 6;
int IN3 = 5;
int IN4 = 4;
int ENA = 9;
int ENB = 3;

void setup() {
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
    pinMode(ENA, OUTPUT);
    pinMode(ENB, OUTPUT);
}

void loop() {
"""

    movimientos = {
        "Me muevo arriba": "avanzar();",
        "Me muevo abajo": "retroceder();",
        "Me muevo a la izquierda": "girarIzquierda();",
        "Me muevo a la derecha": "girarDerecha();",
        "Me muevo arriba a la izquierda": "avanzarDiagonalIzquierda();",
        "Me muevo arriba a la derecha": "avanzarDiagonalDerecha();",
        "Me muevo abajo a la izquierda": "retrocederDiagonalIzquierda();",
        "Me muevo abajo a la derecha": "retrocederDiagonalDerecha();",
    }

    for instruccion in instrucciones:
        if instruccion in movimientos:
            codigo += f"    {movimientos[instruccion]}\n"

    codigo += "}"  # Cierra el loop de Arduino

    # Funciones auxiliares
    codigo += """

void avanzar() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENA, 200);
    analogWrite(ENB, 200);
    delay(500);
}

void retroceder() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 200);
    analogWrite(ENB, 200);
    delay(500);
}

void girarIzquierda() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENA, 150);
    analogWrite(ENB, 150);
    delay(500);
}

void girarDerecha() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 150);
    analogWrite(ENB, 150);
    delay(500);
}

void avanzarDiagonalIzquierda() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENA, 100);
    analogWrite(ENB, 200);
    delay(500);
}

void avanzarDiagonalDerecha() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENA, 200);
    analogWrite(ENB, 100);
    delay(500);
}

void retrocederDiagonalIzquierda() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 100);
    analogWrite(ENB, 200);
    delay(500);
}

void retrocederDiagonalDerecha() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 200);
    analogWrite(ENB, 100);
    delay(500);
}
"""

    return codigo

# Generar el código traducido
codigo_traducido = traducir_instrucciones_a_codigo(instrucciones)

# Mostrar el resultado
print(codigo_traducido)
