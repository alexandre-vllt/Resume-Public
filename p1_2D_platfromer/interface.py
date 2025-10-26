import pygame

from animation import Spaceship, Takeoff
from sprite import Sprite


class New_game(Sprite):
    """
    Represents a sprite for a 'New Game' button in the game menu.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/new_game.png", x, y)


class Start(Sprite):
    """
    Represents a sprite for a 'Start' button in the game menu.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/start_button.png", x, y)

    def activate(self, screen, background):
        """
        Activates the 'Start' button, waiting for user input.

        Parameters:
        - screen: The Pygame display surface.
        - background: The background image to be displayed.

        Returns:
        - bool: True if the game should start, False otherwise.
        """
        begin = False
        new_game = New_game(670, 500)
        while not begin:
            for event in pygame.event.get():
                sourisPos = pygame.mouse.get_pos()  # position de la souris

                if event.type == pygame.QUIT:
                    begin = True
                    return False

                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0] == 1
                ):
                    if (
                        500 < sourisPos[0] < 705 and 450 < sourisPos[1] < 505
                    ):  # on clique sur start
                        begin = True
                        return True

            pygame.event.pump()
            screen.blit(background, (0, 0))
            self.draw(screen)
            new_game.draw(screen)
            pygame.display.flip()


class Play_exit(Sprite):
    """
    Represents a sprite for a 'Play/Exit' button in the game over screen.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/play_exit_button.png", x, y)


class Play(Sprite):
    """
    Represents a sprite for a 'Play' button in the game over screen.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/play_button.png", x, y)


class Exit(Sprite):
    """
    Represents a sprite for an 'Exit' button in the game over screen.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/exit.png", x, y)


class Victory(Sprite):
    """
    Represents a sprite for a victory message in the game over screen.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/victory.png", x, y)


class Game_over(Sprite):
    """
    Represents a sprite for a game over message in the game over screen.

    Parameters:
    - x (int): The initial x-coordinate of the sprite.
    - y (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, x, y):
        super().__init__("menu_sprites/game_over.png", x, y)

    def activate(self, screen, background):
        """
        Activates the 'Game Over' screen, waiting for user input.

        Parameters:
        - screen: The Pygame display surface.
        - background: The background image to be displayed.

        Returns:
        - bool: True if the game should restart, False otherwise.
        """
        running_2 = True  # si on reste dans la partie écran avec game over
        while running_2:
            for event in pygame.event.get():
                sourisPos = pygame.mouse.get_pos()  # position de la souris

                if event.type == pygame.QUIT:
                    running_2 = False
                    return False

                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0] == 1
                ):  # handle MOUSEBUTTONUP
                    if (
                        510 < sourisPos[0] < 695 and 610 < sourisPos[1] < 675
                    ):  # on clique sur quit
                        running_2 = False
                        return False

                    elif (
                        510 < sourisPos[0] < 695 and 500 < sourisPos[1] < 570
                    ):  # on clique sur play
                        running_2 = False
                        return True
            pygame.event.pump()
            screen.blit(background, (0, 0))
            Play_exit(600, 600).draw(screen)
            self.draw(screen)
            pygame.display.flip()


class Player_exit(Sprite):
    """
    Represents a sprite for a player exit (spaceship) in the game.

    Parameters:
    - startx (int): The initial x-coordinate of the sprite.
    - starty (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, startx, starty):
        super().__init__("box_sprites/spaceship.png", startx, starty)
        self.open = True

    def activate(self, screen, background, map, vect_score):
        """
        Activates the player exit sequence, displaying the spaceship taking off.

        Parameters:
        - screen: The Pygame display surface.
        - background: The background image to be displayed.
        - map: An instance of the game map.
        - vect_score: A list of scores from previous game sessions.

        Returns:
        - bool: True if the game should restart, False otherwise.
        """
        takeoff = Takeoff(self.rect.x + 25, self.rect.y + 75)
        while takeoff.rect.y > -100:
            screen.blit(background, (0, 0))
            takeoff.update()
            takeoff.draw(screen)
            map.enemys.draw(screen)
            map.boxes.draw(screen)
            map.mboxes.draw(screen)
            pygame.display.flip()
        spaceship = Spaceship(-100, 100)
        running_2 = True  # si on reste dans la partie écran avec game over
        while running_2:
            for event in pygame.event.get():
                sourisPos = pygame.mouse.get_pos()  # position de la souris

                if event.type == pygame.QUIT:
                    running_2 = False
                    return False

                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0] == 1
                ):  # handle MOUSEBUTTONUP
                    if (
                        900 < sourisPos[0] < 1100 and 650 < sourisPos[1] < 750
                    ):  # on clique sur quit
                        running_2 = False
                        return False

                    elif (
                        100 < sourisPos[0] < 300 and 650 < sourisPos[1] < 750
                    ):  # on clique sur play
                        running_2 = False
                        return True

            pygame.event.pump()
            screen.blit(background, (0, 0))
            # la fusee vole
            spaceship.update()
            spaceship.draw(screen)

            # Affichage du score a la fin de la partie
            font_path = "police/Starting Machine.ttf"
            font = pygame.font.Font(font_path, 36)
            if vect_score:
                last_score = vect_score[-1]
                last_score_surface = font.render(
                    f"VOTRE SCORE : {last_score} S", False, (255, 255, 255)
                )
                screen.blit(last_score_surface, (410, 420))
            # screen.fill(BACKGROUND)
            Play(200, 700).draw(screen)
            Exit(1000, 700).draw(screen)
            Victory(640, 330).draw(screen)
            pygame.display.flip()


class Button(Sprite):
    """
    Represents a generic sprite for a button in the game.

    Parameters:
    - startx (int): The initial x-coordinate of the sprite.
    - starty (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, startx, starty):
        super().__init__("menu_sprites/lock.png", startx, starty)
        self.lock = True

    def open(self):
        """Opens the button, making it interactable."""
        self.image = pygame.image.load("menu_sprites/playable.png")
        self.lock = False

    def close(self):
        """Closes the button, making it non-interactable."""
        self.image = pygame.image.load("menu_spriteslock.png")
        self.lock = True


class Exit(Sprite):
    def __init__(self, startx, starty):
        super().__init__("menu_sprites/exit.png", startx, starty)


class Selection(Sprite):
    """
    Represents a sprite for the game level selection screen.

    """

    def __init__(self):
        super().__init__("menu_sprites/soucoup.png", 600, 400)
        self.buttons = [
            Button(300, 600),
            Button(800, 600),
            Button(850, 170),
            Button(300, 200),
        ]
        self.buttons[0].open()

    def activation(self, screen, running0):
        """
        Activates the level selection screen, waiting for user input.

        Parameters:
        - screen: The Pygame display surface.
        - running0: Flag indicating if the game is running.

        Returns:
        - Tuple: A tuple containing the selected level index and a flag indicating
          if the game should continue running.
        """
        background = pygame.image.load("background/select_background.png.png")
        exit = Exit(600, 750)

        running_2 = True  # si on reste dans la partie écran avec game over
        while running_2:
            key = pygame.key.get_pressed()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()  # position de la souri
                if event.type == pygame.QUIT:
                    return 0, False

                if key[pygame.K_r]:
                    for i in range(4):
                        self.buttons[i].open()

                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.mouse.get_pressed()[0] == 1
                ):  # handle MOUSEBUTTONUP
                    for i in range(4):
                        if (
                            self.buttons[i].rect.collidepoint(pos)
                            and not self.buttons[i].lock
                        ):
                            return i, True
                    if exit.rect.collidepoint(pos):
                        return 0, False

            pygame.event.pump()
            screen.blit(background, (0, 0))
            self.draw(screen)
            exit.draw(screen)
            for b in self.buttons:
                b.draw(screen)
            pygame.display.flip()


class New_gun(Sprite):
    """
    Represents a sprite for a new gun item in the game.

    Parameters:
    - startx (int): The initial x-coordinate of the sprite.
    - starty (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, startx, starty):
        super().__init__("sprites/new_item.png", startx, starty)


class Press_f_to_use2(Sprite):
    """
    Represents a sprite for a visual prompt to press 'F' to use an item in the game.

    Parameters:
    - startx (int): The initial x-coordinate of the sprite.
    - starty (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, startx, starty):
        super().__init__("sprites/press_f_to_use2.png", startx, starty)


class Press_f_to_use(Sprite):
    """
    Represents a sprite for a visual prompt to press 'F' to use an item in the game.
    Activating this prompt restarts the game.

    Parameters:
    - startx (int): The initial x-coordinate of the sprite.
    - starty (int): The initial y-coordinate of the sprite.
    """

    def __init__(self, startx, starty):
        super().__init__("sprites/press_f_to_use.png", startx, starty)

    def activate(self, screen, map, player):
        """
        Activates the 'Press_f_to_use' prompt.

        Parameters:
        - screen: The Pygame display surface.
        - map: An instance of the game map.
        - player: An instance of the player character.

        Returns:
        - bool: True if the game should be restarted, False otherwise.
        """
        running_3 = True
        rose_ou_jaune = 0
        while running_3:
            key = pygame.key.get_pressed()
            new_gun = New_gun(630, 100)
            press_f_to_use2 = Press_f_to_use2(640, 300)
            screen.blit(map.background, (0, 0))
            map.boxes.draw(screen)
            map.mboxes.draw(screen)
            map.enemys.draw(screen)
            map.player_exit.draw(screen)
            player.draw(screen)
            new_gun.draw(screen)
            rose_ou_jaune += 1
            if rose_ou_jaune < 2:
                self.draw(screen)
            elif rose_ou_jaune < 4:
                press_f_to_use2.draw(screen)
            else:
                press_f_to_use2.draw(screen)
                rose_ou_jaune = 0

            pygame.display.flip()

            for event in pygame.event.get():
                if key[pygame.K_f]:
                    running_3 = False  # le jeu se relance
