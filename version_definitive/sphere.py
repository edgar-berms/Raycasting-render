from objet import *

class Sphere(Objet):
    def __init__(self,x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,ombre,rayon):
        super().__init__(x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,ombre)
        self.__rayon = rayon
        
    
    ##### Getter et setter ######
    @property
    def get_rayon(self):
        return self.__rayon
    @get_rayon.setter
    def set_rayon(self,n):
        self.__rayon = n
        
    # Implemente les methodes virtuelles 
    def intersection(self,vecteur_directeur,emplacement_camera,pixel):
        '''
        Méthode pour trouver si notre sphère a un point d'intersection avec le notre vecteur
        '''
        b = 2 * np.dot(vecteur_directeur, emplacement_camera - self.get_position)
        c = np.linalg.norm(emplacement_camera - self.get_position) ** 2 - self.get_rayon ** 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        elif delta == 0:
            t = -b / 2
            return t
        else: 
            return None
            
    def normale(self, vecteur_directeur,emplacement_camera,pixel):
        '''
        Méthode pour trouver notre point d'intersection ainsi que la normale à ce point d'intersection
        '''
        pt_inter = emplacement_camera + self.intersection(vecteur_directeur,emplacement_camera,pixel) * vecteur_directeur
        normale = Vecteur(self.get_position,pt_inter)
        normale_normalise = normale.normalisation()
        return pt_inter,normale_normalise
        
        