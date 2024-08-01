import numpy as np
from vecteur import *

class Camera():
    def __init__(self,l,h,x,y,z,dir,orient,dist_foc):
        self.__longeur = l
        self.__hauteur = h
        self.__dimension = [self.get_l,self.get_h]
        self.__x = x
        self.__y = y
        self.__z = z
        self.__position = np.array([x,y,z])
        self.__direction = dir
        self.__orientation = orient
        self.__distance_focale = dist_foc
        p0 = np.array([0,0,0])
        ph = np.array([0,1,0])
        pd = np.array([1,0,0])
        self.__H = Vecteur(p0,ph)
        self.__D = Vecteur(p0,pd)
    
    ##### Getter et Setter #####
    @property
    def get_l(self):
        return self.__longeur
    @property
    def get_h(self):
        return self.__hauteur
    @property
    def get_dimension(self):
        return self.__dimension
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
    def get_direction(self):
        return self.__direction
    @property
    def get_orientation(self):
        return self.__orientation
    @property
    def get_distance_focale(self):
        return self.__distance_focale
    @property
    def get_H(self):
        return self.__H
    @property
    def get_D(self):
        return self.__D
    @get_l.setter
    def set_l(self, l):
        self.__longeur = l
    @get_h.setter
    def set_h(self, h):
        self.__hauteur = h
    @get_x.setter
    def set_x(self, x):
        self.__x = x
        self.__position = np.array([x, self.__y, self.__z])
    @get_y.setter
    def set_y(self, y):
        self.__y = y
        self.__position = np.array([self.__x, y, self.__z])
    @get_z.setter
    def set_z(self, z):
        self.__z = z
        self.__position = np.array([self.__x, self.__y, z])
    @get_direction.setter
    def set_direction(self, dir):
        self.__direction = dir
    @get_orientation.setter
    def set_orientation(self, orient):
        self.__orientation = orient
    @get_distance_focale.setter
    def set_distance_focale(self, dist_foc):
        self.__distance_focale = dist_foc