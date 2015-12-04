import pygame as py

class Upgrades(py.sprite.Sprite):
    def __init__(self, ButtonNumber, text, ID, colour):
        self.ButtonNumber = ButtonNumber
        self.text = text
        self.ID = ID
        self.colour = colour
        posx = 