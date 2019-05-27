import pygame
from pygame import locals as const
from game import Game
from menu import Menu


def main():
    pygame.init()

    ecran = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Snake Menu")
    menu_items = ('Start', 'Quit')
    gamemenu = Menu(ecran, menu_items)

    #fond = pygame.image.load("images/menu.png").convert_alpha()

    jeu = Game(ecran)

    while gamemenu.mainloop:
        gamemenu.run()
        if gamemenu.start_selected:
            jeu.start()
    pygame.quit()

if __name__ == "__main__":
    main()
