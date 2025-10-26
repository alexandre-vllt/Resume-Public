import pygame

from interface import Game_over, Press_f_to_use, Selection, Start
from map import MAPS, Map
from music import Music
from player import Player
from projectile import Projectile

WIDTH = 1200
HEIGHT = 800


def main():
    pygame.init()
    music = Music()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    background = pygame.image.load("background/nasa.png")
    selection = Selection()
    game_over = Game_over(640, 350)
    start = Start(640, 550)
    vect_scores =[]

    # on affiche le menu tant qu'on clique pas sur start
    running0 = start.activate(screen, background)
    if running0 == 1:
        temps_debut_partie = pygame.time.get_ticks()
    while running0:
        lvl, running0 = selection.activation(screen, running0)
        running1 = running0
        temps_debut_partie =pygame.time.get_ticks()

        (matrice, vect_bot, vect_portal, background_map, box_sprite) = MAPS[lvl]
        map = Map(matrice, vect_bot, vect_portal, background_map, box_sprite)

        player = Player(map.spawnx, map.spawny)

        bullet_right = Projectile(player.rect.centerx, player.rect.centery)
        bullet_left = Projectile(player.rect.centerx, player.rect.centery)
        for bot in map.vect_bot:
            map.enemys.add(bot)
        map.bullet.add(bullet_left, bullet_right)
        press_f_to_use = Press_f_to_use(640, 300)

        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                    running0 = False

            pygame.event.pump()
            collision_enemy, collision_mboxes = player.update(
                map.boxes, map.enemys, map.mboxes, map.portals, music.sound_portal
            )
            player.update(
                map.boxes, map.enemys, map.mboxes, map.portals, music.sound_portal
            )
            # appelé plusieurs fois pour pb de passage dans les boxes + fluidité de la bullet
            for i in range(40):
                player.update_bullet(
                    bullet_left, bullet_right, music.sound_bullet, map.boxes, map.mboxes
                )
            map.mboxes.update(collision_mboxes, False)

            screen.blit(map.background, (0, 0))
            # screen.fill(BACKGROUND)

            map.draw(screen, bullet_left, bullet_right, player)
            
            
            # Affiche le temps écoulé en secondes en haut à droite
            temps_actuel = pygame.time.get_ticks()
            temps_passe = (temps_actuel - temps_debut_partie) // 1000  # conversion en secondes
            font_path = "police/Starting Machine.ttf"
            font = pygame.font.Font(font_path, 36)
            temps_surface = font.render(f"Score : {temps_passe} s", True, (255, 255, 255))
            screen.blit(temps_surface, (WIDTH - 200, 20))
            
            pygame.display.flip()

            # tape la mbox pour la premiere fois, on active le message
            if map.mboxes.sprites()[0].first_use and map.mboxes.sprites()[0].used:
                press_f_to_use.activate(screen, map, player)
                map.mboxes.sprites()[0].first_use = False

            # sortie du décor = game over
            if player.check_game_over_collision() or collision_enemy:
                music.sound_gameover.play()
                for bot in map.vect_bot:
                    bot.undestroy()
                    bot.returnhome()
                    bot.draw(screen)
                map.mboxes.update(collision_mboxes, True)
                running1 = game_over.activate(screen, map.background)
                if running1:
                    temps_debut_partie =pygame.time.get_ticks()
                map.mboxes.sprites()[0].first_use = True
                player = Player(map.spawnx, map.spawny)
                bullet_left.return_player(player)
                bullet_right.return_player(player)
                music.sound_gameover.stop()

            # rencontre avec la fusée = sortie
            if pygame.sprite.collide_mask(player, map.player_exit):
                vect_scores.append(temps_passe)
                music.sound_rocket.play()
                for bot in map.vect_bot:
                    bot.undestroy()
                    bot.returnhome()
                    bot.draw(screen)
                map.mboxes.update(collision_mboxes, True)
                running1 = False
                running0 = map.player_exit.activate(screen, map.background, map,vect_scores)
                if running0:
                    temps_debut_partie =pygame.time.get_ticks()
                if lvl < 3:
                    selection.buttons[lvl + 1].open()
                player = Player(map.spawnx, map.spawny)
                bullet_left.return_player(player)
                bullet_right.return_player(player)
                music.sound_rocket.stop()
            clock.tick(60)

    pygame.display.quit()
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
