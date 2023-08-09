import pygame

class Scene:
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width, self.height = width, height
        self.objects = []