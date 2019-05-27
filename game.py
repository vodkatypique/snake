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
        self.touche = None

    def prepare(self):
        pygame.key.set_repeat(200, 20)
        self.continuer = True
        self.snake = Snake(self.ecran)

    def update_screen(self):
        pygame.draw.rect(self.ecran, (0, 0, 0), (0, 0) + self.ecran.get_size())  # on dessine le fond
        self.snake.render()  # on dessine notre ecran

    def process_event(self):
        for event in pygame.event.get():
            if event.type == const.KEYDOWN:
                if event.key in self.controles.values():
                    self.touche = event.key
            if event.type == const.QUIT:
                self.continuer = False

        if self.touche == self.controles[HAUT]: 
            self.snake.move(HAUT)
        if self.touche == self.controles[BAS]:
            self.snake.move(BAS)
        if self.touche == self.controles[DROITE]:
            self.snake.move(DROITE)
        if self.touche == self.controles[GAUCHE]:
            self.snake.move(GAUCHE)
        

    def start(self):
        self.prepare()
        clock = pygame.time.Clock()

        while self.continuer:
            clock.tick(CLOCK)
            self.process_event()

            self.update_screen()
            pygame.display.flip()
