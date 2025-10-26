
from sprite import Sprite



class Enemy(Sprite):
    def __init__(self, startx, starty):
        super().__init__("box_sprites/on.png", startx, starty)