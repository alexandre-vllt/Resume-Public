from __future__ import division
import cv2
import numpy as np

# Chargement de l'image d'entrée
image = cv2.imread("/Users/fabianarfire/Desktop/EI ST5/test_traitement_image/photo_carrefour2.jpg")
h, w = image.shape[:2]
print("Dimensions de l'image :", w, h)

# Découper la moitié inférieure de l'image
half_image = image[h//2:, :]  # On garde les pixels à partir de la moitié de la hauteur

# Appliquer le flou sur la moitié inférieure de l'image
blur = cv2.blur(half_image, (5, 5))

# Appliquer un seuil binaire
ret, thresh1 = cv2.threshold(blur, 168, 255, cv2.THRESH_BINARY)
hsv = cv2.cvtColor(thresh1, cv2.COLOR_RGB2HSV)

# Définir la plage de couleurs pour le blanc
lower_white = np.array([0, 0, 150])
upper_white = np.array([172, 130, 255])

# Appliquer le masque pour détecter les pixels blancs
mask = cv2.inRange(hsv, lower_white, upper_white)

# Suppression du bruit
kernel_erode = np.ones((6, 6), np.uint8)
eroded_mask = cv2.erode(mask, kernel_erode, iterations=1)
kernel_dilate = np.ones((4, 4), np.uint8)
dilated_mask = cv2.dilate(eroded_mask, kernel_dilate, iterations=1)

# Trouver les contours dans la moitié inférieure
contours, hierarchy = cv2.findContours(dilated_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner tous les contours sur l'image d'origine pour visualisation
im2 = cv2.drawContours(half_image.copy(), contours, -1, (0, 255, 0), 3)

# Sauvegarder l'image avec les contours pour vérification
cv2.imwrite('out_test_half_Fabian.png', im2)
print("Nombre de contours trouvés :", len(contours))

# Garder le plus grand contour
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

# Calculer le centroïde pour le plus grand contour
if len(contours) > 0:
    M = cv2.moments(contours[0])
    # Calcul du centroïde
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00']) + h // 2  # Ajouter h//2 pour obtenir la position réelle dans l'image originale
    print("Centroïde de la plus grande zone dans la moitié inférieure : ({}, {})".format(cx, cy))

    # Dessiner un cercle au niveau du centroïde
    cv2.circle(image, (cx, cy), radius=10, color=(0, 0, 255), thickness=-1)  # Cercle rouge de rayon 5
else:
    print("Aucun centroïde trouvé")

# Sauvegarder l'image avec le cercle du centroïde
cv2.imwrite('out_test_with_centroid_Fabian.png', image)
