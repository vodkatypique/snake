import pygame
from pygame import locals as const
from game import Game


def main():
    print("appuyer sur n'importe quelle touche pour jouer")

    pygame.init()

    ecran = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Snake")

    fond = pygame.image.load("images/menu.png").convert_alpha()

    continuer = True
    jeu = Game(ecran)

    while continuer:
        for event in pygame.event.get():
            if event.type == const.QUIT:
                continuer = False
            if event.type == const.KEYDOWN:
                ecran.fill((0, 0, 0))
                jeu.start()
                continuer = False

        ecran.blit(fond, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
