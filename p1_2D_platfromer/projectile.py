import pygame

from sprite import Sprite


class Projectile(Sprite):
    """
    Represents a projectile in the game.

    Attributes:
    - trajectory_cycle: List of images representing the animation frames for the projectile.
    - speed: The speed at which the projectile moves.
    - movement: Flag indicating whether the projectile is currently in motion.
    - animation_index: Index to track the current animation frame.

    Methods:
    - __init__(startx, starty): Initializes the Projectile object with a starting position.
    - move(x, y): Moves the projectile by the specified amount.
    - trajectory_animation(): Updates the projectile's animation frame.
    - return_player(player): Moves the projectile back to the player's position.
    - check_collision(x, y, boxes): Checks if the projectile collides with any boxes after moving by the specified amount.
    """

    def __init__(self, startx, starty):
        """
        Initializes the Projectile object with a starting position.

        Parameters:
        - startx (int): The initial x-coordinate of the projectile.
        - starty (int): The initial y-coordinate of the projectile.
        """
        super().__init__("character_sprites/LASER.png", startx, starty)

        self.trajectory_cycle = [pygame.image.load("character_sprites/LASER.png")]

        self.speed = 50
        self.movement = 0

        self.animation_index = 0

    def move(self, x, y):
        """
        Moves the projectile by the specified amount.

        Parameters:
        - x (int): The horizontal distance to move.
        - y (int): The vertical distance to move.
        """
        dx = x
        dy = y

        self.movement = 1

        self.rect.move_ip([dx, dy])

    def trajectory_animation(self):
        """
        Updates the projectile's animation frame.
        """
        self.image = self.trajectory_cycle[self.animation_index]
        if self.animation_index < len(self.trajectory_cycle) - 1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def return_player(self, player):
        """
        Moves the projectile back to the player's position.

        Parameters:
        - player (Player): The player object.
        """
        self.rect.x = player.rect.x + 13
        self.rect.y = player.rect.y + 25
        self.movement = 0

    def check_collision(self, x, y, boxes):
        """
        Checks if the projectile collides with any boxes after moving by the specified amount.

        Parameters:
        - x (int): The horizontal distance to move for collision checking.
        - y (int): The vertical distance to move for collision checking.
        """
        self.rect.move_ip([x, y])
        collide = pygame.sprite.spritecollideany(self, boxes)
        self.rect.move_ip([-x, -y])
        return collide
