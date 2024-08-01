from objet import *

class Plan(Objet):
    def __init__(self,x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,ombre,normalex,normaley,normalez):
        super().__init__(x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,ombre)
        self.__normale = np.array([normalex,normaley,normalez])
        
    
    ##### Getter et setter ######
    @property
    def get_normale(self):
        return self.__normale
    @get_normale.setter
    def set_normale(self,x,y,z):
        self.__normale = np.array([x,y,z])
        
    def eq_plan(self):
        '''
        On essaye de trouver l'equation paramètrique du plan
        Ax + By + Cz + D = 0
        On trouve le D qui va nous servir pour la suite des opérations
        '''
        D = self.get_normale[0] * self.get_x + self.get_normale[1] * self.get_y + self.get_normale[2] * self.get_z
        return -D
        
    # Implemente les methodes virtuelles 
    def intersection(self,vecteur_directeur,focale_position,pixel):
        '''
        Pour trouver une intersection entre notre vecteur et notre plan et son paramètre si il y en a un
        '''
        num = -((self.get_normale[0] * pixel[0]) + (self.get_normale[1] * pixel[1]) + (self.get_normale[2] * pixel[2]) + self.eq_plan())
        denum = (self.get_normale[0] * vecteur_directeur[0]) + (self.get_normale[1] * vecteur_directeur[1]) + (self.get_normale[2] * vecteur_directeur[2])
        if (denum == 0):
            return None
        else:
            t = num / denum
            if t > 0:
                return t
    
    def normale(self,vecteur_directeur,emplacement_camera,pixel):
        '''
        Méthode pour trouver notre point d'intersection ainsi que la normale qui lui est attachée
        '''
        if(self.intersection(vecteur_directeur,emplacement_camera,pixel) is not None):
            point_intersection = pixel + self.intersection(vecteur_directeur,emplacement_camera,pixel) * vecteur_directeur
            normale = Vecteur(self.get_position,point_intersection)
            normale_normalise = normale.normalisation()
            return point_intersection,normale_normalise