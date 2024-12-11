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


# Ejemplo de uso
instrucciones_astar = [
"Me muevo arriba",
"Me muevo arriba a la derecha",
"Me muevo arriba a la derecha",
"Me muevo arriba",
"Me muevo arriba a la izquierda",
"Me muevo arriba a la izquierda"
]

codigo = generar_codigo_robot(instrucciones_astar)
print(codigo)
