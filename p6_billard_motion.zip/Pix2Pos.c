
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define BallminScore = 15;
#define nbParams = 29;


// structur qui permet de separer en 3 une variable , pour avoir les 3 couleurs: rouge (r), blanc (w) et jaune (y)
struct color {
    unsigned int r;
    unsigned int w;
    unsigned int y;
};

// On énonce nos deux fonctions au début du programme
void findcolor(int hh, int x, int w, unsigned int pixel, struct color pix[][hh], int RminRed, int RmaxRed,int GminRed,int GmaxRed, int BminRed,int BmaxRed,int RminY,int RmaxY,int GminY,int GmaxY,int BminY,int BmaxY ,int RminW,int RmaxW,int GminW,int GmaxW,int BminW,int BmaxW );

struct color colorball(  int coordx, int coordy,int hh, struct color pix[][hh], int BalleDiameter);

// Écris par Alexandre et Mahé 

int main(int argc, char * argv[]) {
    
    
    // si il n'y a pas le nombre de paramètre dans la ligne de commande
    if( argc != 30 ){
        fprintf(stderr, "il n'y a pas le nombre de paramètre dans la ligne de commande\n");
        return 3;
    }
    // recuperer les info
    
    // table billard coordonées
    
    int Lmin = atoi(argv[1]);
    int Lmax = atoi(argv[2]);
    int Cmin = atoi(argv[3]);
    int Cmax = atoi(argv[4]);
    
    // information balle rouge
    
    int RminRed = atoi(argv[5]);
    int RmaxRed = atoi(argv[6]);
    int GminRed = atoi(argv[7]);
    int GmaxRed = atoi(argv[8]);
    int BminRed = atoi(argv[9]);
    int BmaxRed = atoi(argv[10]);
    
    // information balle jaune
    
    int RminY = atoi(argv[11]);
    int RmaxY = atoi(argv[12]);
    int GminY = atoi(argv[13]);
    int GmaxY = atoi(argv[14]);
    int BminY = atoi(argv[15]);
    int BmaxY = atoi(argv[16]);
    
    // information balle blanche
    
    int RminW = atoi(argv[17]);
    int RmaxW = atoi(argv[18]);
    int GminW = atoi(argv[19]);
    int GmaxW = atoi(argv[20]);
    int BminW = atoi(argv[21]);
    int BmaxW = atoi(argv[22]);
    
    // information bleu
    
    int RminB = atoi(argv[23]);
    int RmaxB = atoi(argv[24]);
    int GminB = atoi(argv[25]);
    int GmaxB = atoi(argv[26]);
    int BminB = atoi(argv[27]);
    int BmaxB = atoi(argv[28]);
    
    // diamètre balle
    
    int BalleDiameter = atoi(argv[29]);
    
    // verification que le diamètre de la balle est valide
    if( BalleDiameter < 5 || BalleDiameter > 20){
        fprintf(stderr, "Erreur le diamètre de la balle est faux\n");
        return 5;
    }
    
    
    
    int Larg;
    int Haut;
    size_t n;
    // n le nombre de pixel lu
    
    unsigned int *pixmap = NULL;
    
    
    // ouverture du fichier Pixmap
    FILE *fp = fopen("pixmap.bin", "rb");
    
    // ouverture du fichier Pos
    FILE *fo = fopen("pos.txt", "w");
    
    // traitement des erreurs lors de l'ouvertures des fichiers
    if(fp == NULL){
        fprintf(stderr, "Erreur lors de l'ouverture du fichier de lecture\n");
        return 1;
    }
    if(fo == NULL){
        fprintf(stderr, "Erreur lors de l'ouverture du fichier d'écriture\n");
        return 1;
    }
    
    // récupération de la première donnée ( largeur )
    size_t pixel1 = fread(&Larg, sizeof(unsigned int),1,fp);
    
    // récupération de la deuxième donnée ( hauteur )
    size_t pixel2 = fread(&Haut, sizeof(unsigned int),1,fp);
    
    // traitement erreur cas où largeure ou hauteur n'est pas valide
    if (Larg<100 || Larg > 1000){
        fprintf(stderr, "erreur la largeur n'est pas valide\n");
        return 2;
    }
    
    if (Haut<100 || Haut > 1000){
        fprintf(stderr, "erreur la hauteur n'est pas valide\n");
        return 2;
    }
    
    // création de l'espace de stockage malloc
    pixmap = malloc(Larg*Haut*sizeof(unsigned int));
    
    if (pixmap == NULL){
        fprintf(stderr, "erreur de lors de la création du tableau  malloc\n");
        return 11;
    }
    // ESPACE DISPO ?


    // récuperation des données de toute les pixels
    n = fread(pixmap, sizeof(unsigned int),Larg*Haut,fp);
        

    // lecture d'un unsigned int pour atteindre la fin du fichier (normalement)
    fread(pixmap, sizeof(unsigned int),1,fp);



    // cas ou le nombre de pixel est inferieur aux dimensions du tableau (pixels manquantes)
    if (n < Larg*Haut){
        fprintf(stderr, "il y a pas assez de pixel\n");
        return 6;
    }

    // traitement erreur si il y atrop de pixel dans le fichier
    if (feof(fp)) {
    }else {
        fprintf(stderr, "warning il y a trop de pixel\n");
    }


    // inverser largeur hauteur Cmin Lmin
    int ll = Cmax - Cmin;
    int hh = Lmax - Lmin;


    // création du tableau deux dimensions ciblant les pixels et leur coordonnées dans la table de billard
    struct color Pix[ll][hh];
    int x, y ;


    // remplir le tableau avec un 1 si le pixel peut etre de la couleur et 0 sinon
    for(y=0 ; y < hh ; y++){
        for(x=0; x < ll ; x++){
            Pix[x][y].r =0;
            Pix[x][y].w =0;
            Pix[x][y].y =0;
            // pixmap[ Lmin*Larg + Cmin + x + y*Larg] permet de cibler tout les pixels de la table du billard sans faire traiter les autres pixels de l'image
            findcolor(hh,x,y,pixmap[ Lmin*Larg + Cmin + x + y*Larg], Pix, RminRed, RmaxRed, GminRed, GmaxRed,BminRed,BmaxRed, RminY, RmaxY, GminY, GmaxY, BminY, BmaxY ,  RminW, RmaxW, GminW, GmaxW,BminW,BmaxW);
        }
    }

    
    int coordx, coordy;
    struct color score;
    score.w = 0;
    score.y = 0;
    score.r = 0;
    struct color carre;
    struct color ballX;
    struct color ballY;
    
    // chercher la boule avec le meilleurs scores pour chaque couleur et ses coordonnées
    for(coordy = 0; coordy < hh - BalleDiameter ;  coordy++){
        for(coordx = 0; coordx < ll - BalleDiameter ; coordx++){
            carre = colorball( coordx, coordy,hh, Pix, BalleDiameter);
            if ( carre.w >  score.w){
                score.w = carre.w;
                ballX.w = coordx;
                ballY.w = coordy;
            }
            if ( carre.y >  score.y){
                score.y = carre.y;
                ballX.y = coordx;
                ballY.y = coordy;
            }
            if ( carre.r >  score.r){
                score.r = carre.r;
                ballX.r = coordx;
                ballY.r = coordy;
            }
        }
    }

        
    // je repasse en coordonnée de l'image
    ballX.r = ballX.r + Cmin;
    ballY.r = ballY.r + Lmin;

    ballX.y = ballX.y + Cmin;
    ballY.y = ballY.y + Lmin;

    ballX.w = ballX.w + Cmin;
    ballY.w = ballY.w + Lmin;

    // erreur pas de balle trouvé car score trop faible
    if (score.w < 15){
        score.w = 0;
        ballX.w = -1;
        ballY.w = -1;
        fprintf(stderr, "il manque la boule blanche\n");
    }
    if (score.y < 15){
        score.y = 0;
        ballX.y = -1;
        ballY.y = -1;
        fprintf(stderr, "il manque la boule jaune\n");
    }
    if (score.r < 15){
        score.r = 0;
        ballX.r = -1;
        ballY.r = -1;
        fprintf(stderr, "il manque la boule rouge\n");
    }

    // ecriture dans le fichier de sortie Pos
    fprintf(fo, "Red: %d, %d, %d\n", ballX.r, ballY.r, score.r);
    fprintf(fo, "Yellow: %d, %d, %d\n", ballX.y, ballY.y, score.y);
    fprintf(fo, "White: %d, %d, %d\n", ballX.w, ballY.w, score.w);
    
    
    // fermeture des fichiers
    fclose(fp);
    fclose(fo);

    // on libère l'espace de stockage
    free(pixmap);

    return 0;

}

// écris par alexandre
/**
 findcolor
 
 fonction qui dit si un pixel peut etre jaune, blanc ou rouge ( elle attribue 1 à la case du tableau si oui )
 
 On commence par recuperer les informations concernant chaque couleur en shiftant le pixel pour avoir seulement les bits qui nous intéresse
 Puis determine si le pixel peut etre de la couleur en question ( si il est dans les bornes prédefinie ou pas ). Si il peut etre de la couleur choisie, la valeur 1 est attribué à la case du tableau correspondant au pixel.
 
 Input
    hh : le nombre de colonne du tableau Pix
    x : la ligne du tabelau
    q: la colonne du tabelau
    pixel: la donnée de la pixel en question récupérée du fichier
    pix[][hh] : tableau caractérisant si les pixels peuvent etre d'un couleur ou pas
    RminRed, RmaxRed, GminRed ... : les bornes de validations des différentes couleurs
 output: les valeurs du tableau Pix[][] sont modifiés
 retourn : pas de return car il s'agit d'un void
 */

void findcolor(int hh, int x, int q, unsigned int pixel, struct color pix[][hh], int RminRed, int RmaxRed,int GminRed,int GmaxRed, int BminRed,int BmaxRed,int RminY,int RmaxY,int GminY,int GmaxY,int BminY,int BmaxY ,int RminW,int RmaxW,int GminW,int GmaxW,int BminW,int BmaxW ){
    unsigned int infoR = (pixel >>16) & 0xFF;
    unsigned int infoG = (pixel >>8 ) & 0xFF;
    unsigned int infoB = (pixel & 0xFF);
    if ( (RminW <= infoR) && (infoR<= RmaxW) && (GminW <= infoG) && (infoG<= GmaxW) && (BminW <= infoB ) && ( infoB<= BmaxW) ){
    pix[x][q].w = 1;
    }
    if ( (RminY <= infoR ) && (infoR <= RmaxY) && (GminY <= infoG) && (infoG <= GmaxY) && (BminY <= infoB) && ( infoB <= BmaxY) ){
    pix[x][q].y = 1;
    }
    if ( (RminRed <= infoR ) && (infoR <= RmaxRed) && (GminRed <= infoG ) && ( infoG <= GmaxRed) && (BminRed <= infoB) && ( infoB <= BmaxRed) ){
    pix[x][q].r = 1;
    }
}


// écris par mahe
// fonction qui calcule le score d'une boule de coordonée coordx coordy

/**
 colorball
 
 fonction qui calcule le score (des 3 couleurs) d'une boule dont les coordonées de la pixel en haut à gauche dans notre tableau est ( coordx ; coordy )
 
 On commence par initialiser les scores à 0. Puis à partir de la première pixel (en haut à gauche) on parcours tout le tableau dont les cases correspondent aux pixels de la boules.
 Soit le carré de Ballediameter de côté. Comme les cases valent 1 si elles peuvent être de la couleur et 0 sinon, il nous suffit d'additioner toute les cases séléctionnées pour obtenir le score.
 
 Input
    coordx: la coordonnée x de la pixel en haut à gauche de la ball testée
    coordy: la coordonnée y de la pixel en haut à gauche de la ball testée
    hh: le nombre de colonne du tableau Pix
    pix[][hh]: tableau caractérisant si les pixels peuvent etre d'un couleur ou pas
    Ballediameter: le diamètre d'une boule
 output
    score: le score de la balle ( c'est un struct color donc il a 3 composantes, une pour chaque couleur )
 */

struct color colorball( int coordx, int coordy, int hh, struct color pix[][hh], int BalleDiameter) {
    struct color score;
    score.w = 0 ;
    score.r =0 ;
    score.y = 0 ;
    for (int h=0 ; h < BalleDiameter ; h++){
        for(int l=0; l < BalleDiameter ; l++ ){
            score.w = score.w + pix[coordx + l][coordy + h].w ;
            score.r = score.r + pix[coordx + l][coordy + h].r ;
            score.y = score.y + pix[coordx + l][ coordy + h].y ;
        }
    }
    return score;
}
