import pygame

from sprite import Sprite


class Spaceship(Sprite):
    """
    Represents a spaceship sprite in the game.

    Attributes:
    - fly_cycle: List of images representing the flying animation frames for the spaceship.
    - animation_index: Index to track the current animation frame.

    Methods:
    - __init__(startx, starty): Initializes the Spaceship object with specified parameters.
    - fly_animation(): Updates the flying animation of the spaceship.
    - update(): Updates the position and animation of the spaceship during the game.
    """

    def __init__(self, startx, starty):
        """
        Initializes the Spaceship object with specified parameters.

        Parameters:
        - startx (int): The initial x-coordinate of the spaceship.
        - starty (int): The initial y-coordinate of the spaceship.
        """
        super().__init__("animation_sprites/longfly01.png", startx, starty)

        png_fly = [
            "animation_sprites/longfly01.png",
            "animation_sprites/longfly02.png",
            "animation_sprites/longfly03.png",
            "animation_sprites/longfly04.png",
        ]

        self.fly_cycle = [pygame.image.load(f"{image}") for image in png_fly]
        self.animation_index = 0

    def fly_animation(self):
        """
        Updates the flying animation of the spaceship.
        """
        if self.animation_index == 3:
            self.animation_index = 0
        else:
            self.animation_index += 1
        self.image = self.fly_cycle[self.animation_index]

    def update(self):
        """
        Updates the position and animation of the spaceship during the game.
        """
        if self.rect.x > 1200:
            self.rect.move_ip([-self.rect.x, 0])
        self.rect.move_ip([10, 0])
        self.fly_animation()


class Takeoff(Sprite):
    """
    Represents a takeoff animation sprite in the game.

    Attributes:
    - takeoff_cycle: List of images representing the takeoff animation frames.
    - animation_index: Index to track the current animation frame.

    Methods:
    - __init__(startx, starty): Initializes the Takeoff object with specified parameters.
    - fly_animation(): Updates the takeoff animation.
    - update(): Updates the position and animation of the takeoff sprite during the game.
    """

    def __init__(self, startx, starty):
        """
        Initializes the Takeoff object with specified parameters.

        Parameters:
        - startx (int): The initial x-coordinate of the takeoff sprite.
        - starty (int): The initial y-coordinate of the takeoff sprite.
        """
        super().__init__("animation_sprites/takeoff01.png", startx, starty)

        png_fly = [
            "animation_sprites/takeoff01.png",
            "animation_sprites/takeoff02.png",
            "animation_sprites/takeoff03.png",
            "animation_sprites/takeoff04.png",
        ]

        self.takeoff_cycle = [pygame.image.load(f"{image}") for image in png_fly]
        self.animation_index = 0

    def fly_animation(self):
        """
        Updates the takeoff animation.
        """
        if self.animation_index == 3:
            self.animation_index = 0
        else:
            self.animation_index += 1
        self.image = self.takeoff_cycle[self.animation_index]

    def update(self):
        """
        Updates the position and animation of the takeoff sprite during the game.
        """
        self.rect.move_ip([0, -10])
        self.fly_animation()
