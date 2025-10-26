import pygame

from entity import Entity


class Bot(Entity):
    """
    Represents an enemy bot in the game.

    Attributes:
    - stand_image: The default image of the bot.
    - jump_image: The image displayed when the bot is jumping.
    - walk_cycle: List of images representing the walking animation frames for the bot.
    - animation_index: Index to track the current animation frame.
    - facing_left: Flag indicating whether the bot is facing left.
    - speed: The horizontal speed at which the bot moves.
    - jump_speed: The vertical speed at which the bot jumps.
    - vsp: Vertical speed (current velocity in the vertical direction).
    - gravity: The gravitational force affecting the bot.
    - init_x, init_y: Initial position of the bot.
    - end_x, end_y: Destination position of the bot.
    - direction: Direction in which the bot is initially moving ("Right", "Left", "GoBack").
    - arrive: Flag indicating whether the bot has reached its destination.
    - gohome: Flag indicating whether the bot should return home after reaching its destination.
    - destroy: Flag indicating whether the bot should be destroyed.

    Methods:
    - __init__(startx, starty, endx, endy, direction, gohome=True): Initializes the Bot object with specified parameters.
    - move(x, y, boxes, bullets, bullet_left, bullet_right, player): Moves the bot and handles collisions.
    - update(boxes, bullets, bullet_left, bullet_right, player): Updates the bot's state and behavior.
    - walk_animation(): Updates the walking animation of the bot.
    - returnhome(): Moves the bot back to its initial position.
    - move_GoBack(): Handles the "GoBack" movement behavior of the bot.
    - undestroy(): Resets the destroy flag, preventing the bot from being destroyed.
    """

    def __init__(self, startx, starty, endx, endy, direction, gohome=True):
        """
        Initializes the Bot object with specified parameters.

        Parameters:
        - startx (int): The initial x-coordinate of the bot.
        - starty (int): The initial y-coordinate of the bot.
        - endx (int): The destination x-coordinate of the bot.
        - endy (int): The destination y-coordinate of the bot.
        - direction (str): The initial direction in which the bot moves ("Right", "Left", "GoBack").
        - gohome (bool): Flag indicating whether the bot should return home after reaching its destination (default is True).
        """
        super().__init__(
            "enemy_sprites/alien_walk_1.png",
            startx,
            starty,
            [
                "enemy_sprites/alien_walk_1.png",
                "enemy_sprites/alien_walk_2.png",
                "enemy_sprites/alien_walk_3.png",
                "enemy_sprites/alien_walk_4.png",
                "enemy_sprites/alien_walk_5.png",
                "enemy_sprites/alien_walk_6.png",
                "enemy_sprites/alien_walk_7.png",
                "enemy_sprites/alien_walk_8.png",
                "enemy_sprites/alien_walk_9.png",
            ],
        )

        self.stand_image = self.image
        self.jump_image = pygame.image.load("enemy_sprites/alien_walk_1.png")
        # self.walk_cycle = [
        #     pygame.image.load(f"sprites/p1_walk.png") for i in range(1, 12)
        # ]

        self.walk_cycle = [pygame.image.load(f"{image}") for image in self.png_walk]

        self.animation_index = 0
        self.facing_left = True

        self.speed = 3
        self.jumpspeed = 20
        self.vsp = 0  # vertical speed
        self.gravity = 1
        self.init_x = startx
        self.init_y = starty
        self.end_x = endx
        self.end_y = endy
        self.direction = direction
        self.arrive = False
        self.gohome = gohome
        self.destroy = False

    def move(self, x, y, boxes, bullets, bullet_left, bullet_right, player):
        """
        Moves the bot and handles collisions.

        Parameters:
        - x (int): The horizontal distance to move.
        - y (int): The vertical distance to move.
        - boxes (pygame.sprite.Group): Group of boxes in the game.
        - bullets (pygame.sprite.Group): Group of bullets in the game.
        - bullet_left (Projectile): Left bullet object.
        - bullet_right (Projectile): Right bullet object.
        - player (Player): The player object.
        """
        dx = x
        dy = y
        while self.check_collision(0, dy, boxes):
            if dy > 0:
                dy -= 1
            elif dy < 0:
                dy -= -1
            else:
                dy = 0
        while self.check_collision(dx, dy, boxes):
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx -= -1
            else:
                dx = 0
        self.rect.move_ip([dx, dy])
        if self.check_collision(x, y, bullets):
            bullet_right.return_player(player)
            bullet_left.return_player(player)
            if self.gohome:
                self.returnhome()
            else:
                self.destroy = True
        if self.destroy:
            self.rect.move_ip([15000, 0])

    def update(self, boxes, bullets, bullet_left, bullet_right, player):
        """
        Updates the bot's state and behavior.

        Parameters:
        - boxes (pygame.sprite.Group): Group of boxes in the game.
        - bullets (pygame.sprite.Group): Group of bullets in the game.
        - bullet_left (Projectile): Left bullet object.
        - bullet_right (Projectile): Right bullet object.
        - player (Player): The player object.
        """
        self.hsp = 0  # horizontal speed
        onground = pygame.sprite.spritecollideany(self, boxes)
        self.walk_animation()
        if self.direction == "Right":
            self.move_right()
        if self.direction == "Left":
            self.move_left()
        if self.direction == "GoBack":
            self.move_GoBack()

        if self.vsp < 10 and not onground:  # 9.8 rounded up
            self.vsp += self.gravity
        # stop falling when the ground is reached
        if self.vsp > 0 and onground:
            self.vsp = 0
        # Condition de deplacement
        if self.rect.y > self.end_y:
            self.returnhome()
        self.move(self.hsp, self.vsp, boxes, bullets, bullet_left, bullet_right, player)

    def walk_animation(self):
        """
        Updates the walking animation of the bot.
        """
        self.image = self.walk_cycle[self.animation_index]
        if not self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle) - 1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def returnhome(self):
        """
        Moves the bot back to its initial position.
        """
        self.rect.x = self.init_x
        self.rect.y = self.init_y

    def move_GoBack(self):
        """
        Handles the "GoBack" movement behavior of the bot.
        """
        if self.rect.x >= self.end_x:
            self.arrive = True
        if self.rect.x <= self.init_x:
            self.arrive = False
        if self.arrive == False:
            self.move_right()
        if self.arrive == True:
            self.move_left()

    def undestroy(self):
        """
        Resets the destroy flag, preventing the bot from being destroyed.
        """
        self.destroy = False
