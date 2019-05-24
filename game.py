import pygame
from pygame import locals as const
from constantes import *
from snake import Snake


class Game:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.snake = Snake(self.ecran)
        self.continuer = True
        self.controles = {
            HAUT: const.K_UP,
            BAS: const.K_DOWN,
            DROITE: const.K_RIGHT,
            GAUCHE: const.K_LEFT
        }

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True
        self.snake = Snake(self.ecran)

    def update_screen(self):
        pygame.draw.rect(self.ecran, (0, 0, 0), (0, 0) + self.ecran.get_size())  # on dessine le fond
        self.snake.render()  # on dessine notre ecran

    def process_event(self, event: pygame.event):
        if event.type == const.KEYDOWN:
            # et revoici l'utilité de nos constantes, utilisées comme clé de dictionnaire :)
            # comme ça on peut plus facilement changer les controles ;)
            if event.key == self.controles[HAUT]:
                self.snake.move(HAUT)
            if event.key == self.controles[BAS]:
                self.snake.move(BAS)
            if event.key == self.controles[DROITE]:
                self.snake.move(DROITE)
            if event.key == self.controles[GAUCHE]:
                self.snake.move(GAUCHE)
        if event.type == const.QUIT:
            self.continuer = False

    def start(self):
        self.prepare()

        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()
            pygame.display.flip()
