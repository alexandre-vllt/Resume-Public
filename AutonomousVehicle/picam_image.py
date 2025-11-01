'''
Obtention de l'image de la picamera2
'''

import cv2
import numpy as np
import cv2

# Importation de picamera2
try:
    from picamera2 import Picamera2
    os = 'rpi'
    print("[INFO] Raspberry pi detectee")
except:
    os = 'cp'



def lancement_camera(os = os):
    if os == 'rpi':
        cap = Picamera2()
    #    cap.preview_configuration.main.size = (1920,1080)
        #cap.preview_configuration.main.format = "RGB888"
        config = cap.create_still_configuration()
        config['main']['format'] = 'RGB888'
        config["main"]["size"] = (640, 480)
        cap.configure(config)

        # Désactiver l'exposition automatique
        
        camera_controls = {
        "AeEnable": False,
        "ExposureTime": 30000,  # Exemple : 10 000 microsecondes (ajustez selon vos besoins)
        "AnalogueGain": 4.0,     # Gain analogique de base (1.0 pour aucun gain supplémentaire)
        "Brightness": 0
        } # 30000 , 4.0 si lumiere et 80000 et 8.0 sans lumiere
        cap.set_controls(camera_controls)
        cap.set_controls({"AwbMode": 0, "ColourGains": (1.5, 1.5)})  # Ajustez les gains de couleur selon vos besoins
        print(cap.controls)
        
        cap.start()
    else :
        cap = cv2.VideoCapture(0)
    return cap


def obtain_image(cap):
    if os == 'rpi':
        image =  cap.capture_array()
    else :
        ret, image = cap.read()
    return image


def stop_Camera(cap):
    if os == "rpi":
        cap.stop()
    else:
        cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print('[INFO] Lancement de la Camera')
    cap = lancement_camera()
    
    print("[INFO] Test de la Camera")
    
    while True:
        image = obtain_image(cap)
        cv2.imshow('Cam', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    stop_Camera(cap)

