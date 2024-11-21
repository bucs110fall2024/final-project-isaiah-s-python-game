import pygame

class Pie:
    def __init__(self, x, y, radius, screen, click_effect=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.image = pygame.image.load(f"assets/pie.png")
        self.rect = self.image.get_rect(center=(x, y,))
        self.click_effect = click_effect
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def is_clicked(self, pos):
        clicked = self.rect.collidepoint(pos)
        return self.rect.collidepoint(pos)
    
    def on_click(self):
        if self.click_effect:
            self.click_effect()
            
    
        
