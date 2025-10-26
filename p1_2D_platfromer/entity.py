from abc import abstractmethod

import pygame

from sprite import Sprite


class Entity(Sprite):
    """
    Abstract base class representing a game entity.

    Attributes:
    - png_walk (list): List of image paths representing the walking animation frames.

    Methods:
    - __init__(image, startx, starty, png_walk): Initializes the Entity object with specified parameters.
    - check_collision(x, y, sprites): Checks for collisions with other sprites.
    - move_right(): Moves the entity to the right.
    - move_left(): Moves the entity to the left.
    - update(): Abstract method to be implemented in subclasses for updating the entity.
    - move(): Abstract method to be implemented in subclasses for handling movement.
    - walk_animation(): Abstract method to be implemented in subclasses for managing walking animation.
    """

    def __init__(self, image, startx, starty, png_walk):
        """
        Initializes the Entity object with specified parameters.

        Parameters:
        - image (str): The image path for the entity's sprite.
        - startx (int): The initial x-coordinate of the entity.
        - starty (int): The initial y-coordinate of the entity.
        - png_walk (list): List of image paths representing the walking animation frames.
        """
        super().__init__(image, startx, starty)
        self.png_walk = png_walk

    def check_collision(self, x, y, sprites):
        """
        Checks for collisions with other sprites.

        Parameters:
        - x (int): The x-translation for collision checking.
        - y (int): The y-translation for collision checking.
        - sprites (pygame.sprite.Group): The group of sprites to check for collisions.

        Returns:
        - pygame.sprite.Sprite or None: The collided sprite, or None if no collision.
        """
        self.rect.move_ip([x, y])
        collide = pygame.sprite.spritecollideany(self, sprites)
        self.rect.move_ip([-x, -y])
        return collide

    def move_right(self):
        """
        Moves the entity to the right.
        """
        self.facing_left = False
        self.walk_animation()
        self.hsp = self.speed

    def move_left(self):
        """
        Moves the entity to the left.
        """
        self.facing_left = True
        self.walk_animation()
        self.hsp = -self.speed

    @abstractmethod
    def update(self):
        """
        Abstract method to be implemented in subclasses for updating the entity.
        """
        pass

    @abstractmethod
    def move(self):
        """
        Abstract method to be implemented in subclasses for handling movement.
        """
        pass

    @abstractmethod
    def walk_animation(self):
        """
        Abstract method to be implemented in subclasses for managing walking animation.
        """
        pass
