import pygame

class Upgrade:
    def __init__(self, x, y, name, base_price, pps, image_path, screen):
        self.x = x
        self.y = y
        self.name = name
        self.base_price = base_price
        self.pps = pps
        self.price = base_price
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (70, 70))  
        self.rect = pygame.Rect(x, y, 180, 70)
        self.quantity = 0
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (150, 150, 150), self.rect)
        self.screen.blit(self.image, (self.rect.x + 10, self.rect.y + 5))
        font = pygame.font.Font(None, 24)
        text = f"{self.name}: {self.quantity} | Cost: {int(self.price)} pies"
        text_surface = font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 50))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def purchase(self, controller):
        if controller.score >= self.price: 
            self.quantity += 1
            controller.score -= self.price  
            self.price *= 1.2  
            controller.pps += self.pps  
            print(f"Purchased {self.name}. New price: {self.price}, CPS: {controller.pps}")
            return True
        else:
            print("Not enough pies to purchase upgrade.")
            return False