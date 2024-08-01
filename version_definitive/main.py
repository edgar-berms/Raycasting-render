from couleur import *
from sphere import *
from scene import *
from plan import *
from triangle import *

LONGEUR = 600
HAUTEUR = 400
PROFONDEUR = 1
RATIO = LONGEUR/HAUTEUR
ECRAN = (-1,1/RATIO,1,-1/RATIO)

if __name__ == "__main__":
    
    # ##### Test des couleurs #####
    rouge = Couleur(255,0,0)
    blanc = Couleur(255,255,255)
    violet = Couleur(255,0,255)
    gris = Couleur(145,145,145)
    marron = Couleur(88,44,0)
    bleu = Couleur(0,0,200)
    vert = Couleur(0,180,0)
    noir = Couleur(0,0,0)
    
    ##### Test des plans #####
    sol = Plan(0,-5,0,vert,np.array([0.25,0.2,0.1]),np.array([1,1,1]),0.25,False,0,1,0)  
    #mur = Plan(0,0,-10,gris,np.array([0.25,0.2,0.1]),np.array([1,1,1]),0.25,True,0,0,1)
    
    ##### Test des sphères #####
    sphr1 = Sphere(0, 0, -1.1,rouge,np.array([0.25,0.5,0.1]),np.array([1,1,1]),0.25,False,0.7)
    #sphr2 = Sphere(1.5,0.5,-2.5,violet,np.array([0.1,0,0.4]),np.array([1,1,1]),0.25,False,0.25)
    sphr3 = Sphere(-0.2,0.2,-0.5,blanc,np.array([0.25,0.2,0.1]),np.array([0.1,0.1,0.1]),0.1,False,0.1)
    sphr4 = Sphere(0.2,0.2,-0.5,blanc,np.array([0.25,0.2,0.1]),np.array([0.1,0.1,0.1]),0.1,False,0.1)
    sphr5 = Sphere(-0.175,0.2,-0.4,noir,np.array([0.25,0.2,0.1]),np.array([0.1,0.1,0.1]),0.1,False,0.05)
    sphr6 = Sphere(0.175,0.2,-0.4,noir,np.array([0.25,0.2,0.1]),np.array([0.1,0.1,0.1]),0.1,False,0.05)
    
    ##### Test des triangles #####
    p1 = np.array([0,1,-1])
    p2 = np.array([1,0.6,-1])
    p3 = np.array([-1,0.6,-1])
    tri1 = Triangle(0,1,-1,bleu,np.array([0,0.1,0.5]),np.array([1,1,1]),0.25,False,0,0,1,p1,p2,p3)
    p4 = np.array([0,-0.25,-0.25])
    p5 = np.array([0.25,-0.15,-0.25])
    p6 = np.array([-0.25,-0.15,-0.25])
    tri2 = Triangle(0,-0.5,-0.25,blanc,np.array([0,0.1,0.5]),np.array([1,1,1]),0.25,False,0,0,1,p4,p5,p6)
    
    ##### Test des lumières #####
    #lumiere1 = Lumiere(5,5,5,blanc)
    lumiere2 = Lumiere(0,5,3,blanc)
    
    ##### Test des notre caméra #####
    cam = Camera(LONGEUR,HAUTEUR,0,0,0,None,None,1)
    
    ##### Test de notre scene #####
    objets = [sphr1,sol,tri1,sphr3,sphr4,sphr5,sphr6,tri2]
    lumieres = [lumiere2]
    scn = Scene(cam,objets,lumieres,np.array([0.2,0,0]))
    
    # On affiche notre scène
    scn.afficher(LONGEUR,HAUTEUR,ECRAN,PROFONDEUR)