import pygame
import time

class Boosts:
    def __init__(self, x, y, screen, effect_type):
        self.x = x
        self.y = y
        self.screen = screen
        self.effect_type = effect_type
        self.size = 50
        self.boost_imagepath = r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\diamondpie.png"
        self.image = pygame.image.load(self.boost_imagepath)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.spawn_time = time.time()
        self.active = True

    def update(self):
        if time.time() - self.spawn_time > 12:
            self.active = False

    def draw(self):
        if self.active:
            self.screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def on_click(self, controller):
        if self.effect_type == "double_click_score":
            controller.multiplier = 2
            controller.action_text = "Double Click Score activated!"
            print("Double Click Score activated!")
        elif self.effect_type == "increase_score":
            controller.score += round(controller.score * 0.5)  
            controller.action_text = "+50% Score activated!"
            print("50% Score added!")
        elif self.effect_type == "increase_multiplier":
            controller.pps *= 2  
            controller.action_text = "PPS doubled!"
            print("PPS doubled!")
        elif self.effect_type == "five_times_multiplier":
            controller.score += 5  
            controller.action_text = "+500% Score activated!"
            print("500% Score added!")
        elif self.effect_type == "fifty_times_multiplier":
            controller.pps += 50  
            controller.action_text = "PPS increased by 50!"
            print("PPS increased by 50!")
        self.active = False

