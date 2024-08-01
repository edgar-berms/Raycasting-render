from couleur import *

class Lumiere():
    def __init__(self,x,y,z,couleur):
        self.__position = np.array([x,y,z])
        self.__couleur = couleur
        
        
    ##### Getter et setter ######
    @property
    def get_position(self):
        return self.__position
    @property
    def get_couleur(self):
        return self.__couleur
    @get_position.setter
    def set_position(self,x,y,z):
        self.__position = np.array([x,y,z])