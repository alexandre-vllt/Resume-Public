#ifndef CAR_CONTROL_H
#define CAR_CONTROL_H

#include <Arduino.h>

// Déclaration des pins des moteurs (à reprendre de votre fichier principal si besoin)
const int speedPin_M1 = 5;  // Pin PWM pour le moteur 1
const int speedPin_M2 = 6; // Pin PWM pour le moteur 2
const int directionPin_M1 = 4; // Pin direction pour le moteur 1
const int directionPin_M2 = 7; // Pin direction pour le moteur 2

// Fonction pour tourner à droite
void carTurnRight(int speed) {
  digitalWrite(directionPin_M1, HIGH); // Avance moteur gauche
  digitalWrite(directionPin_M2, HIGH); // Recule moteur droit
  analogWrite(speedPin_M1, speed);     // Vitesse moteur gauche
  analogWrite(speedPin_M2, speed);     // Vitesse moteur droit
  
  delay(500); // Ajuster ce délai pour un quart de tour précis
  carStop();
}

// Fonction pour tourner à gauche
void carTurnLeft(int speed) {
  digitalWrite(directionPin_M1, LOW);  // Recule moteur gauche
  digitalWrite(directionPin_M2, LOW);  // Avance moteur droit
  analogWrite(speedPin_M1, speed);     // Vitesse moteur gauche
  analogWrite(speedPin_M2, speed);     // Vitesse moteur droit
  
  delay(500); // Ajuster ce délai pour un quart de tour précis
  carStop();
}

#endif // CAR_CONTROL_H
