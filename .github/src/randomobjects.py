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
        self.active = True

    def update(self):
        pass  

    def draw(self):
        if self.active:
            self.screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def on_click(self, controller):  
        if self.effect_type == "double_click_score":
            controller.double_click_score_multiplier *= 2  
            controller.action_text = "Double Click Score activated!"
            controller.action_text_position = (self.x, self.y) 
            controller.action_text_start_time = time.time()  
            print("Double Click Score activated!")
        elif self.effect_type == "increase_score":
            controller.score += controller.score * 0.5  
            controller.action_text = "Score increased by 0.5!"
            controller.action_text_position = (self.x, self.y)  
            controller.action_text_start_time = time.time()  
            print("50% Score added!")
        elif self.effect_type == "double_score":  
            controller.score *= 2 
            controller.action_text = "Score doubled!"
            controller.action_text_position = (self.x, self.y)  
            controller.action_text_start_time = time.time()  
            print("PPS increased by 50%!")
        elif self.effect_type == "five_times_multiplier":
            controller.multiplier *= 5  
            controller.action_text = "Five Times Multiplier activated!"
            controller.action_text_position = (self.x, self.y)  
            controller.action_text_start_time = time.time() 
            print("Five Times Multiplier activated!")
        elif self.effect_type == "2x PPS multiplier":
            controller.pps *= 2  
            controller.action_text = "PPS increased by 200%!"
            controller.action_text_position = (self.x, self.y) 
            controller.action_text_start_time = time.time() 
            print("PPS increased by 200%!")
        self.active = False
