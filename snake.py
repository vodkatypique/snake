import pygame
from constantes import *
import nourriture


class Snake:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        
        self.ecran_largeur = self.ecran.get_width()

        self.ecran_hauteur = self.ecran.get_height()

        self.image_tete = pygame.image.load("images/tete.png").convert_alpha()
        self.image_tete = pygame.transform.scale(self.image_tete, (20, 20))

        self.image_corps = pygame.image.load("images/corps.png").convert_alpha()
        self.image_corps = pygame.transform.scale(self.image_corps, (20, 20))

        self.image_bordure = pygame.image.load("images/bordures.png").convert_alpha()
        self.image_bordure = pygame.transform.scale(self.image_bordure, (20, 20))

        self.coordonnees_bordures_haut = [[x, 0] for x in range(self.ecran_largeur) if x%self.image_bordure.get_width()==0]
        self.coordonnees_bordures_bas = [[x, self.ecran_hauteur-self.image_bordure.get_height()] for x in range(self.ecran_largeur) if x%self.image_bordure.get_width()==0]
        self.coordonnees_bordures_gauche = [[0, y] for y in range(self.ecran_hauteur) if y%self.image_bordure.get_height()==0]
        self.coordonnees_bordures_droite = [[self.ecran_largeur-self.image_bordure.get_width(), y] for y in range(self.ecran_hauteur) if y%self.image_bordure.get_height()==0]

        # marche bien et comprehensible, mais le "dedoublonnage" est gourmand, donc attention sur de tres grande taille, pas tres grave ici
        self.coordonnees_bordures = self.coordonnees_bordures_bas+self.coordonnees_bordures_droite+self.coordonnees_bordures_gauche+self.coordonnees_bordures_haut
        self.coordonnees_bordures_sans_doublons = [elt for i,elt in enumerate(self.coordonnees_bordures) if elt not in self.coordonnees_bordures[0:i]]
        ######################

        self.pos = [[self.ecran_largeur//2, self.ecran_hauteur//2], [(self.ecran_largeur//2) - self.image_corps.get_width(), (self.ecran_hauteur//2)]]

        self.pomme = nourriture.Pomme(self)

    def render_bordure(self):
        for coordonnees in self.coordonnees_bordures:
            self.ecran.blit(self.image_bordure, coordonnees)

    def render(self):
        self.render_bordure()
        for i, coordonnees in enumerate(self.pos):
            if i == 0:
                self.ecran.blit(self.image_tete, coordonnees)
            else:
                self.ecran.blit(self.image_corps, coordonnees)
        self.ecran.blit(self.pomme.image_pomme, self.pomme.pos)


        texte = pygame.font.SysFont('freesans', 15, True)
        title_texte = texte.render("niveau : " + str(self.pomme.numero), True, (255, 0, 0))
        self.ecran.blit(title_texte, title_texte.get_rect())

    def render_pomme(self):
        self.pomme.supprimerEtGenerer(self)

    def move(self, dir: int=DROITE):
        temp = list(self.pos[0])
        self.pos.insert(1, temp)
        if dir == DROITE:
            if self.pos[0][0] + VITESSE_DEPLACEMENT + self.image_tete.get_width() <= self.ecran_largeur:
                self.pos[0][0] += VITESSE_DEPLACEMENT
        elif dir == GAUCHE:
            if self.pos[0][0] - VITESSE_DEPLACEMENT >= 0:
                self.pos[0][0] -= VITESSE_DEPLACEMENT
        elif dir == HAUT:
            if self.pos[0][1] - VITESSE_DEPLACEMENT >= 0:
                self.pos[0][1] -= VITESSE_DEPLACEMENT
        elif dir == BAS:
            if self.pos[0][1] + VITESSE_DEPLACEMENT + self.image_tete.get_height() <= self.ecran_hauteur:
                self.pos[0][1] += VITESSE_DEPLACEMENT
        
        if self.pos[0] in self.coordonnees_bordures_sans_doublons:
            print("touché")

        if self.pos[0] == self.pomme.pos:
            print("miam")
            self.pomme.supprimerEtGenerer(self)
            while self.pomme.pos in self.pos:
                self.pomme.supprimerEtGenerer(self)
        else:
            last = self.pos.pop()
        
        if list(self.pos[0]) in self.pos[1:]:
            print ("touché") 

