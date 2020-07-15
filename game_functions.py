import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets, bullet):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            ship.moving_left = True

        if event.key == pygame.K_RIGHT:
            ship.moving_right = True

        if event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets, bullet)

        if event.key == pygame.K_q:
            sys.exit()


# elif event.key==pygame.K_DOWN:
# ship.moving_down=True
# elif event.key==pygame.K_UP:
# ship.moving_up=True


def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False


# elif event.key==pygame.K_DOWN:
# ship.moving_down=False
# elif event.key==pygame.K_UP:
# ship.moving_up=False


def check_events(ai_settings, screen, ship, bullets, bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        check_keydown_events(event, ai_settings, screen, ship, bullets, bullet)

        check_keyup_events(event, ship)


# elif event.type==pygame.KEYDOWN:
# if event.key==pygame.K_RIGHT and event.key==pygame.K_LEFT:
# ship.moving_right=False
# ship.moving_left=False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.blit(ai_settings.bg_image, (0, 0))
    # screen.fill(ai_settings.bg_color_1)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens, alien_hit):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

    check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens, alien_hit)


def check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens, alien_hit):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        alien_hit.play()

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets, bullet):
    if len(bullets) < ai_settings.bullets_allowed:
        # pygame.mixer.music.load('audio/bullet.mp3')
        # pygame.mixer.music.play()
        bullet.play()
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = available_space_x / (2 * alien_width)
    return number_alien_x


def get_row_number_y(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    row_number_y = available_space_y / (2 * alien_height)
    return row_number_y


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    # alien.y = alien_height+2*alien_height*row_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(screen, ai_settings)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    row_number_y = get_row_number_y(ai_settings, alien.rect.height, ship.rect.height)

    for row_number in range(int(row_number_y)):
        for alien_number in range(int(number_alien_x)):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, ship1_hit):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship Hit!!!!!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, ship1_hit)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, ship1_hit)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, ship1_hit):
    if stats.ships_left >= 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        ship1_hit.play()

        sleep(1)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, ship1_hit):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, ship1_hit)
            break


