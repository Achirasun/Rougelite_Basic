import pygame, sys
from setting import *
from level import Level
from menu import Menu

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Rougelite Basic')
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.main_menu = Menu()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.main_menu.show_main_menu:
                self.main_menu.render_main_menu(self.screen)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.main_menu.start_button.collidepoint(event.pos):
                            self.main_menu.show_main_menu = False  # Transition to the game level
                        elif self.main_menu.quit_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

            else:
                self.screen.fill('white')
                # Run the game level
                self.level.run()

                pygame.display.update()
                self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
