from objet import *

class Triangle(Objet):
    def __init__(self,x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,ombre,normalex,normaley,normalez,p1,p2,p3):
        super().__init__(x,y,z,couleur,fact_reflex_diffu,fact_reflex_spec,fact_reflet,ombre)
        self.__normale = np.array([normalex,normaley,normalez])
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
    
    ##### Getter et setter ######
    @property
    def get_normale(self):
        return self.__normale
    @property
    def get_p1(self):
        return self.__p1
    @property
    def get_p2(self):
        return self.__p2
    @property
    def get_p3(self):
        return self.__p3
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
    
    def est_dans_triangle(self,p1,p2,p3,pt_inter):
        '''
        Notre point est dans un triangle si ces conditions sont réunies
        (vect(p1,p2) ^ vect(p1,inter)) . (vect(p1,inter) ^ vect(p1,p3)) >= 0
        (vect(p2,p1) ^ vect(p2,inter)) . (vect(p2,inter) ^ vect(p2,p3)) >= 0
        (vect(p3,p1) ^ vect(p3,inter)) . (vect(p3,inter) ^ vect(p3,p2)) >= 0
        '''
        V_p1_p2 = Vecteur(p1,p2)
        V_p1_inter = Vecteur(p1,pt_inter)
        V_p1_p3 = Vecteur(p1,p3)
        prod_vect_p1p2_p1inter = V_p1_p2.prod_vect(V_p1_inter)
        prod_vect_p1inter_p1p3 = V_p1_inter.prod_vect(V_p1_p3)
        prod_scal_p1p2p1inter_p1interp1p3 = np.dot(prod_vect_p1p2_p1inter,prod_vect_p1inter_p1p3)
        if(prod_scal_p1p2p1inter_p1interp1p3 >= 0):
            V_p2_p1 = Vecteur(p2,p1)
            V_p2_inter = Vecteur(p2,pt_inter)
            V_p2_p3 = Vecteur(p2,p3)
            prod_vect_p2p1_p2inter = V_p2_p1.prod_vect(V_p2_inter)
            prod_vect_p2inter_p2p3 = V_p2_inter.prod_vect(V_p2_p3)
            prod_scal_p2p1p2inter_p2interp2p3 = np.dot(prod_vect_p2p1_p2inter,prod_vect_p2inter_p2p3)
            if(prod_scal_p2p1p2inter_p2interp2p3 >= 0):         
                V_p3_p1 = Vecteur(p3,p1)
                V_p3_inter = Vecteur(p3,pt_inter)  
                V_p3_p2 = Vecteur(p3,p2)
                prod_vect_p3p1_p3inter = V_p3_p1.prod_vect(V_p3_inter)
                prod_vect_p3inter_p3p2 = V_p3_inter.prod_vect(V_p3_p2)
                prod_scal_p3p1p3inter_p3interp3p2 = np.dot(prod_vect_p3p1_p3inter,prod_vect_p3inter_p3p2)
                if(prod_scal_p3p1p3inter_p3interp3p2 >= 0):
                    return True
        return False             
        
        
        
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
                point_intersection = pixel + t * vecteur_directeur
                if(self.est_dans_triangle(self.get_p1,self.get_p2,self.get_p3,point_intersection) == True):
                    return t
                else:
                    return None
    
    def normale(self,vecteur_directeur,emplacement_camera,pixel):
        '''
        Méthode pour trouver notre point d'intersection ainsi que la normale qui lui est attachée
        '''
        if(self.intersection(vecteur_directeur,emplacement_camera,pixel) is not None):
            point_intersection = pixel + self.intersection(vecteur_directeur,emplacement_camera,pixel) * vecteur_directeur
            normale = Vecteur(self.get_position,point_intersection)
            normale_normalise = normale.normalisation()
            return point_intersection,normale_normalise