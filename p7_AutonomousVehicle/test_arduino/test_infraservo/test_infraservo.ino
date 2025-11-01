#include <Chrono.h>
#include <Arduino.h>
#include <Servo.h>


// Définir les pins pour les moteurs (PWM et direction)
const int speedPin_M1 = 5;  // Pin PWM pour le moteur 1
const int speedPin_M2 = 6; // Pin PWM pour le moteur 2
const int directionPin_M1 = 4; // Pin direction pour le moteur 1
const int directionPin_M2 = 7; // Pin direction pour le moteur 2
const int temps_detection = 30;

Chrono sweepServo_chrono; // change servo angle every 50 ms

Servo myservo;    // create servo object to control a servo
#define  servoPin 9    // pin number of the servo
int pos = 90;    // initial position of the servo
bool doSweep = true;    // optional rotation of the servo
int minPos = 75;    // lower bound on the position angle
int maxPos = 105;    // upper bound
bool clockwise = false;    // initial direction of the servo rotation
int direction_dispo[3];

int distanceInCm = 80;

#define infraredPin A0   // pin number of the sensor
float volts = 0;         // sensor analog value
int compteur = 0;

unsigned long previousMillis = 0; // Temps de la dernière lecture
const long interval = 50;

int compteur_detection =0;
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


// Fonction pour tourner à droite
void carTurnRight(int speed) {
  digitalWrite(directionPin_M1, LOW); // Avance moteur gauche
  digitalWrite(directionPin_M2, LOW); // Recule moteur droit
  analogWrite(speedPin_M1, speed);     // Vitesse moteur gauche
  analogWrite(speedPin_M2, speed);     // Vitesse moteur droit
  
  delay(600); // Ajuster ce délai pour un quart de tour précis
  carStop();
}

// Fonction pour tourner à gauche
void carTurnLeft(int speed) {
  digitalWrite(directionPin_M1, HIGH);  // Recule moteur gauche
  digitalWrite(directionPin_M2, HIGH);  // Avance moteur droit
  analogWrite(speedPin_M1, speed);     // Vitesse moteur gauche
  analogWrite(speedPin_M2, speed);     // Vitesse moteur droit
  
  delay(600); // Ajuster ce délai pour un quart de tour précis
  carStop();
}

void carTurnBack(int speed) {
  digitalWrite(directionPin_M1, HIGH);  // Recule moteur gauche
  digitalWrite(directionPin_M2, HIGH);  // Avance moteur droit
  analogWrite(speedPin_M1, speed);     // Vitesse moteur gauche
  analogWrite(speedPin_M2, speed);     // Vitesse moteur droit
  
  delay(1250); // Ajuster ce délai pour un quart de tour précis
  carStop();
}

void carTurnAround(int speed) {
  digitalWrite(directionPin_M1, HIGH);  // Recule moteur gauche
  digitalWrite(directionPin_M2, HIGH);  // Avance moteur droit
  analogWrite(speedPin_M1, speed);     // Vitesse moteur gauche
  analogWrite(speedPin_M2, speed);     // Vitesse moteur droit
  
  delay(2500); // Ajuster ce délai pour un quart de tour précis
  carStop();
}



bool readSensor() {
  volts = analogRead(infraredPin) * 5.0 / 1024.0;  // 10 bits over 5 volts
  distanceInCm = convertMeasure();   // sensor characteristics
  
  if (distanceInCm < 30 && distanceInCm != 0) {
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
  const int SERVO_SPEED = 3;
  if(!clockwise){
    if(pos >= minPos && pos <= maxPos){
      pos += SERVO_SPEED;                            // in steps of 1 degree
      myservo.write(pos);               // tell servo to go to position in variable 'pos'
    }
    if(pos >= maxPos)  clockwise = true; // change direction
  }else{
    if(pos >= minPos && pos <= maxPos){
      pos -= SERVO_SPEED;
      myservo.write(pos);
    }
    if(pos <= minPos)  clockwise = false;
  }
}

void loopCommandReceived(bool detection, String command) {
  
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

bool loopSensorLine(){
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
  
  return detection;
}


void loopSensorInter(int (&chemin_block)[3]){
  
  int   IminPos = 20;
  int Imaxpos = 160;
  
  pos = IminPos;
  myservo.write(pos);
  delay(2000);
  
  while(pos <= Imaxpos){
    unsigned long currentMillis = millis();
    detection = false;
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      detection = readSensor();
    }
    if(detection){
      if(pos<60) chemin_block[0] = 1;
      if(pos>=60 and pos<120) chemin_block[1] = 1;
      if(pos>120) chemin_block[2] = 1;
    }
    pos = pos + 4;
    myservo.write(pos);
    delay(50);
  }
  pos = 90;
  myservo.write(pos);
  delay(50);
}
    
    
  

void loop() {


  if (Serial.available()) {

    detection = loopSensorLine();

		String command = Serial.readStringUntil('\n');  // Lire la commande jusqu'à la fin de ligne
		if (command.startsWith("I")){
			String stringValue;
			direction_dispo[0] = 0;
			direction_dispo[1] = 0;
			direction_dispo[2] = 0;
			loopSensorInter(direction_dispo);
			for (int i = 0; i < 3; i++) {
				stringValue += String(direction_dispo[i]);
				}
			Serial.println(stringValue);
		}else if(command.startsWith("R")){
      carTurnRight(255);
    }else if(command.startsWith("L")){
      carTurnLeft(255);
    } else if (command.startsWith("H")){
      carTurnBack(255);
    } else if (command.startsWith("G")){
      carTurnAround(255);
    }
    else loopCommandReceived(detection, command);	
    

    //Demi-Tour
    if(detection){
			++compteur_detection;
			if(compteur_detection >= temps_detection){
				carTurnBack(255);
        Serial.println("Demi-tour");
				compteur_detection = 0;
				detection = false;
			}
		}else{
			compteur_detection = 0;
		}
  }
}

 

   
