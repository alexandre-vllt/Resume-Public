import pygame

from sprite import Sprite


class Mbox(Sprite):
    def __init__(self, startx, starty):
        super().__init__("box_sprites/mbox.png", startx, starty)

        mbox_shine = [
            "box_sprites/mbox.png",
            "box_sprites/mbox2.png",
            "box_sprites/mbox3.png",
        ]

        self.shine_cycle = [pygame.image.load(f"{image}") for image in mbox_shine]
        self.shine_index = 0
        self.cont = 10
        self.used = False
        self.first_use = True

    def shine_animation(self):
        self.image = self.shine_cycle[self.shine_index]
        self.cont += 1
        if self.cont < 50:
            self.shine_index = 1
        elif 50 <= self.cont < 100:
            self.shine_index = 0
        else:
            self.cont = 0

    def update(self, collision_mboxes, exitplayer):
        if not (collision_mboxes) and not (self.used):
            self.shine_animation()
        else:
            self.image = self.shine_cycle[2]
            self.used = True
        if(exitplayer):
            self.shine_animation()
            self.used = False

