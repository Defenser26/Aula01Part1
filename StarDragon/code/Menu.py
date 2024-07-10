import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_RED, MENU_OPTION, WIN_WIDTH, COLOR_WHITE, COLOR_YELLOW

class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.surf.get_rect(left=-500, top=-200)

    def run(self):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)
        menu_option = 0

        while True:
            # Desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(80, "Dragon", COLOR_RED, (WIN_WIDTH / 2, 100))
            self.menu_text(80, "Star", COLOR_RED, (WIN_WIDTH / 2, 200))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 400 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 400 + 30 * i))

            pygame.display.flip()

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
