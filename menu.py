import sys
import pygame

pygame.init()

class Menu:
    def __init__(self,
                 ecran,
                 items,
                 bg_color=(0,0,0),
                 font=None,
                 font_size=50,
                 font_color=(255,255,255)):
        
        self.ecran = ecran
        self.font = pygame.font.SysFont(font, font_size)
        self.ecran_larg = self.ecran.get_rect().width
        self.ecran_haut = self.ecran.get_rect().height

        self.paddingx = 8
        self.paddingy = 20

        self.bg_color = bg_color
        self.bg_img = pygame.image.load('images/menu.png')
        self.bg_img_rect = self.bg_img.get_rect()

        self.start_selected = False
        self.quit_select = False

        self.index_selected = 0
        self.current_item = ()

        self.mainloop = True
        
        self.menu_items = []

 
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
            larg = label.get_rect().width
            haut = label.get_rect().height
    
    # Calcul la position en abscisse de l'élément de menu 
            posx = (self.ecran_larg / 2) - (larg / 2)
 
    # Calcul la hauteur totale du menu
            t_h = len(items) * haut
 
    # Calcul la position en ordonnée
            posy = (self.ecran_haut / 2) - (t_h / 2) + (index * haut)
 
    # Ajoute l'élément de menu avec ses dimensions calculées
            self.menu_items.append([item, label, (larg, haut), (posx, posy)])

    def run(self):
        while self.mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for index, item in enumerate(self.menu_items):
                            if self.current_item[0] == item[0]:
                                if self.index_selected > 0:
                                    self.index_selected -= 1
                    if event.key == pygame.K_DOWN:
                        for index, item in enumerate(self.menu_items):
                            if self.current_item[0] == item[0]:
                                if self.index_selected < (len(self.menu_items) - 1):
                                    self.index_selected += 1

                    if event.key == pygame.K_RETURN:
                        if len(self.current_item) > 0:
                            if self.current_item[0] == "Start":
                                self.start_selected = True
                            elif self.current_item[0] == "Quit":
                                self.quit_select = True
                            self.mainloop = False



            self.current_item = self.menu_items[self.index_selected]

            self.ecran.fill(self.bg_color)
 
            if not self.start_selected:
                self.ecran.blit(self.bg_img, self.bg_img_rect)
 
                for name, label, (width, height), (posx, posy) in self.menu_items:
                    self.ecran.blit(label, (posx, posy))
                    name, label, (width, height), (posx, posy) = self.current_item
                    pygame.draw.rect(
                                     self.ecran,
                                     (255, 255, 255),
                                     [
                                         posx - self.paddingx, posy - self.paddingy,
                                         width + self.paddingx + self.paddingx,
                                         height + self.paddingy
                                     ],
                                     2)
 
                    pygame.display.flip()