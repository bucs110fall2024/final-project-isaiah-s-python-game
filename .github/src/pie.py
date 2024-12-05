import pygame

class Pie:
    def __init__(self, x, y, radius, screen, click_effect=None):
        self.x = x
        self.y = y
        self.radius = radius 
        self.screen = screen
        self.image_path = r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\pie.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))  
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.click_effect = click_effect

    def draw(self):
        self.screen.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def on_click(self):
        if self.click_effect:
            self.click_effect()  
            print("Pie clicked! Score increased.")
