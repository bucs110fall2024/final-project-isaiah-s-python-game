import pygame
from src.controller import Controller  

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pie Clicker!")
    controller = Controller(screen)
    controller.run()

if __name__ == "__main__":
    main()

