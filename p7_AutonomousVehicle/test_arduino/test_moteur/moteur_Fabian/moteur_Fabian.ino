#include <Arduino.h>
#include <Servo.h>
#include <Chrono.h>


// Définir les pins pour les moteurs (PWM et direction)
const int speedPin_M1 = 5;  // Pin PWM pour le moteur 1
const int speedPin_M2 = 6; // Pin PWM pour le moteur 2
const int directionPin_M1 = 4; // Pin direction pour le moteur 1
const int directionPin_M2 = 7; // Pin direction pour le moteur 2

Chrono sweepServo_chrono; // change servo angle every 50 ms

Servo myservo;    // create servo object to control a servo
#define  servoPin 9    // pin number of the servo
int pos = 90;    // initial position of the servo
bool doSweep = true;    // optional rotation of the servo
int minPos = 60;    // lower bound on the position angle
int maxPos = 120;    // upper bound
bool clockwise = false;    // initial direction of the servo rotation

int distanceInCm = 80;

#define infraredPin A0   // pin number of the sensor
float volts = 0;         // sensor analog value
int compteur = 0;

unsigned long previousMillis = 0; // Temps de la dernière lecture
const long interval = 50;

bool detection = false;       // Intervalle de 50 ms pour la lecture du capteur

void setup() {
  myservo.attach(servoPin);
  myservo.write(pos);
  Serial.begin(115200);       // Sets the baud rate to 9600

  // Configurer les pins des moteurs comme sorties
  pinMode(speedPin_M1, OUTPUT);
  pinMode(speedPin_M2, OUTPUT);
  pinMode(directionPin_M1, OUTPUT);
  pinMode(directionPin_M2, OUTPUT);

}

void carAdvance(int leftSpeed,int rightSpeed) {       //Move forward
  digitalWrite(directionPin_M1, leftSpeed > 0 ? HIGH : LOW);
  digitalWrite(directionPin_M2, rightSpeed > 0 ? LOW : HIGH);
  analogWrite (speedPin_M1, abs(leftSpeed));
  analogWrite (speedPin_M2, abs(rightSpeed));
}

void carStop(){                 //  Motor Stop
  digitalWrite(speedPin_M2,0);
  digitalWrite(speedPin_M1,0);
}


bool readSensor() {
  volts = analogRead(infraredPin) * 5.0 / 1024.0;  // 10 bits over 5 volts
  distanceInCm = convertMeasure();   // sensor characteristics
  
  if (distanceInCm < 30 && distanceInCm != 0) {
    Serial.println("obstacle");
    Serial.println(++compteur);
    return true;
  }
  return false;
}

int convertMeasure(){               // approximate sensor characteristics
  if (volts < 1) {
    distanceInCm = 28.0 / volts;
  } else {
    volts -= 0.28;
    distanceInCm = 20.2 / volts;
  }
  return distanceInCm;
}

void servoSweep(){
  const int SERVO_SPEED = 2;
  if(!clockwise){
    if(pos >= minPos && pos <= maxPos){
      pos += 2;                            // in steps of 1 degree
      myservo.write(pos);               // tell servo to go to position in variable 'pos'
    }
    if(pos >= maxPos)  clockwise = true; // change direction
  }else{
    if(pos >= minPos && pos <= maxPos){
      pos -= 2;
      myservo.write(pos);
    }
    if(pos <= minPos)  clockwise = false;
  }
}

void loopCommandReceived(bool detection) {
    String command = Serial.readStringUntil('\n');  // Lire la commande jusqu'à la fin de ligne

    // Vérifier la commande de connexion
    if (command.startsWith("A12")) {
        Serial.println("OK connexion");  // Acquittement de la connexion
    }
    // Vérifier la commande de contrôle des moteurs
    else if (command == "a" || detection) {
        carStop();
        Serial.println("Déconnecté");  // Acquittement de la déconnexion
    }
    else if (command.startsWith("C")) {
        int spaceIndex1 = command.indexOf(' ', 2);  // Trouver l'espace après "C"
        int motor1Speed = command.substring(2, spaceIndex1).toInt();  // Vitesse moteur 1
        int motor2Speed = command.substring(spaceIndex1 + 1).toInt();  // Vitesse moteur 2

        carAdvance(motor1Speed, motor2Speed);

        Serial.println("OK Fabian");  // Acquittement de la commande moteur
    }
    // Vérifier la commande de déconnexion
}


bool loopSensor(){
  unsigned long currentMillis = millis();
  detection = false;
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    detection = readSensor();
  }
  
  if(not detection){
    // Balayage du servo
    if(doSweep){
      if(sweepServo_chrono.hasPassed(50)){
        servoSweep();
      }
    }
  }
  //delay(50);

  return detection;
}



void loop() {
    // Vérifier si une commande est reçue sur le port série



  if (Serial.available()) {
    bool detection = loopSensor();
    loopCommandReceived(detection);

  }
}
