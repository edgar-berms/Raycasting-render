from camera import *
from lumiere import *
from objet import *
from PIL import Image

class Scene():
    def __init__(self,cam,objs,lumieres,lumiere_amb):
        self.__camera = cam
        self.__objets = objs
        self.__lumieres = lumieres
        self.__lumiere_ambiante = lumiere_amb
    
    @property
    def get_cam(self):
        return self.__camera
    @property
    def get_objets(self):
        return self.__objets 
    @property
    def get_lumieres(self):
        return self.__lumieres
    @property
    def get_lumieres_ambiante(self):
        return self.__lumiere_ambiante 
    
    def texture_mur(self,objet,pixel):
        '''
        Fonction pour changer la couleur de l'objet afin d'appliquer une texture de mur
        Ce n'est pas une vrai texture mais plus un changement régulier de couleur d'un même objet pour faire penser à une texture
        '''
        if(pixel[1] % 25 == 0 or pixel[0] % 50 == 0):
            # Affiche une couleur blanche
            objet.get_couleur.set_r = 255
            objet.get_couleur.set_v = 255
            objet.get_couleur.set_b = 255
        else:
            # Affiche une couleur rouge
            objet.get_couleur.set_r = 150
            objet.get_couleur.set_v = 0
            objet.get_couleur.set_b = 0
          
    
    def raytracing(self,ecran,profondeur):
        '''
        Méthode principale qui créer le raytracing
        '''
        liste_img = []
        for i, y in enumerate(np.linspace(ecran[1], ecran[3], self.get_cam.get_h)):
            for j, x in enumerate(np.linspace(ecran[0], ecran[2], self.get_cam.get_l)):
                # Ici i, y in enumerate(np.linspace(ecran[1], ecran[3], cam.get_h)) crée cam.get_h élément entre l'intervalle ecran[1] et ecran[3]
                # par exemple, si ecran[1] = 0 et ecran[3] = 10 et cam.get_h = 10 on aura donc [1,2,3,4,5,6,...]
                # et i,j sont les indices de notre liste d'intervalle si i = 0 alors il retournera 1 si on reste dans notre exemple
                pixel = np.array([x, y, 0])
                focale_position = np.array([self.get_cam.get_x,self.get_cam.get_y,self.get_cam.get_z + self.get_cam.get_distance_focale])
                # Ici notre vecteur directeur de notre point que l'on normalise par la suite
                vect = Vecteur(focale_position,pixel)
                vect_normalise = vect.normalisation()
                
                # On initialise quelques données en dehors des boucles pour pouvoir les réutiliser par la suite
                min_distance = np.inf
                objet_plus_proche = None
                point_intersection_decale = None
                bonne_normale = None
                bon_point_intersection = None
                ombrage = False
                c = np.zeros((3))
                couleur = Couleur(0,0,0)
                reflexion = 1
                
                # Boucle pour connaitre le nombre de "rebonds" que l'on fait 
                for k in range(profondeur):
                    # Pour chaque objet de notre scène
                    for objet in self.get_objets:
                        # On regarde si il y a une intersetion entre notre objet courant et notre vecteur
                        if(objet.intersection(vect_normalise,focale_position,pixel) is not None):
                            # Si il y a une intersection alors on calcule le point d'intersection ainsi que le normale
                            point_intersection,normale = objet.normale(vect_normalise,focale_position,pixel)
                            # On calcule la distance entre notre focale et notre point d'intersection afin de connaitre plus tard quel est l'objet le plus proche
                            distance = np.linalg.norm(point_intersection - focale_position)
                            # On cherche la plus petite distance et on mets à jour nos valeurs qui vont nous servir
                            if(distance < min_distance):
                                min_distance = distance
                                objet_plus_proche = objet
                                bonne_normale = normale
                                bon_point_intersection = point_intersection
                       
                    # Si il y a un objet plus proche ca veut dire qu'il y a une intersection entre notre rayon et un objet de la scène              
                    if(objet_plus_proche is not None):  
                        # Alors on créer un point d'intersection légérement décalé afin de pour la suite pourvoir avoir les ombres porté de l'objet
                        point_intersection_decale = bon_point_intersection + 1e-5 * bonne_normale    
                        # On créer une liste d'ombre à vide pour stocker les booléen des ombres 
                        liste_ombre = []  
                        # Pour chaque lumière de notre scène
                        for lumiere in self.get_lumieres:
                            # On part du principe qu'il n'y a pas d'ombre
                            ombrage = False
                            # On calcule le vecteur directeur entre notre point d'intersection décalé et notre source lumineuse pour pouvoir créer les ombres
                            intersection_lumiere = Vecteur(point_intersection_decale,lumiere.get_position)
                            # On le normalise
                            intersection_lumiere_normalise = intersection_lumiere.normalisation()
                            # On calcule la distance entre notre point d'intersection et la lumière
                            distance_intersection_lumiere = np.linalg.norm(lumiere.get_position - point_intersection_decale)
                            distance_min_bis = np.inf
                            for objet in self.get_objets:
                                if(objet.intersection(intersection_lumiere_normalise,point_intersection_decale,pixel) is not None):
                                    # On cherche les coordonnees de notre point obstacle 
                                    point_intersection_bis,_ = objet.normale(intersection_lumiere_normalise,point_intersection_decale,pixel)
                                    # On cherche la distance entre notre point intersection et notre point intersection obstacle
                                    distance_bis = np.linalg.norm(point_intersection_bis - bon_point_intersection)
                                    # On essaye de trouver ici le point d'intersection dont la distance est la plus courte
                                    if(distance_bis < distance_min_bis):
                                        distance_min_bis = distance_bis
                            # On se place dans la situation ou il y a bien une intersection mais que notre objet qui intersecte est derriere notre source lumineuse
                            # alors ici notre point intersection sera bien eclaire
                            # Notre point intersection                        Notre source lumineuse            Un autre objet
                            #       °-------------------------------------------------°------------------------------° 
                            if(distance_min_bis < distance_intersection_lumiere):
                                # Il n'est pas eclaire
                                ombrage = True
                            # On ajoute le bool d'ombrage dans 
                            liste_ombre.append(ombrage)
                        
                        # Si tous les éléments de notre liste sont True alors ombrage sera a True
                        # ce qui veut dire qu'il faut que le point soient ombragé quelque soit la lumière sinon ombrage sera à False   
                        ombrage = all(liste_ombre)
                        
                        # Si ombrage est à False alors notre pixel est éclairé et doit être illuminé            
                        if(ombrage == False):
                            # On calcul notre vecteur entre le point d'intersection et notre focale pour la lumière spéculaire
                            intersection_camera = Vecteur(bon_point_intersection,focale_position)
                            intersection_camera_normalise = intersection_camera.normalisation()
                            reflet_speculaire = (intersection_lumiere_normalise + intersection_camera_normalise)
                            reflet_speculaire_normalise = reflet_speculaire / np.linalg.norm(reflet_speculaire)
                            brillance = 100
                            
                            # Si notre objet à une "texture" alors on l'applique ici
                            if (objet_plus_proche.get_texture == True):
                                pixel_alt = np.array([int(pixel[0] * (300*200)),int(pixel[1] * (300*200)),0])
                                self.texture_mur(objet_plus_proche,pixel_alt)
                            
                            # On créer une variable éclairage qui prends la couleur de notre objet le plus proche
                            eclairage = np.array([objet_plus_proche.get_couleur.get_r/255,objet_plus_proche.get_couleur.get_v/255,objet_plus_proche.get_couleur.get_b/255])
                            
                            # Eclairage ambiant
                            eclairage = self.get_lumieres_ambiante + eclairage
                            
                            # Eclairage diffus
                            eclairage = objet_plus_proche.get_fact_reflex_diffu * np.dot(intersection_lumiere_normalise, bonne_normale) + eclairage
                            
                            # Eclairage spéculaire
                            eclairage = objet_plus_proche.get_fact_reflex_spec * np.dot(bonne_normale, reflet_speculaire_normalise) ** (brillance / 4) + eclairage
                            
                            # Eclairage réféchi
                            c =  reflexion * eclairage + c
                            
                            # np.clip va mettre la valeur de c à 0 ou 1 si elle dépasse avant 0 ou après 1, pratique pour la lumière spéculaire
                            c_mod = np.clip(c, 0, 1)
                            
                            # On transforme notre couleur qui était normalisé en valeur entre 0 et 255 
                            couleur.set_r = c_mod[0]*255
                            couleur.set_v = c_mod[1]*255
                            couleur.set_b = c_mod[2]*255
                            
                            # On change notre position de focale ainsi que le vecteur directeur afin de boucler sur les bonnes valeurs                            
                            focale_position = point_intersection_decale
                            vect_normalise = vect_normalise - 2 * np.dot(vect_normalise,bonne_normale) * bonne_normale
                            
                            # On change aussi notre valeur de reflexion
                            reflexion = objet_plus_proche.get_fact_reflet * reflexion
                  
                # On ajoute dans une liste l'emplacement de notre pixel ainsi que le couleur qui lui correspond   
                liste_img.append([(i,j),couleur])   
        # On retourne la liste                                                                       
        return liste_img
    
    def afficher(self,longeur,hauteur,ecran,profondeur):
        '''
        Créer un fichier image de notre scène avec le rendu qui va bien
        '''
        # Créer un écran virtuel vide (avec des pixels noirs)
        ecran_virtuelle = np.zeros((hauteur, longeur, 3), dtype=np.uint8)

        # Liste_image est de la forme [position, couleur]
        liste_img = self.raytracing(ecran,profondeur)
        # Mettre à jour l'écran virtuel avec les couleurs des pixels intersectés par le raycasting
        for (x, y), couleur in liste_img:
            ecran_virtuelle[x,y] = (couleur.get_r,couleur.get_v,couleur.get_b)  # Modifier la couleur du pixel

        # Convertir le tableau numpy en image PIL
        image = Image.fromarray(ecran_virtuelle)

        # Enregistrer l'image avec PIL
        image.save("chapeau.png")
    
    