import numpy as np

##### Notre classe couleur que l'on initialise en rvb sur 255 et non normalisé #####

class Couleur():
    def __init__(self,r,v,b):
        self.__r = r
        self.__v = v
        self.__b = b
        self.__couleur = np.array([               
            self.get_r,            
            self.get_v,
            self.get_b
        ])
        
    ##### Getter et Setter #####    
    @property
    def get_r(self):
        return self.__r
    @property
    def get_v(self):
        return self.__v
    @property
    def get_b(self):
        return self.__b
    @property
    def get_couleur(self):
        return self.__couleur
    @get_r.setter
    def set_r(self,n):                         
        self.__r = n
    @get_v.setter
    def set_v(self,n):                        
        self.__v = n
    @get_b.setter
    def set_b(self,n):
        self.__b = n
        
    def __add__(self,c2):
        '''
        Mélange de deux couleurs
        '''
        r = (self.get_couleur[0] + c2.get_couleur[0]) // 2
        v = (self.get_couleur[1] + c2.get_couleur[1]) // 2
        b = (self.get_couleur[2] + c2.get_couleur[2]) // 2
        return np.array((r,v,b))                        # Si nos deux couleurs sont valides alors pas besoin de revérifier
    
    def __mul__(self,c2):
        '''
        Mélange de deux couleur par la multiplication
        '''
        self.set_r = self.get_r * c2.get_r
        self.set_v = self.get_v * c2.get_v
        self.set_b = self.get_b * c2.get_b
        
    def __str__(self):
        '''
        Surcharge de l'opérateur de sortie afin de connaitre les valeurs rvb de notre lumière
        '''
        return f"({self.get_r},{self.get_v},{self.get_b})"