import pygame
from setting import *

class Menu:
    def __init__(self):

        self.show_main_menu = True
        self.font = pygame.font.Font(UI_FONT, 48)
        self.main_menu_title = self.font.render("Rougelite Basic", True, TEXT_COLOR)
        self.start_button = pygame.Rect(WIDTH // 2 - 150, 200, 300, 50)
        self.quit_button = pygame.Rect(MENU_WIDTH_CENTER - 100, 300, 200, 50)
        self.start_text = self.font.render("Start Game", True, MENU_BUTTON_COLOR)
        self.quit_text = self.font.render("Quit", True, MENU_BUTTON_COLOR)

    def render_main_menu(self, screen):
        # Load the background image
        background_image = pygame.image.load("./Asset/MenuBG.png")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGTH))

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Position of main menu title
        title_x = MENU_WIDTH_CENTER - self.main_menu_title.get_width() // 2
        screen.blit(self.main_menu_title, (title_x, 100))

        # Drawing buttons
        pygame.draw.rect(screen, MENU_BUTTON_BG, self.start_button)
        pygame.draw.rect(screen, MENU_BUTTON_BG, self.quit_button)

        # Render text on buttons
        start_text_rect = self.start_text.get_rect(center=self.start_button.center)
        screen.blit(self.start_text, start_text_rect)

        quit_text_rect = self.quit_text.get_rect(center=self.quit_button.center)
        screen.blit(self.quit_text, quit_text_rect)

        pygame.display.update()

    # def render_main_menu(self, screen):
        
    #     # setup
    #     screen.fill(MENU_BG_COLOR)

    #     # pos of mainmenu
    #     screen.blit(self.main_menu_title, (MENU_WIDTH_CENTER - self.main_menu_title.get_width() // 2, 100))

    #     # drawing button
    #     pygame.draw.rect(screen, MENU_BUTTON_BG, self.start_button)
    #     pygame.draw.rect(screen, MENU_BUTTON_BG, self.quit_button)

    #     # render text
    #     text_rect = self.start_text.get_rect(center=self.start_button.center)
    #     screen.blit(self.start_text, text_rect)

    #     text_rect = self.quit_text.get_rect(center=self.quit_button.center)
    #     screen.blit(self.quit_text, text_rect)

    #     pygame.display.update()

