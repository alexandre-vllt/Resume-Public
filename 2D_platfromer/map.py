import pygame

from box import Box
from enemy import Enemy
from interface import Player_exit
from map1 import MAP1
from map2 import MAP2
from map3 import MAP3
from map4 import MAP4
from mbox import Mbox
from portal import Portal

WIDTH = 1200
HEIGHT = 800
LEN_BOX = 25
MAX_X = WIDTH // LEN_BOX + 2
MAX_Y = HEIGHT // LEN_BOX + 2

MAP0 = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]


MAPS = [MAP1, MAP2, MAP3, MAP4]


class Map:
    """
    Represents a game map with various elements such as boxes, enemies, portals, and a player exit.

    Attributes:
        boxes (pygame.sprite.Group): A group containing box sprites.
        player_exit (Player_exit): An instance of the player exit.
        enemys (pygame.sprite.Group): A group containing enemy sprites.
        mboxes (pygame.sprite.Group): A group containing mbox sprites.
        portals (pygame.sprite.Group): A group containing portal sprites.
        bullet (pygame.sprite.Group): A group containing bullet sprites.
        mat (list): The matrix representing the map layout.
        spawnx (float): The x-coordinate of the player's spawn position.
        spawny (float): The y-coordinate of the player's spawn position.
        vect_bot (list): A list containing vectors for bot movement.
        vect_portal (list): A list containing vectors for portal positions.
        background (pygame.Surface): The background image of the map.
        box_sprite (pygame.Surface): The image representing a box sprite.

    Methods:
        draw(screen, bullet_left, bullet_right, player):
            Draws the map elements on the given screen, including the player, enemies, boxes, portals, and more.
    """

    def __init__(self, matrice, vect_bot, vect_portal, background, box_sprite):
        """
        Initializes a Map instance with the specified parameters.

        Parameters:
            matrice (list): A matrix representing the map layout.
            vect_bot (list): A list containing vectors for bot movement.
            vect_portal (list): A list containing vectors for portal positions.
            background (str): The file path of the background image.
            box_sprite (str): The file path of the box sprite image.
        """
        self.boxes = pygame.sprite.Group()
        self.player_exit = Player_exit(0, 0)
        self.enemys = pygame.sprite.Group()
        self.mboxes = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        self.mat = matrice
        self.spawnx = 0
        self.spawny = 0
        self.vect_bot = vect_bot
        self.vect_portal = vect_portal
        numberportal = 0
        self.background = pygame.image.load(background)
        self.box_sprite = pygame.image.load(box_sprite)
        for i in range(MAX_X):
            for j in range(MAX_Y):
                match matrice[j][i]:
                    # box
                    case 1:
                        new_box = Box((i - 1) * 25 + 12.5, (j - 1) * 25 + 12.5)
                        new_box.image = self.box_sprite
                        self.boxes.add(new_box)
                    # fusee
                    case 2:
                        self.player_exit = Player_exit(
                            (i - 1) * 25 + 12.5, (j - 1) * 25 - 25
                        )
                    # fire
                    case 3:
                        self.enemys.add(Enemy((i - 1) * 25 + 12.5, (j - 1) * 25 + 20))
                    # mbox
                    case 4:
                        self.mboxes.add(Mbox((i - 1) * 25 + 12.5, (j - 1) * 25 + 12.5))
                    # portal
                    case 5:
                        self.portals.add(
                            Portal(
                                (i - 1) * 25 + 7,
                                (j - 1) * 25,
                                self.vect_portal[numberportal][0],
                                self.vect_portal[numberportal][1],
                            )
                        )
                        numberportal += 1
                    # position de spawn
                    case 6:
                        self.spawnx = (i - 1) * 25 + 12.5
                        self.spawny = (j - 1) * 25 - 25

    def draw(self, screen, bullet_left, bullet_right, player):
        """
        Draws the map elements on the given screen, including the player, enemies, boxes, portals, and more.

        Parameters:
            screen (pygame.Surface): The screen surface to draw the elements on.
            bullet_left (Bullet): The left-moving bullet instance.
            bullet_right (Bullet): The right-moving bullet instance.
            player (Player_exit): The player exit instance.
        """
        if bullet_left.movement == 1:
            bullet_left.draw(screen)
        if bullet_right.movement == 1:
            bullet_right.draw(screen)
        player.draw(screen)
        self.enemys.draw(screen)
        self.boxes.draw(screen)
        self.mboxes.draw(screen)
        self.portals.draw(screen)
        self.player_exit.draw(screen)
        for bot in self.vect_bot:
            bot.update(self.boxes, self.bullet, bullet_left, bullet_right, player)
