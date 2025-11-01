from robot_class import Robot
from line_follower import decide_from_image
import picam_image
import cv2
from pythonRaspberry import *
from time import time, sleep
from corner_detection import locateIntersection
from datetime import datetime



i = int(time())

def supprimerImages():
    import os

    # Obtenir le répertoire actuel
    current_directory = os.getcwd()

    # Parcourir tous les fichiers du répertoire actuel
    for filename in os.listdir(current_directory):
        # Vérifier si le nom du fichier commence par "Inter"
        if filename.startswith("Inter"):
            # Construire le chemin complet du fichier
            file_path = os.path.join(current_directory, filename)
            # Vérifier que c'est bien un fichier (et non un dossier)
            if os.path.isfile(file_path):
                # Supprimer le fichier
                os.remove(file_path)

def main(mission):
    supprimerImages()
    robot = Robot(0, 0, initial_dir=2, mission=mission)
    
    if robot.mission == 'livraison':
        xGoal = int(input("[INPUT] Coordonnee x de l'objectif :"))
        yGoal = int(input("[INPUT] Coordonnee y de l'objectif :"))
        robot.goal_definition(xGoal, yGoal)
    
    print("[INFO] Lancement de la camera")
    cap = picam_image.lancement_camera()
    
    print("[INFO] Connexion a l'arduino")
    ##################################################
    # TODO : Connexion avec l'arduino (commande A12)
    arduino = connexionArduino()
    ##################################################
    print("[INFO] Connecte !")
    
    
    print("[INFO] Lancement du suivi de ligne")
    
    try :
        last = time()
        lastGauche, lastDroite = 0, 0
        timeToContinueSuiviDeLigne = 0
        #minTimeToDetectNewIntersection = 0
        intersectionDetectee = False
        lastPossibleDirections = [False, False, False]
        lastImage = None
        
        while True:
            current = time()
            #if current != last:
                #print('\rfps', round(1 / (current - last)), 'dt:', current - last, end='')
            last = current
            image = picam_image.obtain_image(cap)
            if lastImage is None:
                lastImage = image[:]
            w, h = image.shape[:2]

            #x, y = locateIntersection(image, False)
            #print('\nIntersection:', x, y)

            #avant = time()
            CUT = 0.3
            ans = decide_from_image(image, CUT)
            if ans is None:
                gauche = lastGauche
                droite = lastDroite
            else:
                (cx, cy), (min_x, max_x, min_y, max_y) = ans
                delta = (cx - 0.5) * 2 # Retourner la différence entre le centroïde et le centre de l'image

                if delta < 0:
                    gauche, droite = 1, (1 + delta)
                else:
                    gauche, droite = (1 - delta), 1

                possibleDirections = [False, False, False]
                if min_x < 0.1:
                    possibleDirections[0] = True
                if min_y < CUT + 0.05:
                    possibleDirections[1] = True
                if max_x > 0.9:
                    possibleDirections[2] = True

                #LIMITE_BASSE = 0.35
                LIMITE_HAUTE = 0.7
                height, width, _ = image.shape
                #cv2.line(image, (0, int(LIMITE_BASSE * height)), (width, int(LIMITE_BASSE * height)), (255, 0, 0), 2)
                cv2.line(image, (0, int(LIMITE_HAUTE * height)), (width, int(LIMITE_HAUTE * height)), (255, 0, 0), 2)
            
            #print(f'cy: {cy}, max_y: {max_y}')
            # S'il y a une intersection
            if timeToContinueSuiviDeLigne is None and cy < LIMITE_HAUTE and max_y > 0.85 and \
            lastGauche > 0.7 and lastDroite>0.7 and gauche>0.7 and droite>0.7 and \
               (min_x < 0.07 or max_x > 0.93):   
                print(f'NEW  Intersection {round(time(), 1)} with directions {possibleDirections}')
                intersectionDetectee = True
                
            else:
                # Pas d'intersectin détectée
                if intersectionDetectee:
                    print(f'STOP Intersection {round(time(), 1)} with directions {lastPossibleDirections}')
                    #sleep(0.15)
                    robot.switch_status('intersection')
                    now = datetime.now()

                    cv2.imwrite(f'Intersection {now.strftime("%H-%M-%S")} - {lastPossibleDirections}.png', lastImage)
                    envoiCommande(arduino, 0, 0, minSpeed=0, maxSpeed=200)
                    
                    ###################################################
                    # TODO Algo de choix de chemin


                    obstaclesDetectes = envoieIntersection(arduino)
                    print(f'obstacles detectes: {obstaclesDetectes}')
                    
                    if robot.mission == 'huit':
                        direction = robot.direction_choice(lastPossibleDirections)
                    else :
                        direction = robot.nextStepToGotoGoal(lastPossibleDirections, obstaclesDetectes)
                    print('Choix de direction :', direction)
                    if direction!=b'A':
                        print("coucou Arnaud")
                        envoieRotation(arduino, direction)
                    
                    ###################################################
                    
                    intersectionDetectee = False
                    timeToContinueSuiviDeLigne = time() + 2
            

            if timeToContinueSuiviDeLigne is not None:
                #print(f'    Intersection detected at {round(time(), 1)} with directions {possibleDirections}')

                '''if possibleDirections[0]:
                    cv2.line(image, (int(cx * w), int(cy * h)), (int(cx * w - 100), int(cy * h)), (255, 0, 0), 3)
                if possibleDirections[1]:
                    cv2.line(image, (int(cx * w), int(cy * h)), (int(cx * w), int(cy * h - 100)), (255, 0, 0), 3)
                if possibleDirections[2]:
                    cv2.line(image, (int(cx * w), int(cy * h)), (int(cx * w + 100), int(cy * h)), (255, 0, 0), 3)
                '''
                
                # Déterminer toutes les directions possibles
                if time() > timeToContinueSuiviDeLigne:
                    robot.switch_status('suivi_de_ligne')
                    #print(f"Final possible directions: {possibleDirections}")
                    timeToContinueSuiviDeLigne = None
                    #minTimeToDetectNewIntersection = time() + 1
                

            lastGauche, lastDroite = gauche, droite
            lastPossibleDirections = possibleDirections[:]
            lastImage = image[:]
            
            if robot.state == 'suivi_de_ligne':
                ##################################################
                response = envoiCommande(arduino, gauche, droite, minSpeed=80, maxSpeed=200)
                if response == "Demi-tour":
                    robot.direction = (robot.direction+2)%4
                    for i in range(1):
                        robot.moveBy(Robot.convertDirectionIntToVector(robot.direction))
                ##################################################
            
            cv2.imshow('Cam', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    except Exception as e:
        
        print(e)
        ###########################################
        disconnectRobot(arduino)
        picam_image.stop_Camera(cap) # Fermeture de la camera
        ###########################################


if __name__ == "__main__":
    print("[INFO] Lancement du programme")
    
    missionDirectory = {'0':'test', '1': 'huit', '2':'livraison'}
    
    print("[IFNO] Mission existante")
    
    for i in missionDirectory.keys():
        print(i, missionDirectory[i])
    
    missionKey = input('[INPUT] Choix de mission : ')
    while missionKey not in missionDirectory:
        print("[ERROR] Mission non codee")
        missionKey = input('[INPUT] Choix de mission : ')
        
    main(missionDirectory[missionKey])
