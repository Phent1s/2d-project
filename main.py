import pygame
import sys
import math

pygame.init()

window_width = 1280
window_length = 720

screen = pygame.display.set_mode((window_width, window_length))
pygame.display.set_caption('Тест1')

pygame.mixer.music.load('Medieval Vol. 2 6.mp3')
pygame.mixer.music.play(-1)  # -1 означает бесконечное повторение
sound_effect = pygame.mixer.Sound('swinging-staff-whoosh-strong-08-44658.mp3')

# Загрузите анимацию атаки персонажа
attack1 = pygame.image.load('Attack 1.png')
attack2 = pygame.image.load('Attack 2.png')
attack3 = pygame.image.load('Attack 3.png')
attack4 = pygame.image.load('Attack 4.png')

# Измените размеры кадров атаки
attack1 = pygame.transform.scale(attack1, (200, 240))
attack2 = pygame.transform.scale(attack2, (220, 240))
attack3 = pygame.transform.scale(attack3, (140, 240))
attack4 = pygame.transform.scale(attack4, (220, 240))

# Создайте список кадров атаки
attack_animation_frames = [attack1, attack2, attack3, attack4]

# Установите начальные значения
is_attacking = False  # Переменная для отслеживания состояния атаки
attack_frame_index = 0  # Индекс текущего кадра атаки
attack_animation_speed = 100  # Более быстрая смена кадров атаки в миллисекундах
attack_duration = len(attack_animation_frames) * attack_animation_speed  # Длительность атаки

hero = pygame.image.load('HERO_afk.png')
background = pygame.image.load('game_background_1.png')

slime1 = pygame.image.load('slime-idle-1.png')
slime1 = pygame.transform.scale(slime1, (120, 120))
slime_speed = 1  # Скорость движения слайма

slime_move0 = pygame.image.load('slime-move-0.png')
slime_move1 = pygame.image.load('slime-move-1.png')
slime_move2 = pygame.image.load('slime-move-2.png')
slime_move3 = pygame.image.load('slime-move-3.png')

slime_move0 = pygame.transform.scale(slime_move0, (120, 120))
slime_move1 = pygame.transform.scale(slime_move1, (120, 120))
slime_move2 = pygame.transform.scale(slime_move2, (120, 120))
slime_move3 = pygame.transform.scale(slime_move3, (120, 120))
frame_index_slime = 0
slime_animation_speed = 130  # Время в миллисекундах между сменой кадров

slime_animation_frames = [slime_move0, slime_move1, slime_move2, slime_move3]

is_slime_attacking = False
slime_attack_frame_index = 0
slime_attack_start_time = -2  # Добавьте эту переменную для отслеживания времени начала атаки слизня
attack_threshold_distance = 70 # Расстояние для атаки слайма (от центра персонажа до слайма)

Run1 = pygame.image.load('ven/Run_1.png')
Run2 = pygame.image.load('ven/Run_2.png')
Run3 = pygame.image.load('ven/Run_3.png')
Run4 = pygame.image.load('ven/Run_4.png')
Run5 = pygame.image.load('ven/Run_5.png')
Run6 = pygame.image.load('ven/Run_6.png')
Run7 = pygame.image.load('ven/Run_7.png')

# Slime attack animation

slime_attack0 = pygame.image.load('ven/slime-attack-0.png')
slime_attack1 = pygame.image.load('ven/slime-attack-1.png')
slime_attack2 = pygame.image.load('ven/slime-attack-2.png')
slime_attack3 = pygame.image.load('ven/slime-attack-3.png')
slime_attack4 = pygame.image.load('ven/slime-attack-4.png')

slime_attack0 = pygame.transform.scale(slime_attack0, (120, 120))
slime_attack1 = pygame.transform.scale(slime_attack1, (120, 120))
slime_attack2 = pygame.transform.scale(slime_attack2, (120, 120))
slime_attack3 = pygame.transform.scale(slime_attack3, (120, 120))
slime_attack4 = pygame.transform.scale(slime_attack4, (120, 120))

slime_attack_animations_frames = [slime_attack0, slime_attack1, slime_attack2, slime_attack3, slime_attack4]
slime_attack_animation_speed = 130

background = pygame.transform.scale(background, (1280, 720))
hero = pygame.transform.scale(hero, (240, 240))
Run1 = pygame.transform.scale(Run1, (140, 240))
Run2 = pygame.transform.scale(Run2, (140, 240))
Run3 = pygame.transform.scale(Run3, (160, 240))
Run4 = pygame.transform.scale(Run4, (160, 240))
Run5 = pygame.transform.scale(Run5, (160, 240))
Run6 = pygame.transform.scale(Run6, (160, 240))
Run7 = pygame.transform.scale(Run7, (160, 240))

screen.blit(background, (0, 0))
slime1_x = 1000
slime1_y = 400
hero_x = 80
hero_y = 290

hero_width = hero.get_width()
hero_height = hero.get_height()

speed = 3

animation_frames_right = [Run1, Run2, Run3, Run4, Run5, Run6, Run7]
frame_index_right = 0
animation_frames_left = [pygame.transform.flip(frame, True, False) for frame in animation_frames_right]
frame_index_left = 0
animation_speed = 130  # Время в миллисекундах между сменой кадров
last_hero_update_time = pygame.time.get_ticks()
last_slime_update_time = pygame.time.get_ticks()
current_hero_frame = hero
current_slime_frame = slime1

direction = "right"  # Направление движения (right или left)

bottom_limit = 380
top_limit = 100

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_attacking:
            is_attacking = True
            attack_start_time = pygame.time.get_ticks()
            attack_frame_index = 0
            sound_effect.play()

    if is_attacking:
        current_time = pygame.time.get_ticks()
        if current_time - attack_start_time >= attack_duration:
            is_attacking = False
            attack_frame_index = 0
            # После завершения анимации атаки, персонаж вернется в статичное положение
            current_hero_frame = hero

        else:
            attack_frame_index = (current_time - attack_start_time) // attack_animation_speed
            if attack_frame_index < len(attack_animation_frames):
                current_hero_frame = attack_animation_frames[attack_frame_index]
            else:
                is_attacking = False
                attack_frame_index = 0
                current_hero_frame = hero

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        hero_x += speed
        direction = "right"
        if hero_x < 0:
            hero_x = 0
        current_time = pygame.time.get_ticks()
        if current_time - last_hero_update_time >= animation_speed:
            last_hero_update_time = current_time
            frame_index_right = (frame_index_right + 1) % len(animation_frames_right)
            current_hero_frame = animation_frames_right[frame_index_right]

    elif keys[pygame.K_a]:
        hero_x -= speed
        direction = "left"
        if hero_x < 0:
            hero_x = 0
        current_time = pygame.time.get_ticks()
        if current_time - last_hero_update_time >= animation_speed:
            last_hero_update_time = current_time
            frame_index_left = (frame_index_left + 1) % len(animation_frames_left)
            current_hero_frame = animation_frames_left[frame_index_left]

    elif keys[pygame.K_s]:
        hero_y += speed
        direction = "down"
        if hero_y > bottom_limit:
            hero_y = bottom_limit
        if hero_y < 0:
            hero_y = 0
        current_time = pygame.time.get_ticks()
        if current_time - last_hero_update_time >= animation_speed:
            last_hero_update_time = current_time
            frame_index_right = (frame_index_right + 1) % len(animation_frames_right)
            current_hero_frame = animation_frames_right[frame_index_right]

    elif keys[pygame.K_w]:
        hero_y -= speed
        direction = "up"
        if hero_y < top_limit:
            hero_y = top_limit
        if hero_y < 0:
            hero_y = 0
        current_time = pygame.time.get_ticks()
        if current_time - last_hero_update_time >= animation_speed:
            last_hero_update_time = current_time
            frame_index_right = (frame_index_right + 1) % len(animation_frames_right)
            current_hero_frame = animation_frames_right[frame_index_right]

    # Если ни одна из клавиш не нажата и атака не выполняется, то анимация остается статичной
    if not any(keys) and not is_attacking:
        current_hero_frame = hero

    hero_center_x = hero_x + hero_width // 2
    hero_center_y = hero_y + hero_height // 2
    slime_center_x = slime1_x + slime1.get_width() // 2
    slime_center_y = slime1_y + slime1.get_height() // 2

    angle = math.atan2(hero_center_y - slime_center_y, hero_center_x - slime_center_x)

    # Определение направления для разворота слайма
    if slime1_x > hero_x:
        direction_slime = "right"
    else:
        direction_slime = "left"

    slime1_x += slime_speed * math.cos(angle)
    slime1_y += slime_speed * math.sin(angle)

    current_time = pygame.time.get_ticks()
    if current_time - last_slime_update_time >= slime_animation_speed:
        last_slime_update_time = current_time
        frame_index_slime = (frame_index_slime + 1) % len(slime_animation_frames)

    # Разворот модельки слайма в соответствии с направлением
    if direction_slime == "right":
        current_slime_frame = slime_animation_frames[frame_index_slime]
    elif direction_slime == "left":
        current_slime_frame = pygame.transform.flip(slime_animation_frames[frame_index_slime], True, False)

    # Проверка, если слизень находится достаточно близко к герою, начать атаку слизня
    distance_to_hero = math.dist((slime_center_x, slime_center_y), (hero_center_x, hero_center_y))
    if distance_to_hero < attack_threshold_distance:
        is_slime_attacking = True
        slime_attack_start_time = pygame.time.get_ticks()
        slime_attack_frame_index = 0

    if is_slime_attacking:
        if slime_attack_frame_index < len(slime_attack_animations_frames):
            current_slime_frame = slime_attack_animations_frames[slime_attack_frame_index]
            slime_attack_frame_index += 1
        else:
            is_slime_attacking = False
            slime_attack_frame_index = 0
            current_slime_frame = slime_animation_frames[frame_index_slime]

    screen.blit(background, (0, 0))
    screen.blit(current_slime_frame, (slime1_x, slime1_y))
    screen.blit(current_hero_frame, (hero_x, hero_y))

    pygame.display.update()
    clock.tick(60)


