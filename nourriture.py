import pygame
import random


class Pomme:
    def __init__(self, snake):
        self.numero = 0
        self.image_pomme = pygame.image.load("images/pomme.png").convert_alpha()
        self.image_pomme = pygame.transform.scale(self.image_pomme, (20, 20))
        self.multiple_x = [x for x in range(snake.image_bordure.get_width(), snake.ecran_largeur-snake.image_bordure.get_width()-self.image_pomme.get_width()) if x%snake.image_bordure.get_width()==0]
        self.multiple_y = [x for x in range(snake.image_bordure.get_height(), snake.ecran_hauteur-snake.image_bordure.get_height()-self.image_pomme.get_height()) if x%snake.image_bordure.get_height()==0]

        self.pos = [random.choice(self.multiple_x), random.choice(self.multiple_y)]

    def supprimerEtGenerer(self, snake):
        self.numero += 1
        self.pos = [random.choice(self.multiple_x), random.choice(self.multiple_y)]
