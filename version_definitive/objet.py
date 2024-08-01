from couleur import *
from vecteur import *
from abc import ABC,abstractmethod

class Objet():
    def __init__(self,x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,texture):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__position = np.array([x,y,z])
        self.__couleur = couleur
        self.__fact_reflex_diffu = fact_reflex_diffu
        self.__fact_reflex_spec = fact_reflex_spec
        self.__fact_reflet = fact_reflet
        self.__texture = texture
    
    
    ##### Getter et setter #####
    @property
    def get_x(self):
        return self.__x
    @property
    def get_y(self):
        return self.__y
    @property
    def get_z(self):
        return self.__z
    @property
    def get_position(self):
        return self.__position
    @property
    def get_couleur(self):
        return self.__couleur
    @property
    def get_fact_reflex_diffu(self):
        return self.__fact_reflex_diffu
    @property
    def get_fact_reflex_spec(self):
        return self.__fact_reflex_spec
    @property
    def get_fact_reflet(self):
        return self.__fact_reflet
    @property
    def get_texture(self):
        return self.__texture
    @get_x.setter
    def set_x(self, n):
        self.__x = n
        self.__position = np.array([self.__x,self.__y,self.__z])
    @get_y.setter
    def set_y(self, n):
        self.__y = n
        self.__position = np.array([self.__x,self.__y,self.__z])
    @get_z.setter
    def set_z(self, n):
        self.__z = n
        self.__position = np.array([self.__x,self.__y,self.__z])
    @get_position.setter
    def set_position(self, nouvelle_position):
        self.__position = nouvelle_position
    @get_couleur.setter
    def set_couleur(self,nouvelle_couleur):
        self.__couleur = nouvelle_couleur
    @get_fact_reflex_diffu.setter
    def set_fact_reflex_diffu(self, nouveau_fact_reflex_diffu):
        self.__fact_reflex_diffu = nouveau_fact_reflex_diffu
    @get_fact_reflex_spec.setter
    def set_fact_reflex_spec(self, nouveau_fact_reflex_spec):
        self.__fact_reflex_spec = nouveau_fact_reflex_spec
    @get_fact_reflet.setter
    def set_fact_reflet(self, nouveau_fact_reflet):
        self.__fact_reflet = nouveau_fact_reflet
    @get_texture.setter
    def set_texture(self, nouvelle_texture):
        self.__texture = nouvelle_texture
     
    @abstractmethod    
    def intersection(self):
        pass
    
    @abstractmethod 
    def normale(self):
        pass