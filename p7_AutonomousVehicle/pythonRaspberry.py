# Importer la bibliothèque de gestion de la liaison série
import serial
import time

def connexionArduino():
    # Configurer le port série pour communiquer avec l'Arduino
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.1)
    time.sleep(1)  # Attendre un peu pour que la connexion soit établie

    # Envoyer la commande de connexion pour activer la communication
    arduino.write(b'A12')  # A12 : Connexion avec acquittement en ASCII
    response = arduino.readline().decode('utf-8').strip()
    print("Réponse de connexion de l'Arduino :", response)

    return arduino


def envoiCommande(arduino, gauche, droite, minSpeed, maxSpeed):
    '''
    gauche: entre 0 et 1
    droite: entre 0 et 1
    minSpeed: entre 0 et 255 (110 marche bien !)
    maxSpeed: entre 0 et 255 (mettre entre 150 et 255 marche bien, 255 marche le mieux)
    '''
    commande = f"C {max(minSpeed, gauche * maxSpeed)} {max(minSpeed, droite * maxSpeed)}\n"
    #print(gauche, droite)
    arduino.write(commande.encode('utf-8'))
    #time.sleep(2)
    response = arduino.readline().decode('utf-8').strip()
    return response
    #print("Réponse de l'Arduino pour la commande moteur :", response)
    #time.sleep(2)

# Envoyer la commande d'intersection (et la recevoir)

def envoieIntersection(arduino):
    arduino.write(b'I')
    time.sleep(6)
    response = arduino.readline().decode('utf-8').strip()
    obstaclesDetectes = [False, False, False] # True si un obstacle est détecté
    print(f'response: {response}')
    for i in range(len(response)):
        if response[i] == "1":
            obstaclesDetectes[2 - i] = True
    return obstaclesDetectes 

# Envoie commande de rotation
def envoieRotation(arduino, commande):
    #rep = {'R': b'R', 'L': b'L', 'H': b'H'}
    #if commande in ['R', 'L', 'H']:
    arduino.write(commande)

# Envoyer la commande de déconnexion à l'Arduino pour arrêter les moteurs

def disconnectRobot(arduino):
    arduino.write(b'a')  # 'a' : Déconnexion de l'Arduino
    time.sleep(1)
    response = arduino.readline().decode('utf-8').strip()
    print("Réponse de déconnexion de l'Arduino :", response)

    # Fermer la liaison série
    arduino.close()
