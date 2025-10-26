
from sprite import Sprite


class Portal(Sprite):
    def __init__(self, startx, starty, tpx, tpy):
        super().__init__("box_sprites/portal.png", startx, starty)
        self.tpx = tpx
        self.tpy = tpy
