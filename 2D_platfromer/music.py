import pygame


class Music:
    """
    Handles the music and sound effects for the game.

    Attributes:
    - sound_portal: A pygame.mixer.Sound object for portal-related sounds.
    - sound_bullet: A pygame.mixer.Sound object for bullet-related sounds.
    - sound_gameover: A pygame.mixer.Sound object for the game over sound.
    - sound_rocket: A pygame.mixer.Sound object for rocket launch sounds.

    Methods:
    - __init__(): Initializes the Music object, loads music, and sets volume levels.
    """

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("music/gamemusicfinal.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.sound_portal = pygame.mixer.Sound("music/Portal.mp3")
        self.sound_portal.set_volume(10)
        self.sound_bullet = pygame.mixer.Sound("music/Balle.mp3")
        self.sound_bullet.set_volume(0.1)
        self.sound_gameover = pygame.mixer.Sound("music/Game-Over-sound-effect.mp3")
        self.sound_rocket = pygame.mixer.Sound("music/Rocket launcher sound effect.mp3")
