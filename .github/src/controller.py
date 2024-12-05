import pygame
from pie import Pie
from randomobjects import Boosts
from upgrade import Upgrade
import random
import time
import os

class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.background_path = r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\background.png"
        self.background = pygame.image.load(self.background_path)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.pps = 0  
        self.multiplier = 1  
        self.pie = Pie(300, 300, 100, screen, click_effect=self.increase_score)
        self.boosts = []
        self.boost_spawn_chance = 0.0025  
        self.last_boost_spawn_time = time.time()
        self.font = pygame.font.Font(None, 36)
        self.action_font = pygame.font.Font(None, 24)
        self.action_text = ""
        self.action_text_color = (255, 0, 0)
        self.action_text_position = (0, 0)
        self.action_text_start_time = 0
        self.upgrades = []
        self.upgrades_data()
        self.high_score = self.load_high_score()
        self.purchase_message = ""  
        self.purchase_message_position = (self.width // 2, 0) 

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                try:
                    return int(round(float(file.read().strip())))  
                except ValueError:
                    return 0  
        return 0

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1 * self.multiplier  
        self.action_text = f"+{1 * self.multiplier} score"
        self.action_text_position = (self.pie.x, self.pie.y)
        self.action_text_start_time = time.time()
        print(f"Score increased! Current score: {self.score}")

    def draw_score(self):
        score_text = f"Pies: {int(self.score)}"
        pps_text = f"PPS: {int(self.pps)}" 
        multiplier_text = f"Multiplier: {int(self.multiplier)}"
        high_score_text = f"High Score: {int(self.high_score)}"

        if self.score >= 10000:
            score_surface = self.font.render(score_text, True, (0, 255, 0)) 
            pps_surface = self.font.render(pps_text, True, (0, 255, 0))
            multiplier_surface = self.font.render(multiplier_text, True, (0, 255, 0))
            high_score_surface = self.font.render(high_score_text, True, (0, 255, 0))
        elif self.score >= 5000:
            score_surface = self.font.render(score_text, True, (255, 255, 0))  
            pps_surface = self.font.render(pps_text, True, (255, 255, 0))
            multiplier_surface = self.font.render(multiplier_text, True, (255, 255, 0))
            high_score_surface = self.font.render(high_score_text, True, (255, 255, 0))
        else:
            score_surface = self.font.render(score_text, True, (0, 0, 255)) 
            pps_surface = self.font.render(pps_text, True, (0, 0, 255))
            multiplier_surface = self.font.render(multiplier_text, True, (0, 0, 255))
            high_score_surface = self.font.render(high_score_text, True, (0, 0, 255))

        score_rect = score_surface.get_rect(center=(self.screen.get_width() // 2, 20))
        pps_rect = pps_surface.get_rect(center=(self.screen.get_width() // 2, 60))  
        multiplier_rect = multiplier_surface.get_rect(center=(self.screen.get_width() // 2, 100))
        high_score_rect = high_score_surface.get_rect(topleft=(10, 10))  
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(pps_surface, pps_rect) 
        self.screen.blit(multiplier_surface, multiplier_rect)
        self.screen.blit(high_score_surface, high_score_rect)

        if self.action_text and (time.time() - self.action_text_start_time < 0.5):
            action_surface = self.action_font.render(self.action_text, True, self.action_text_color)
            action_rect = action_surface.get_rect(center=self.action_text_position)
            self.screen.blit(action_surface, action_rect)

        if self.purchase_message:
            purchase_surface = self.font.render(self.purchase_message, True, (255, 0, 0))  
            purchase_rect = purchase_surface.get_rect(center=(self.width // 2, 140))  
            self.screen.blit(purchase_surface, purchase_rect)

    def mouseevent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pie.is_clicked(event.pos):
                print("Pie clicked!")
                self.pie.on_click() 
            for boost in self.boosts:
                if boost.is_clicked(event.pos):
                    boost.on_click(self)
                    self.action_text = f"{boost.effect_type.replace('_', ' ').title()} activated!"
                    self.action_text_position = (boost.x, boost.y)
                    self.action_text_start_time = time.time()
            for upgrade in self.upgrades:
                if upgrade.is_clicked(event.pos):
                    print(f"Upgrade {upgrade.name} clicked!")
                    if upgrade.purchase(self): 
                        self.action_text = f"Purchased {upgrade.name}!"
                        self.purchase_message = ""  
                    else:
                        self.purchase_message = "Not enough pies to purchase upgrade!"
                        self.purchase_message_position = event.pos  

    def spawn_boost(self):
        effects = ["double_click_score", "increase_score", "increase_multiplier", "five_times_multiplier", "fifty_times_multiplier"]
        weights = [35, 25, 25, 14, 1]
        effect_type = random.choices(effects, weights=weights)[0]
        x = random.randint(50, self.screen.get_width() * 3 // 4 - 50)
        y = random.randint(50, self.screen.get_height() - 50)
        self.boosts.append(Boosts(x, y, self.screen, effect_type))

    def update_pps(self):
        self.pps = sum(upgrade.pps * upgrade.quantity for upgrade in self.upgrades)
        self.score += self.pps / 60

    def update_boosts(self):
        if random.random() < self.boost_spawn_chance:
            self.spawn_boost()
        for boost in self.boosts:
            boost.update()
        self.boosts = [boost for boost in self.boosts if boost.active]

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.pie.draw()
        self.draw_score()
        for boost in self.boosts:
            boost.draw()
        for upgrade in self.upgrades:
            upgrade.draw()
        pygame.display.flip()

    def upgrades_data(self):
        upgrade_data = [
            {"name": "Oven", "base_price": 100, "pps": 0.5, "image_path": r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\oven.png"},
            {"name": "Kitchen", "base_price": 500, "pps": 2.5, "image_path": r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\factory.png"},
            {"name": "Mine", "base_price": 2000, "pps": 12.5, "image_path": r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\mine.png"},
            {"name": "Planet", "base_price": 10000, "pps": 50, "image_path": r"C:\Users\isaia\OneDrive\Documents\Desktop\final-project-isaiah-s-python-game\.github\assets\planet.png"},
        ]
        
        upgrade_data.sort(key=lambda u: u["pps"])

        menu_x = self.width * 3 // 4
        menu_width = 200
        upgrade_height = 100
        padding = 10
        start_y = padding

        for i, upgrade in enumerate(upgrade_data):
            x = menu_x + (menu_width - 180) // 2
            y = start_y + i * (upgrade_height + padding)
            self.upgrades.append(
                Upgrade(
                    x, y, 
                    upgrade["name"], 
                    upgrade["base_price"], 
                    upgrade["pps"], 
                    upgrade["image_path"], 
                    self.screen
                )
            )

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.mouseevent(event)

            self.update_boosts()
            self.update_pps()  
            self.draw()
            self.save_high_score()  
            self.clock.tick(60)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ultimate Pie Clicker!")
    controller = Controller(screen)
    controller.run()

if __name__ == "__main__":
    main()

pygame.quit()
