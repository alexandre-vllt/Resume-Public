import pygame

from entity import Entity


class Player(Entity):
    def __init__(self, startx, starty):
        """
        Initialize a Player object.

        Parameters:
            startx (int): The initial x-coordinate of the player.
            starty (int): The initial y-coordinate of the player.
        """
        super().__init__(
            "character_sprites/u_walk1.png",
            startx,
            starty,
            [
                "character_sprites/u_walk1.png",
                "character_sprites/u_walk2.png",
                "character_sprites/u_walk3.png",
                "character_sprites/u_walk4.png",
                "character_sprites/u_walk5.png",
                "character_sprites/u_walk6.png",
                "character_sprites/u_walk7.png",
                "character_sprites/u_walk8.png",
                "character_sprites/u_walk9.png",
                "character_sprites/u_walk10.png",
                "character_sprites/u_walk11.png",
            ],
        )
        self.stand_image = self.image
        self.jump_image = pygame.image.load("character_sprites/u_walk1.png")
        self.armed_image = pygame.image.load("character_sprites/u_walk_armed1.png")
        # self.walk_cycle = [
        #     pygame.image.load(f"sprites/p1_walk.png") for i in range(1, 12)
        # ]

        png_walk_armed = [
            "character_sprites/u_walk_armed1.png",
            "character_sprites/u_walk_armed2.png",
            "character_sprites/u_walk_armed3.png",
            "character_sprites/u_walk_armed4.png",
            "character_sprites/u_walk_armed5.png",
            "character_sprites/u_walk_armed6.png",
            "character_sprites/u_walk_armed7.png",
            "character_sprites/u_walk_armed8.png",
            "character_sprites/u_walk_armed9.png",
            "character_sprites/u_walk_armed10.png",
            "character_sprites/u_walk_armed11.png",
        ]

        self.walk_cycle = [pygame.image.load(f"{image}") for image in self.png_walk]
        self.walk_cycle_armed = [
            pygame.image.load(f"{image}") for image in png_walk_armed
        ]

        self.animation_index = 0
        self.facing_left = False

        self.speed = 2
        self.min_jumpspeed = 3
        self.jumpspeed = 15
        self.hsp = 0
        self.vsp = 0  # vertical speed
        self.gravity = 1
        self.prev_key = pygame.key.get_pressed()
        self.tir = 0

    def check_game_over_collision(self):
        """
        Check if the player collides with the bottom of the screen.

        Returns:
            bool: True if the player collides with the bottom, False otherwise.
        """
        return self.rect.y >= 750

    def move(self, x, y, boxes, enemy, mboxes, portals, sound_portal):
        """
        Move the player based on the given x and y values, checking collisions with various elements.

        Parameters:
            x (int): The change in the x-coordinate.
            y (int): The change in the y-coordinate.
            boxes (pygame.sprite.Group): Group of boxes in the game.
            enemy (pygame.sprite.Group): Group of enemies in the game.
            mboxes (pygame.sprite.Group): Group of mbox instances in the game.
            portals (pygame.sprite.Group): Group of portal instances in the game.
            sound_portal (pygame.mixer.Sound): Sound effect for portal collisions.

        Returns:
            Tuple[bool, bool]: Two boolean values indicating collision with enemy and mbox.
        """
        collision = False
        collision_mboxes = False
        if self.check_collision(x, y, enemy):
            collision = True
        if self.check_collision(x, y, mboxes):
            collision_mboxes = True

        dx = x
        dy = y

        while self.check_collision(0, dy, boxes) or self.check_collision(0, dy, mboxes):
            if dy > 0:
                dy -= 1
            elif dy < 0:
                dy -= -1
            else:
                dy = 0
        while self.check_collision(dx, dy, boxes) or self.check_collision(
            dx, dy, mboxes
        ):
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx -= -1
            else:
                dx = 0
        self.rect.move_ip([dx, dy])
        self.check_collison_portals(x, y, portals, sound_portal)
        return collision, collision_mboxes

    def variable_jump(self, key):
        """
        Adjust the vertical speed for variable height jumping.

        Parameters:
            key (pygame.key): The current state of the keys.

        Note:
            This method modifies the `vsp` attribute of the player.
        """
        if self.prev_key[pygame.K_UP] and not key[pygame.K_UP]:
            if self.vsp < -self.min_jumpspeed:
                self.vsp = -self.min_jumpspeed
        self.prev_key = key

    def apply_gravity(self, onground, upperground):
        """
        Apply gravity to the player's vertical speed.

        Parameters:
            onground (bool): Whether the player is on the ground.
            upperground (bool): Whether there is a block above the player.
        """
        if self.vsp < 5 and not onground:  # 9.8 rounded up
            self.jump_animation()
            self.vsp += self.gravity

        if onground and self.vsp > 0:
            self.vsp = 0

        if upperground and self.vsp <= 0:
            self.vsp = 0

    def update(self, boxes, enemy, mboxes, portals, sound_portal):
        """
        Update the player's position and state based on user input and collisions.

        Parameters:
            boxes (pygame.sprite.Group): Group of boxes in the game.
            enemy (pygame.sprite.Group): Group of enemies in the game.
            mboxes (pygame.sprite.Group): Group of mbox instances in the game.
            portals (pygame.sprite.Group): Group of portal instances in the game.
            sound_portal (pygame.mixer.Sound): Sound effect for portal collisions.

        Returns:
            Tuple[bool, bool]: Two boolean values indicating collision with enemy and mbox.
        """
        self.hsp = 0
        onground = self.check_collision(0, 1, boxes) or self.check_collision(
            0, 1, mboxes
        )
        upperground = self.check_collision(0, -1, boxes) or self.check_collision(
            0, -1, mboxes
        )
        # check keys
        key = pygame.key.get_pressed()
        mbox = mboxes.sprites()[0]

        if key[pygame.K_LEFT] and key[pygame.K_f] and mbox.used:
            self.facing_left = True
            self.walk_animation_armed()
            self.tir = 1
            self.hsp = -self.speed

        elif key[pygame.K_RIGHT] and key[pygame.K_f] and mbox.used:
            self.facing_left = False
            self.walk_animation_armed()
            self.tir = 1
            self.hsp = self.speed

        elif key[pygame.K_f] and mbox.used:
            self.image = self.armed_image
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)
            self.tir = 1

        elif key[pygame.K_LEFT]:
            self.tir = 0
            self.facing_left = True
            self.walk_animation()
            self.hsp = -self.speed

        elif key[pygame.K_RIGHT]:
            self.tir = 0
            self.facing_left = False
            self.walk_animation()
            self.hsp = self.speed

        else:
            self.tir = 0

        if (key[pygame.K_UP] or key[pygame.K_SPACE]) and onground:
            self.vsp = -self.jumpspeed

        # variable height jumping
        self.variable_jump(key)
        # gravity
        self.apply_gravity(onground, upperground)
        # movement
        return self.move(
            self.hsp, self.vsp, boxes, enemy, mboxes, portals, sound_portal
        )

    def walk_animation(self):
        """
        Update the player's image for walking animation.

        Note:
            This method modifies the player's `image` attribute and updates the animation index.
        """
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle) - 1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def walk_animation_armed(self):
        """
        Update the player's image for armed walking animation.

        Note:
            This method modifies the player's `image` attribute and updates the animation index.
        """
        self.image = self.walk_cycle_armed[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle_armed) - 1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def jump_animation(self):
        """
        Update the player's image for jump animation.

        Note:
            This method modifies the player's `image` attribute.
        """
        self.image = self.jump_image
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def update_bullet(self, bullet_left, bullet_right, sound_bullet, boxes, mboxes):
        """
        Update the player's bullets based on user input and collisions.

        Parameters:
            bullet_left (Projectile): The left projectile fired by the player.
            bullet_right (Projectile): The right projectile fired by the player.
            sound_bullet (pygame.mixer.Sound): Sound effect for bullet firing.
            boxes (pygame.sprite.Group): Group of boxes in the game.
            mboxes (pygame.sprite.Group): Group of mbox instances in the game.
        """
        mbox = mboxes.sprites()[0]

        if mbox.used:
            if (
                bullet_right.check_collision(1, 0, boxes)
                or bullet_right.check_collision(1, 0, mboxes)
                or bullet_left.check_collision(-1, 0, boxes)
                or bullet_left.check_collision(-1, 0, mboxes)
            ):  # si une balle touche une box
                bullet_right.return_player(self)
                bullet_left.return_player(self)

            if self.tir == 1 and self.facing_left == True:
                bullet_left.movement = 1
                sound_bullet.play()
                if bullet_right.movement == 0:
                    bullet_right.rect.x = self.rect.x + 13
                    bullet_right.rect.y = self.rect.y + 25

            if self.tir == 1 and self.facing_left == False:
                bullet_right.movement = 1
                sound_bullet.play()
                if bullet_left.movement == 0:
                    bullet_left.rect.x = self.rect.x + 13
                    bullet_left.rect.y = self.rect.y + 25

            if self.tir == 1:
                sound_bullet.play()
                if bullet_right.rect.centerx > 1250:
                    bullet_right.rect.x = self.rect.x + 13
                    bullet_right.rect.y = self.rect.y + 25
                    bullet_right.movement = 0

            if self.tir == 1:
                sound_bullet.play()
                if bullet_left.rect.centerx < -10:
                    bullet_left.rect.x = self.rect.x + 13
                    bullet_left.rect.y = self.rect.y + 25
                    bullet_left.movement = 0

            if self.tir == 0 and bullet_left.movement == 0:
                bullet_left.movement = 0
                bullet_left.rect.x = self.rect.x + 13
                bullet_left.rect.y = self.rect.y + 25

            if self.tir == 0 and bullet_right.movement == 0:
                bullet_right.movement = 0
                bullet_right.rect.x = self.rect.x + 13
                bullet_right.rect.y = self.rect.y + 25

            if bullet_right.movement == 1:
                bullet_right.move(
                    (bullet_right.speed) / 32, 0
                )  # sera appelé 4 fois dans main

            if bullet_left.movement == 1:
                bullet_left.move((-bullet_left.speed) / 32, 0)

    def check_collison_portals(self, x, y, portals, sound_portal):
        """
        Check if the player collides with any portals and initiate teleportation.

        Parameters:
            x (int): The change in the x-coordinate.
            y (int): The change in the y-coordinate.
            portals (pygame.sprite.Group): Group of portal instances in the game.
            sound_portal (pygame.mixer.Sound): Sound effect for portal collisions.
        """
        for portal in portals.sprites():
            if self.check_collision(x, y, pygame.sprite.Group(portal)):
                sound_portal.play()
                self.rect.x = portal.tpx
                self.rect.y = portal.tpy
