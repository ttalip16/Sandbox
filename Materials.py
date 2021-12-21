import random as rd
import pygame

# родителький класс
class Material:

    def __init__(self):
        self.color_list = list()
        self.color = rd.choice(self.color_list)
        self.gravity = 0 # 0 - no gravity, 1 - down, 2 - up (gas)
        self.temperature = 0
        self.temperature_to_fire = None

    def set_gravity(self, bool_gravity):
        self.gravity = bool_gravity

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def add_temperature(self, delta_temperature):
        self.temperature += delta_temperature

    def render(self, screen, x, y, cell_size):
        size = (x, y, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, size)

class SandMaterial(Material):

    def __init__(self):
        self.color_list = [(255, 255, 0), (200, 200, 10)]
        self.color = rd.choice(self.color_list)
        self.gravity = 1 # 0 - no gravity, 1 - down, 2 - up (gas)
        self.temperature = 0
        self.temperature_to_fire = None