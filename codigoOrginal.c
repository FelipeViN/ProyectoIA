#include "NewPing.h"
#define PIN_TRIG 12  // Pin del Arduino conectado al pin Trigger del sensor de ultrasonidos
#define PIN_ECHO 8   // Pin del Arduino conectado al pin Echo del sensor de ultrasonidos
#define MAX_DISTANCIA 100  // Distancia máxima a detectar en cm.

NewPing sonar(PIN_TRIG, PIN_ECHO, MAX_DISTANCIA);

//motor 1
int ENA = 9;
int IN1 = 7;
int IN2 = 6;

//motor 2
int IN3 = 5;
int IN4 = 4;
int ENB = 3;

long randomNumber;
const int PinLedRojo = 11;
const int PinLedVerde = 10;
const int PinLedAzul = 13;
int zumbador = 2; // Pin para el zumbador

void setup() {
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(PinLedVerde, OUTPUT);
  pinMode(PinLedRojo, OUTPUT);
  pinMode(PinLedAzul, OUTPUT);
  pinMode(zumbador, OUTPUT); // Configurar el pin del zumbador como salida
}

void loop() {
  //delay(500);
  int tiempo = sonar.ping_median();
  int distancia = tiempo / US_ROUNDTRIP_CM;
  
  // Imprimir el tiempo medido en la consola
  Serial.print("Tiempo: ");
  Serial.print(tiempo);
  Serial.println(" microsegundos");
  
  // Imprimir la distancia medida en la consola
  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  if (distancia > 0) {  // hay espacio
    if(distancia < 30){
      parada(1000);
      digitalWrite(zumbador, HIGH); // Activar el zumbador
      delay(200);
      digitalWrite(zumbador, LOW); // Desactivar el zumbador

      if(distancia < 20){
        rojo();
        retrocede();
        delay(200);
      } else {
        randomNumber = random(1,2);
        Serial.print("El numero aleatorio es = ");
        Serial.println(randomNumber);
        if (randomNumber == 1){
          azul();
          izquierda();
          delay(400);
          parada(500);
        } else {
          azul();
          derecha();
          delay(400);
          parada(500);
        }
      }
    } else {
      verde();
      avanza();
    }
  }
}

void parada(uint16_t tiempo) {
  parar();  // Para los motores
  delay(tiempo);  // Espera el tiempo que se le indique.
}

void avanza(){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
}

void retrocede(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
}

void derecha(){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 120);
  analogWrite(ENB, 0);
}

void izquierda(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, 0);
  analogWrite(ENB, 120);
}

void parar(){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

void verde() {
  Serial.println("¡Verde!");
  digitalWrite(PinLedRojo, LOW);
  digitalWrite(PinLedVerde, HIGH);
  digitalWrite(PinLedAzul, LOW);
}

void rojo() {
  Serial.println("¡Rojo!");
  digitalWrite(PinLedRojo, HIGH);
  digitalWrite(PinLedVerde, LOW);
  digitalWrite(PinLedAzul, LOW);
}

void azul() {
  Serial.println("¡Azul!");
  digitalWrite(PinLedRojo, LOW);
  digitalWrite(PinLedVerde, LOW);
  digitalWrite(PinLedAzul, HIGH);
}
