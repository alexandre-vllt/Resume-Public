import cv2  # Importe la bibliothèque OpenCV pour la manipulation d'images
import numpy as np  # Importe NumPy pour les opérations sur les tableaux
from itertools import combinations






def showImg(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def locateIntersection(img, showWindow):
    FINAL_IMAGE = img


    if  showWindow: showImg(img)

    # Appliquer un flou pour réduire le bruit
    blur = cv2.blur(img, (6, 6))  # Applique un flou (moyenne) de 6x6 sur l'image

    # Convertir l'image en binaire avec un seuil fixe
    ret, thresh1 = cv2.threshold(blur, 168, 255, cv2.THRESH_BINARY)  # Seuil pour isoler les pixels clairs
    hsv = cv2.cvtColor(thresh1, cv2.COLOR_RGB2HSV)  # Convertit l'image binaire en espace de couleur HSV

    # Définir la plage de couleur blanche en HSV
    lower_white = np.array([0, 0, 168])  # Valeurs minimales pour la couleur blanche
    upper_white = np.array([172, 111, 255])  # Valeurs maximales pour la couleur blanche

    # Appliquer un masque pour extraire les pixels dans la gamme blanche
    mask = cv2.inRange(hsv, lower_white, upper_white)  # Crée un masque pour les pixels blancs

    # Suppression du bruit par érosion et dilatation
    kernel_erode = np.ones((6, 6), np.uint8)  # Crée un noyau de 6x6 pour l'érosion
    eroded_mask = cv2.erode(mask, kernel_erode, iterations=1)  # Applique l'érosion pour réduire le bruit
    kernel_dilate = np.ones((4, 4), np.uint8)  # Crée un noyau de 4x4 pour la dilatation
    dilated_mask = cv2.dilate(eroded_mask, kernel_dilate, iterations=5)  # Applique la dilatation pour restaurer la forme

    # Convertir l'image dilatée en niveaux de gris pour la détection de coins
    gray = np.float32(dilated_mask)  # Convertit le masque dilaté en format float32 pour cornerHarris

    if  showWindow: showImg(gray)

    # Détection de coins avec l'algorithme de Harris
    dst = cv2.cornerHarris(gray, 7, 3, 0.06)  # Détecte les coins avec un bloc de 5x5, une aperture de 3 et un k de 0.10


    # Détection de caractéristiques/corners forts avec l'algorithme GoodFeaturesToTrack
    corners = cv2.goodFeaturesToTrack(gray, 5, 0.5, 20)  # Détecte jusqu'à 5 coins avec une qualité min de 0.5 et une distance de 20 entre eux

    if corners is None or len(corners) == 0:
        print("No corners found")
        return None, None
    
    corners = np.int0(corners)  # Convertit les coordonnées des coins en entiers

    # Boucle pour afficher les coordonnées des coins détectés et les marquer sur l'image
    for i in corners: 
        x, y = i.ravel()  # Récupère les coordonnées x et y du coin
        print(x, y)  # Affiche les coordonnées du coin
        cv2.circle(FINAL_IMAGE, (x, y), 3, 255, -1)  # Dessine un petit cercle blanc (rayon 3) sur chaque coin détecté

    # Dilatation de l'image de coins pour faciliter la visualisation des coins marqués (optionnel)
    dst = cv2.dilate(dst, None)

    # Enregistre l'image avec les coins marqués
    #cv2.imwrite('out_test.png', img)

    # Applique un seuil sur les coins détectés pour marquer les coins les plus forts en rouge
    #img[dst > 0.001 * dst.max()] = [0, 0, 255]  # Marque les coins forts en rouge sur l'image

    # Afficher l'image (décommenter pour visualiser)
    """cv2.imshow('dst', img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()"""


    ##########

    maxDstValue = np.max(dst)


    '''liste = []
    for y in range(dst.shape[0]):  # Parcourir les lignes
        for x in range(dst.shape[1]):  # Parcourir les colonnes
            liste.append(dst[y, x] / maxDstValue)

    found = []
    for elt in liste:
        if elt in found:
            continue
        print('elt', elt)
        found.append(elt)'''

    #########

    # Normaliser les valeurs de dst pour les afficher
    dst_norm = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)
    dst_norm = np.uint8(dst_norm)

    
    if  showWindow: showImg(dst_norm)

    # Définir les seuils
    threshold_min = 20  # Par exemple, seuil minimum
    threshold_max = 100  # Par exemple, seuil maximum

    # Appliquer les couleurs conditionnelles
    dst_thresholded = np.uint8(np.where(dst_norm < threshold_min, 0,       # Noir foncé
                    np.where(dst_norm > threshold_max, 255,    # Blanc parfait
                    128)))                                      # Gris moyen

    # Définir le facteur de réduction

    
    if  showWindow: showImg(dst_thresholded)

    # Vérifier si le nombre de lignes et de colonnes est impair, et ajuster si nécessaire
    '''if dst_thresholded.shape[0] % 5 != 0:  # Si le nombre de lignes est impair
        dst_thresholded = dst_thresholded[:-1, :]  # Supprimer la dernière ligne

    if dst_thresholded.shape[1] % 5 != 0:  # Si le nombre de colonnes est impair
        dst_thresholded = dst_thresholded[:, :-1]  # Supprimer la dernière colonne'''

    # Créer une image réduite avec la moitié des dimensions
    REDUCTION_FACTOR = 13

    reduced_height = dst_thresholded.shape[0] // REDUCTION_FACTOR
    reduced_width = dst_thresholded.shape[1] // REDUCTION_FACTOR
    reduced_image = np.zeros((reduced_height, reduced_width), dtype=np.uint8)

    # Parcourir l'image par groupes de 2x2 pixels
    for i in range(0, dst_thresholded.shape[0] // REDUCTION_FACTOR * REDUCTION_FACTOR, REDUCTION_FACTOR):
        for j in range(0, dst_thresholded.shape[1] // REDUCTION_FACTOR * REDUCTION_FACTOR, REDUCTION_FACTOR):
            # Extraire les valeurs des pixels dans le groupe de 2x2
            pixels = dst_thresholded[i:i+REDUCTION_FACTOR, j:j+REDUCTION_FACTOR].flatten()

            # Appliquer les règles de couleur
            if 255 in pixels:
                reduced_pixel = 255  # Blanc parfait si un pixel est blanc
            elif 0 in pixels:
                reduced_pixel = 0    # Noir foncé si un pixel est noir
            else:
                reduced_pixel = 128  # Gris moyen si tous les pixels sont gris

            # Affecter la couleur au pixel réduit
            reduced_image[i//REDUCTION_FACTOR, j//REDUCTION_FACTOR] = reduced_pixel


    whitePixelCoordinates = [(x, y) for x in range(reduced_image.shape[0]) for y in range(reduced_image.shape[1]) if reduced_image[x, y] == 255]
    clusters = [] # each clusster is a list of its pixels
    for i in range(len(whitePixelCoordinates)):
        found = False
        for cluster in clusters:
            for whitePixel in cluster:
                if abs(whitePixel[0] - whitePixelCoordinates[i][0]) <= 1 and abs(whitePixel[1] - whitePixelCoordinates[i][1]) <= 1:
                    cluster.append(whitePixelCoordinates[i])
                    found = True
                    break
            if found:
                break
        else:
            clusters.append([whitePixelCoordinates[i]])


    clusterCentroids = []
    for cluster in clusters:
        x = 0
        y = 0
        for whitePixel in cluster:
            x += whitePixel[0]
            y += whitePixel[1]
        clusterCentroids.append((x//len(cluster), y//len(cluster)))

    MAX_DIST_X = 3
    MAX_DIST_Y = 4
    intersections = [] # contient ((x,y), closePoints)



    # Générer toutes les combinaisons de 4 éléments
    for SIZE in (4, 3, 2):
        # Filtrer les clusterCentroids pour exclure ceux présents dans intersections
        remainingClusterCentroids = [centroid for centroid in clusterCentroids if centroid not in [point for _, points in intersections for point in points]]

        combinaisons = list(combinations(remainingClusterCentroids, SIZE))

        # Afficher les combinaisons
        for comb in combinaisons:
            superCentroidX = sum([centroid[0] for centroid in comb]) // SIZE
            superCentroidY = sum([centroid[1] for centroid in comb]) // SIZE

            for centroid in comb:
                if abs(centroid[0] - superCentroidX) > MAX_DIST_X or abs(centroid[1] - superCentroidY) > MAX_DIST_Y:
                    break
            else:
                intersections.append(((superCentroidX, superCentroidY), comb))
                break


            

    # Redimensionner l'image pour afficher chaque pixel comme un carré
    # Définir le facteur d'agrandissement pour créer une grille
    AUGMENTING_FACTOR = REDUCTION_FACTOR  # Ajuste ce facteur pour la taille de la grille

    # Calculer la nouvelle taille de l'image avec des "carrés" pour chaque pixel
    new_width = reduced_image.shape[1] * AUGMENTING_FACTOR
    new_height = reduced_image.shape[0] * AUGMENTING_FACTOR
    new_size = (new_width, new_height)

    # Redimensionner l'image pour créer la grille de pixels
    grid_image = cv2.resize(reduced_image, new_size, interpolation=cv2.INTER_NEAREST)

    # Convertir l'image réduite en couleur (BGR)
    grid_image_color = cv2.cvtColor(grid_image, cv2.COLOR_GRAY2BGR)

    # Dessiner un cercle rouge au centre de chaque centroïde de chaque cluster
    for centroid in clusterCentroids:
        center_x = centroid[1] * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
        center_y = centroid[0] * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
        cv2.circle(FINAL_IMAGE, (center_x, center_y), AUGMENTING_FACTOR // 2, (0, 0, 255), -1)

    for (x,y), closePoints in intersections:
        center_x = y * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
        center_y = x * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
        cv2.circle(FINAL_IMAGE, (center_x, center_y), AUGMENTING_FACTOR // 2, (0, 255, 0), -1)
        for closePoint in closePoints:
            close_x = closePoint[1] * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
            close_y = closePoint[0] * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
            cv2.line(FINAL_IMAGE, (center_x, center_y), (close_x, close_y), (0, 255, 0), 2)

        # Dessiner un cercle bleu centré sur chaque intersection
        for (x, y), closePoints in intersections:
            center_x = y * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2
            center_y = x * AUGMENTING_FACTOR + AUGMENTING_FACTOR // 2

            # Dessiner une ligne horizontale en bleu
            cv2.line(FINAL_IMAGE, 
                    (center_x - MAX_DIST_X * AUGMENTING_FACTOR // 2, center_y), 
                    (center_x + MAX_DIST_X * AUGMENTING_FACTOR // 2, center_y), 
                    (255, 0, 0), 2)
        
            # Dessiner une ligne verticale en bleu
            cv2.line(FINAL_IMAGE, 
                    (center_x, center_y - MAX_DIST_Y * AUGMENTING_FACTOR // 2), 
                    (center_x, center_y + MAX_DIST_Y * AUGMENTING_FACTOR // 2), 
                    (255, 0, 0), 2)
            
            cv2.putText(FINAL_IMAGE, str(len(closePoints)), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(FINAL_IMAGE, str(len(closePoints)), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)



    # Afficher l'image sous forme de grille de pixels avec les points rouges
    if showWindow: showImg(FINAL_IMAGE)

    for (x, y), closePoints in intersections:
        if len(closePoints) == 4:
            return x, y

    return None, None


if __name__ == '__main__':
    # Charger l'image depuis un fichier
    filename = 'tests_Fabian/test_traitement_image/photo_carrefour2.jpg'
    img = cv2.imread(filename)  # Lit l'image spécifiée

    locateIntersection(img, showWindow=True)