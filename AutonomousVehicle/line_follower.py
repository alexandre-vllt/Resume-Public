import cv2
import numpy as np

def trouveContour(image, CUT):
    #print("FONCTION DECIDE FROM IMAGE:")
    #print("Dimensions de l'image :", w, h)

    # Découper la moitié inférieure de l'image

    
    h, w = image.shape[:2]
    half_image = image[int(h*CUT):, :]

    gray_image = cv2.cvtColor(half_image, cv2.COLOR_BGR2GRAY)

    # Définir un seuil pour détecter les zones très blanches
    # Par exemple, les pixels avec une intensité supérieure à 230 seront considérés comme "très blancs"
    _, mask = cv2.threshold(gray_image, 190, 255, cv2.THRESH_BINARY)

    # Utiliser le masque pour filtrer l'image

    #cv2.imshow('Image', mask)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Suppression du bruit
    kernel_erode = np.ones((6, 6), np.uint8)
    eroded_mask = cv2.erode(mask, kernel_erode, iterations=1)
    kernel_dilate = np.ones((4, 4), np.uint8)
    dilated_mask = cv2.dilate(eroded_mask, kernel_dilate, iterations=1)

    # Trouver les contours dans la moitié inférieure
    contours, hierarchy = cv2.findContours(dilated_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner tous les contours sur l'image d'origine pour visualisation
    for contour in contours:
        contour += np.array([0, int(h*CUT)])  # Ajouter h//2 à chaque point y du contour
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # Sauvegarder l'image avec les contours pour vérification
    #cv2.imwrite('out_Fabian_contour_vert.png', im2)
    #print("Nombre de contours trouvés :", len(contours))

    # Garder le plus grand contour
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

    # Calculer le centroïde pour le plus grand contour
    if len(contours) == 0:
        return None

    M = cv2.moments(contours[0])
    '''for contour in contours:
        contour += np.array([0, h // 2])  # Ajouter h//2 à chaque point y du contour
    cv2.polylines(image, contours, isClosed=True, color=(0, 170, 0), thickness=4)'''

    # Trouver le x le plus faible, le x le plus élevé et le y le plus faible parmi tous les points du contour
    min_x = min(contours[0], key=lambda point: point[0][0])[0][0]
    max_x = max(contours[0], key=lambda point: point[0][0])[0][0]
    min_y = min(contours[0], key=lambda point: point[0][1])[0][1]
    max_y = max(contours[0], key=lambda point: point[0][1])[0][1]

    # Calcul du centroïde
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00']) # Ajouter h//2 pour obtenir la position réelle dans l'image originale
    
    return (cx, cy), (min_x, max_x, min_y, max_y)

def decide_from_image(image, CUT):
    '''
    image: tableau numpy représentant l'image à traiter
    retourne: (gauche, droite), cyNormalised, possibleDirections
    '''
    
    h, w = image.shape[:2]
    #half_image = image[h//2:, :]  # On garde les pixels à partir de la moitié de la hauteur

    ans = trouveContour(image, CUT)
    if ans is None:
        print('Aucun centroide trouve')
        return None
    
    (cx, cy), (min_x, max_x, min_y, max_y) = ans

    # Dessiner un cercle au niveau du centroïde
    cv2.circle(image, (cx, cy), radius=10, color=(0, 0, 255), thickness=-1)  # Cercle rouge de rayon 5
        
    #cv2.imwrite('out_Fabian_controide.png', image)

    min_x /= w
    max_x /= w
    min_y /= h
    max_y /= h

    cx /= w
    cy /= h

    return (cx, cy), (min_x, max_x, min_y, max_y)
