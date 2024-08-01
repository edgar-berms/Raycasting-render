import numpy as np

class Vecteur():
    def __init__(self,ori,ext):                     # Vecteur défini par 2 points origine et extrémité
        self.__origine = ori                        # origine et extremité sont des points défini par (x,y,z) et avec numpy
        self.__extremite = ext
        self.__vecteur = np.array([                 # On creer notre vecteur
            self.get_extremite[0] - self.get_origine[0],
            self.get_extremite[1] - self.get_origine[1],
            self.get_extremite[2] - self.get_origine[2]
        ])
        
    ##### Getter et Setter #####
    @property
    def get_origine(self):
        return self.__origine
    @property
    def get_extremite(self):
        return self.__extremite
    @property
    def get_vecteur(self):
        return self.__vecteur
    @get_origine.setter
    def set_origine(self,n):
        self.__origine = n
    @get_extremite.setter
    def set_extremite(self,n):
        self.__extremite = n
    
    @property
    def get_x(self):
        return self.__vecteur[0]
    @property
    def get_y(self):
        return self.__vecteur[1]
    @property
    def get_z(self):
        return self.__vecteur[2]
    @get_x.setter
    def set_x(self,n):
        self.__vecteur[0] = n
    @get_y.setter
    def get_y(self,n):
        self.__vecteur[1] = n
    @get_z.setter
    def get_z(self,n):
        self.__vecteur[2] = n
        
    def __add__(self,v2):
        '''
        Surcharge de l'opération d'addition pour les vecteurs
        '''
        x = self.get_vecteur[0] + v2.get_vecteur[0]
        y = self.get_vecteur[1] + v2.get_vecteur[1]
        z = self.get_vecteur[2] + v2.get_vecteur[2]
        return np.array([x,y,z])
    
    def __sub__(self,v2):
        '''
        Surcharge de l'opération de soustraction pour les vecteurs
        '''
        x = self.get_vecteur[0] - v2.get_vecteur[0]
        y = self.get_vecteur[1] - v2.get_vecteur[1]
        z = self.get_vecteur[2] - v2.get_vecteur[2]
        return np.array((x,y,z))
    
    def __mul__(self,n):
        '''
        Calcul le scalaire d'un vecteur par rapport à un entier ou float
        '''
        x = self.get_vecteur[0] * n
        y = self.get_vecteur[1] * n
        z = self.get_vecteur[2] * n
        return np.array((x,y,z))
    
    def __str__(self):
        '''
        Surcharge de l'opérateur d'affichage pour affichet le s composante du vecteur
        '''
        return f"({self.get_vecteur[0]},{self.get_vecteur[1]},{self.get_vecteur[2]})"
    
    def prod_scalaire(self,v2):
        '''
        Calcul du produit entre deux vecteurs
        '''
        # print(type(self.get_vecteur))
        # print(type(v2))
        prod_scal = np.dot(self.get_vecteur,v2.get_vecteur)
        return prod_scal
    
    def prod_vect(self,v):
        '''
        Calcul le produit vectorielle de deux vecteurs
        '''
        v1 = self.get_vecteur
        v2 = v.get_vecteur
        x = (v1[1]*v2[2])-(v1[2]*v2[1])
        y = (v1[2]*v2[0])-(v2[2]*v1[0])
        z = (v1[0]*v2[1])-(v1[1]*v2[0])
        return np.array((x,y,z))
    
    def norme_vect(self):
        '''
        Calcul la norme d'un vecteur
        '''
        norme = np.linalg.norm(self.get_vecteur)
        return norme
    
    def normalisation(self):
        '''
        Calcul le vecteur unitaire qui correspond à notre vecteur dans le self
        '''
        x = self.get_vecteur[0] / self.norme_vect()
        y = self.get_vecteur[1] / self.norme_vect()
        z = self.get_vecteur[2] / self.norme_vect()
        return np.array((x,y,z))
    