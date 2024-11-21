import pygame
from pie import Pie


class Controller:
    def __init__(self, screen):
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((800, 600))
        self.width, self.height = pygame.display.get_window_size()
        self.score = 0
        self.pie = Pie(400, 300, 100, screen, is_clicked=self.increase_score)
        
        
    def increase_score(self):
        self.score += 1
        
    def mouseevent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.pie.is_clicked(event.pos):
            self.pie.on_click()
            
    def draw(self):
        self.pie.draw()
    
    def main():
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pie Click")
        clock = pygame.time.Clock()
        controller = Controller(screen)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                controller.mouseevent(event)
                
            controller.draw()
    pygame.quit()
    
    main()
        
