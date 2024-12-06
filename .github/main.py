from src.controller import Controller
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ultimate Pie Clicker!")
    controller = Controller(screen)
    controller.run()

if __name__ == "__main__":
    main()

pygame.quit()


