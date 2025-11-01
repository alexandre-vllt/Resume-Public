from robot_class import Robot
from line_follower import decide_from_image
import picam_image
import cv2
from pythonRaspberry import *
from time import time, sleep
from corner_detection import locateIntersection



i = int(time())

def main(mission):
    
    robot = Robot(0,0,mission=mission, priority=['R','A','L'])
    
    print("[INFO] Lancement de la camera")
    cap = picam_image.lancement_camera()
    
    print("[INFO] Connexion a l'arduino")
    ##################################################
    # TODO : Connexion avec l'arduino (commande A12)
    print('[COMMAND] Connexion a l arduino')
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
                if min_y < CUT + 0.1:
                    possibleDirections[1] = True
                if max_x > 0.9:
                    possibleDirections[2] = True

                #LIMITE_BASSE = 0.35
                LIMITE_HAUTE = 0.65
                height, width, _ = image.shape
                #cv2.line(image, (0, int(LIMITE_BASSE * height)), (width, int(LIMITE_BASSE * height)), (255, 0, 0), 2)
                cv2.line(image, (0, int(LIMITE_HAUTE * height)), (width, int(LIMITE_HAUTE * height)), (255, 0, 0), 2)
            
            #print(f'cy: {cy}, max_y: {max_y}')
            # S'il y a une intersection
            if timeToContinueSuiviDeLigne is None and cy < LIMITE_HAUTE and max_y > 0.85 and lastGauche > 0.7 and lastDroite>0.7 and gauche>0.7 and droite>0.7:
                print(f'NEW  Intersection {round(time(), 1)} with directions {possibleDirections}')
                intersectionDetectee = True
                
            else:
                # Pas d'intersectin détectée
                if intersectionDetectee:
                    print(f'STOP Intersection {round(time(), 1)} with directions {lastPossibleDirections}')
                    sleep(0.4)
                    robot.switch_status('intersection')
                    cv2.imwrite(f'Intersection {i} : {lastPossibleDirections}.png', lastImage)
                    print("[COMMAND] Stop le robot")
                    
                    ###################################################
                    # TODO Choisir la rotation
                    direction = robot.direction_choice(lastPossibleDirections)
                    print('Choix de direction :', direction)
                    if direction!='A':
                        print("[COMMAND] Envoie de la rotation")
                    
                    ###################################################
                    
                    #envoieIntersection(arduino)
                    intersectionDetectee = False
                    timeToContinueSuiviDeLigne = time() + 3
            

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
                    print(f"Final possible directions: {possibleDirections}")
                    timeToContinueSuiviDeLigne = None
                    #minTimeToDetectNewIntersection = time() + 1
                

            lastGauche, lastDroite = gauche, droite
            lastPossibleDirections = possibleDirections[:]
            lastImage = image[:]
            
            if robot.state == 'suivi_de_ligne':
                ##################################################
                # TODO : Lancer la commande
                pass
                ##################################################
            
            cv2.imshow('Cam', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    except Exception as e:
        
        print(e)
        ###########################################
        # TODO : lancer la commande de fin (a) pour que le robot arrete de tourner
        print("[COMMAND] Deconnexion")
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
