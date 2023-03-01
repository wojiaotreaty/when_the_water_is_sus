# When The Water Is Sus
# Hydro duduStream Production
# developers: Daniel Lee, William Liu
# audio by: Kyle Sung

import pygame, os, sys
from pygame import mixer

from random import *

# pygame initialize
pygame.init()
pygame.mixer.init()

# fullscreen display
WIDTH, HEIGHT = pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1]

# player info and UNITs
mc = pygame.image.load(os.path.join('Assets', 'roguelike_mc.png'))
mc = pygame.transform.scale(mc, ((int((HEIGHT) / 13), int(HEIGHT / 10))))
UNIT = mc.get_height()
RL = UNIT * 10
# coordinates of the player
mc_x = int(WIDTH / 2)
mc_y = int(HEIGHT / 2) - int((int(HEIGHT / 10) * (2 / 3)))

# general
# sets the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT - int(HEIGHT / 15)))
pygame.display.set_caption("When The Water Is Sus")

# credit images
title_credit = pygame.image.load(os.path.join('Assets', 'team_name.png'))
title_credit = pygame.transform.scale(title_credit, (UNIT * 6.5, UNIT * 0.35))

end_credit = pygame.image.load(os.path.join('Assets', 'names_credit.png'))
end_credit = pygame.transform.scale(end_credit, (UNIT * 3.7, UNIT * 0.35))

# title images
title_1 = pygame.image.load(os.path.join('Assets', 'title_1.png'))
title_1 = pygame.transform.scale(title_1, (UNIT * 15, UNIT * 0.7))
shadow = pygame.image.load(os.path.join('Assets', 'title_2.png'))
shadow = pygame.transform.scale(shadow, (UNIT * 15, UNIT * 0.7))

start_img = pygame.image.load(os.path.join('Assets', 'press_enter.png'))
start_img = pygame.transform.scale(start_img, (UNIT * 6.8, UNIT * 1.5))

# death screan image
death_img = pygame.image.load(os.path.join('Assets', 'death.jpg'))
death_img = pygame.transform.scale(death_img, (WIDTH, HEIGHT))

# start menu image
cave_img = pygame.image.load(os.path.join('Assets', 'cave_img.png'))
cave_img = pygame.transform.scale(cave_img, (WIDTH, HEIGHT))
# sprites
ground_img = pygame.image.load(os.path.join('Assets', 'ground.png'))
ground_img = pygame.transform.scale(ground_img, (UNIT, UNIT))
wall_img = pygame.image.load(os.path.join('Assets', 'wall.png'))
wall_img = pygame.transform.scale(wall_img, (UNIT, UNIT))
chest_img = pygame.image.load(os.path.join('Assets', 'ladder.png'))
chest_img = pygame.transform.scale(chest_img, (UNIT, UNIT))
flood_img = pygame.image.load(os.path.join('Assets', 'flood.png'))
flood_img = pygame.transform.scale(flood_img, (UNIT, UNIT))
flood_img = pygame.transform.scale(flood_img, (UNIT, UNIT))
status_box_img = pygame.image.load(os.path.join('Assets', 'status_box.png'))
status_box_img = pygame.transform.scale(status_box_img, (3 * UNIT, (3 * UNIT + 0.15 * UNIT)))

# ladder sfx
ladder_sfx = mixer.Sound(os.path.join('Audio', 'Gamejam_Ladder_Efx_Stereo.mp3'))

# map movement
move_distance = UNIT

# time function
clock = pygame.time.Clock()


# ---------------------------------------------------------------------------------------#


# functions------------------------------------------------------------------------------#
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def draw_window():
    '''
    draws a white background
    '''
    WIN.fill((0, 0, 0))


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def random_coord_generator(num):
    '''
    generates coordinates of where to create rooms
    '''
    temp_adj_rooms = []
    adjacent_rooms = []
    used_rooms = [[0, 0]]

    for i in range(num):
        temp_adj_rooms = []
        adjacent_rooms = []
        for room in used_rooms:
            # all four possible room
            temp_rooms = [[room[0] - 1, room[1]], [room[0] + 1, room[1]], [room[0], room[1] - 1],
                          [room[0], room[1] + 1]]

            for each_room in range(len(temp_rooms)):
                temp_adj_rooms.append(temp_rooms[each_room])

        for each_room in range(len(temp_adj_rooms)):
            if (temp_adj_rooms[each_room] in used_rooms) == False:
                adjacent_rooms.append(temp_adj_rooms[each_room])

        random_index = randrange(0, len(adjacent_rooms))

        used_rooms.append(adjacent_rooms[random_index])

    return used_rooms


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def start_level(num):
    '''
    returns a list of (room_coordinate, room_layout) items for num times, along with elevation of each tile
    '''
    counter = -1
    room_with_ladder = randrange(1, num + 1)

    # list that appends each 'item'
    coord_layout_list = []

    # list of tiles that have '5'
    ladder_made = False

    # coordinate list for num many coordinates
    coordinate_list = random_coord_generator(num)

    # calls each coordinate [x, y] from coordinate_list
    for room_coordinate in coordinate_list:

        # randomly chooses a room layout from list of possible room layouts
        # create a copy of the room layout
        # read file --------------------#
        file = open('Rooms.txt')
        # master list of all the rooms
        linelist = []

        for line in file:
            linelist.append(line.strip().split())

        room_1 = linelist[:10]
        for row in range(len(room_1)):
            for tile in range(len(room_1[row])):
                elevation = randrange(0, 5)
                room_1[row][tile] = [room_1[row][tile], elevation]

        room_2 = linelist[10:20]
        for row in range(len(room_2)):
            for tile in range(len(room_2[row])):
                elevation = randrange(0, 5)
                room_2[row][tile] = [room_2[row][tile], elevation]

        room_3 = linelist[20:30]
        for row in range(len(room_3)):
            for tile in range(len(room_3[row])):
                elevation = randrange(0, 5)
                room_3[row][tile] = [room_3[row][tile], elevation]

        room_4 = linelist[30:40]
        for row in range(len(room_4)):
            for tile in range(len(room_4[row])):
                elevation = randrange(0, 5)
                room_4[row][tile] = [room_4[row][tile], elevation]

        room_5 = linelist[40:50]
        for row in range(len(room_5)):
            for tile in range(len(room_5[row])):
                elevation = randrange(0, 5)
                room_5[row][tile] = [room_5[row][tile], elevation]

        # useless room for now
        treasure_room = linelist[50:60]

        empty_room = linelist[60:70]
        for row in range(len(empty_room)):
            for tile in range(len(empty_room[row])):
                elevation = randrange(0, 5)
                empty_room[row][tile] = [empty_room[row][tile], elevation]

        # list of possible rooms to generate
        possible_rooms = [room_1, room_2, room_3, room_4, room_5]

        if room_coordinate == coordinate_list[0]:
            room_layout = empty_room
        else:
            room_layout = possible_rooms[randrange(len(possible_rooms))]

        counter += 1
        # traverses through each ascii character of the room layout list
        for row in range(len(room_layout)):
            for tile in range(len(room_layout[row])):
                if room_with_ladder != counter:
                    if room_layout[row][tile][0] == '5':
                        room_layout[row][tile].insert(0, '0')
                        room_layout[row][tile].pop(1)

                else:
                    if room_layout[row][tile][0] == '5':
                        room_layout[row][tile].insert(1, 10)
                        room_layout[row][tile].pop(2)

                if room_layout[row][tile][0] == '1':
                    room_layout[row][tile].insert(1, randrange(3, 5))
                    room_layout[row][tile].pop(2)

                # elevation = randrange(0, 5)
                # room_layout[row][tile] = (room_layout[row][tile], elevation)

        coord_layout_list.append((room_coordinate, room_layout))
    return coord_layout_list


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def create_level(x_change, y_change, coord_layout_list, flood_elevation):
    obstacle_list = []
    ground_list = []
    flood_list = []
    ladder_rect_coords = []

    for roomset in range(len(coord_layout_list)):
        x_coord_save = ((coord_layout_list[roomset][0][0]) * RL) + mc_x + x_change - int(
            ((4 / 13) * UNIT) / 2) - 4 * UNIT
        x_coord = x_coord_save
        y_coord_save = ((coord_layout_list[roomset][0][1]) * RL) + mc_y + y_change - 4 * UNIT
        y_coord = y_coord_save

        room_layout = coord_layout_list[roomset][1]

        for row in room_layout:
            for i in range(len(row)):
                if row[i][1] <= flood_elevation:  # flood
                    WIN.blit(flood_img, (x_coord, y_coord))
                    flood_list.append((x_coord, y_coord))
                elif row[i][0] == "0":  # ground
                    WIN.blit(ground_img, (x_coord, y_coord))
                    ground_list.append((x_coord, y_coord))
                elif row[i][0] == "1":  # wall
                    WIN.blit(wall_img, (x_coord, y_coord))
                    obstacle_list.append((x_coord, y_coord))
                else:  # ladder
                    WIN.blit(chest_img, (x_coord, y_coord))
                    ladder_rect_coords.append((x_coord, y_coord))

                x_coord += UNIT
            y_coord += UNIT
            x_coord = x_coord_save

    WIN.blit(mc, (mc_x, mc_y))

    return obstacle_list, ground_list, flood_list, ladder_rect_coords


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def draw_gui():
    # status box
    WIN.blit(status_box_img, (int(UNIT / 10), int(UNIT * 1 / 5)))

    # level gui
    level_text = ingame_font.render("Level: " + str(num_rooms), 1, (54, 31, 13))
    WIN.blit(level_text, (int(UNIT * 3 / 4 - UNIT / 20), int(UNIT * 0.9)))

    # HP gui
    hp_text = ingame_font.render("HP: ", 1, (54, 31, 13))
    WIN.blit(hp_text, (int(UNIT * 3 / 4 - UNIT / 20), int(UNIT * 0.9 + UNIT * 0.5)))
    hp_num = ingame_font.render("      " + str(hp), 1, (139, 0, 0))
    WIN.blit(hp_num, (int(UNIT * 3 / 4 - UNIT / 20), int(UNIT * 0.9 + UNIT * 0.5)))

    # flood gui
    flood_text1 = ingame_font.render("Flood", 1, (54, 31, 13))
    WIN.blit(flood_text1, (int(UNIT * 3 / 4 - UNIT / 20), int(UNIT * 1.9)))
    flood_text2 = ingame_font.render("in: ", 1, (54, 31, 13))
    WIN.blit(flood_text2, (int(UNIT * 3 / 4 - UNIT / 20), int(UNIT * 1.9 + UNIT / 3)))
    flood_num = ingame_font.render("    " + str(actions_left), 1, (0, 0, 139))
    WIN.blit(flood_num, (int(UNIT * 3 / 4 - UNIT / 20 + UNIT / 10), int(UNIT * 1.9 + UNIT / 3)))


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def tile_step():
    var = randrange(0, 5)
    if var == 1:
        tile_sfx = mixer.Sound(os.path.join('Audio', 'tilestep1.mp3'))
        tile_sfx.set_volume(0.8)
        tile_sfx.play()
    elif var == 2:
        tile_sfx = mixer.Sound(os.path.join('Audio', 'tilestep2.mp3'))
        tile_sfx.set_volume(0.8)
        tile_sfx.play()
    elif var == 3:
        tile_sfx = mixer.Sound(os.path.join('Audio', 'tilestep3.mp3'))
        tile_sfx.set_volume(0.8)
        tile_sfx.play()
    elif var == 4:
        tile_sfx = mixer.Sound(os.path.join('Audio', 'tilestep4.mp3'))
        tile_sfx.set_volume(0.8)
        tile_sfx.play()
    elif var == 0:
        tile_sfx = mixer.Sound(os.path.join('Audio', 'tilestep5.mp3'))
        tile_sfx.set_volume(0.8)
        tile_sfx.play()


# ---------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------#
def water_step():
    var = randrange(0, 5)
    if var == 1:
        water_sfx = mixer.Sound(os.path.join('Audio', 'waterstep1.mp3'))
        water_sfx.set_volume(0.8)
        water_sfx.play()
    elif var == 2:
        water_sfx = mixer.Sound(os.path.join('Audio', 'waterstep2.mp3'))
        water_sfx.set_volume(0.8)
        water_sfx.play()
    elif var == 3:
        water_sfx = mixer.Sound(os.path.join('Audio', 'waterstep3.mp3'))
        water_sfx.set_volume(0.8)
        water_sfx.play()
    elif var == 4:
        water_sfx = mixer.Sound(os.path.join('Audio', 'waterstep4.mp3'))
        water_sfx.set_volume(0.8)
        water_sfx.play()
    elif var == 0:
        water_sfx = mixer.Sound(os.path.join('Audio', 'waterstep5.mp3'))
        water_sfx.set_volume(0.8)
        water_sfx.play()


# ---------------------------------------------------------------------------------------#

# fonts--------------------------------------------------------------------#
death_screen_font = pygame.font.SysFont('PKMN RBYGSC', int(2 * UNIT), True)

tutorial_title_font = pygame.font.SysFont('PKMN RBYGSC', int(UNIT), True)

# creating in game display of hp, score... etc
ingame_font = pygame.font.SysFont('PKMN RBYGSC', int(UNIT * 3 / 5), True)
# -------------------------------------------------------------------------#

run = True

# tutorial is one time only
tutorial = True

while run:
    # base case
    getLadder = True
    num_rooms = 0
    left_over_hp = 0

    # --------------------------------------------------------------------------------#
    while tutorial:
        WIN.fill((20, 9, 3))

        tutorial_title = tutorial_title_font.render("TUTORIAL", 1, (255, 255, 255))
        WIN.blit(tutorial_title, (7 * UNIT, int(3 * UNIT / 2)))

        tutorial_info1 = ingame_font.render("You're LOST in a CAVE and a FLOOD BEGINS!", 1, (255, 255, 255))
        WIN.blit(tutorial_info1, (int(3 * UNIT + 0.8 * UNIT), 3 * UNIT))

        tutorial_info2 = ingame_font.render("Oh no! WATER IS EVERYWHERE!", 1, (255, 255, 255))
        WIN.blit(tutorial_info2, (int(5 * UNIT + 0.15 * UNIT), 4 * UNIT))

        tutorial_info3 = ingame_font.render("Quick! Find that LADDER and GO UP!", 1, (255, 255, 255))
        WIN.blit(tutorial_info3, (int(4 * UNIT + 0.7 * UNIT), 5 * UNIT))

        tutorial_info4 = ingame_font.render("*Remaining HP will be added towards the next level", 1, (255, 255, 255))
        WIN.blit(tutorial_info4, (int(3 * UNIT), 7 * UNIT))

        tutorial_info5 = ingame_font.render("Press Enter to Continue", 1, (255, 255, 255))
        WIN.blit(tutorial_info5, (int(6.15 * UNIT), 8 * UNIT))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                run = False

            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                tutorial = False

    # --------------------------------------------------------------------------------------#
    # start music---------------------------------------------------------------------------#
    bgm = mixer.Sound(os.path.join('Audio', 'Gamejam_Song_1_V2.mp3'))
    bgm.set_volume(0.5)
    bgm.play(-1)

    start = True
    while start:
        WIN.blit(cave_img, (0, 0))
        WIN.blit(shadow,
                 ((WIN.get_width() / 2 - shadow.get_width() / 2 + UNIT / 20), (WIN.get_height() / 3 + UNIT / 10)))
        WIN.blit(title_1, ((WIN.get_width() / 2 - title_1.get_width() / 2), WIN.get_height() / 3))

        WIN.blit(start_img, ((WIN.get_width() / 2 - start_img.get_width() / 2 + UNIT / 15), WIN.get_height() * 0.6))

        WIN.blit(title_credit, (WIN.get_width() / 2 - title_credit.get_width() / 2, WIN.get_height() * 0.9))

        pygame.display.update()

        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                run = False

            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                start = False

    # stop start screen music--------------------------------------------#
    pygame.mixer.stop()
    bgm = mixer.Sound(os.path.join('Audio', 'Gamejam_V2.mp3'))
    bgm.set_volume(0.5)
    bgm.play(-1)

    # ----------------------------------------------------------------------------#
    ingame = True
    while ingame:
        draw_window()

        # rectangle hitbox---------------------------------------------------------------#
        mc_rect_center = pygame.Rect((mc_x - (int(UNIT * 4 / 26))), mc_y, UNIT, UNIT)  # hitbox for ladder

        mc_rect_right = pygame.Rect((mc_x - (int(UNIT * 4 / 26)) + UNIT), mc_y, UNIT, UNIT)

        mc_rect_left = pygame.Rect((mc_x - (int(UNIT * 4 / 26)) - UNIT), mc_y, UNIT, UNIT)

        mc_rect_up = pygame.Rect((mc_x - (int(UNIT * 4 / 26))), (mc_y - UNIT), UNIT, UNIT)

        mc_rect_down = pygame.Rect((mc_x - (int(UNIT * 4 / 26))), (mc_y + UNIT), UNIT, UNIT)
        # -------------------------------------------------------------------------------#

        # if the character touches the ladder
        if getLadder:
            num_rooms += 1
            actions_left = 20
            total_actions = 0
            flood_elevation = -1
            coord_layout_list = start_level(num_rooms)
            y_change = 0
            x_change = 0
            hp = 5 + left_over_hp
            getLadder = False

        # flood level
        if actions_left <= 0:
            actions_left = 20
            flood_elevation += 1

        if hp <= 0:
            pygame.mixer.stop()
            ingame = False

        # creating a list of coordinates for walls, ladder, ground, flood----------------------------#
        obstacle_ladder_list = create_level(x_change, y_change, coord_layout_list, flood_elevation)

        obstacles = obstacle_ladder_list[0]
        ground = obstacle_ladder_list[1]
        flood = obstacle_ladder_list[2]
        ladder = obstacle_ladder_list[3]
        # -------------------------------------------------------------------------------------------#

        # creating the rects for walls, ladder, ground, flood-----------------#
        obstacle_rect_list = []

        for coord in obstacles:
            obstacle = pygame.Rect(coord[0], coord[1], UNIT, UNIT)
            pygame.draw.rect(WIN, (0, 0, 0), obstacle, int(UNIT / 24))
            obstacle_rect_list.append(obstacle)

        ground_rect_list = []

        for coord in ground:
            ground = pygame.Rect(coord[0], coord[1], UNIT, UNIT)
            ground_rect_list.append(ground)

        flood_rect_list = []

        for coord in flood:
            flood = pygame.Rect(coord[0], coord[1], UNIT, UNIT)
            flood_rect_list.append(flood)

        ladder_rect_list = []

        for coord in ladder:
            ladder_rect = pygame.Rect(coord[0], coord[1], UNIT, UNIT)
            ladder_rect_list.append(ladder_rect)
        # ---------------------------------------------------------------------#

        # collision detection of the character with walls, ladder, ground, flood-------------------------------------#
        if mc_rect_right.collidelist(ground_rect_list) != -1 or mc_rect_right.collidelist(
                ladder_rect_list) != -1 or mc_rect_right.collidelist(flood_rect_list) != -1:
            canMoveRight = True
        else:
            canMoveRight = False

        if mc_rect_left.collidelist(ground_rect_list) != -1 or mc_rect_left.collidelist(
                ladder_rect_list) != -1 or mc_rect_left.collidelist(flood_rect_list) != -1:
            canMoveLeft = True
        else:
            canMoveLeft = False

        if mc_rect_up.collidelist(ground_rect_list) != -1 or mc_rect_up.collidelist(
                ladder_rect_list) != -1 or mc_rect_up.collidelist(flood_rect_list) != -1:
            canMoveUp = True
        else:
            canMoveUp = False

        if mc_rect_down.collidelist(ground_rect_list) != -1 or mc_rect_down.collidelist(
                ladder_rect_list) != -1 or mc_rect_down.collidelist(flood_rect_list) != -1:
            canMoveDown = True
        else:
            canMoveDown = False
        # -----------------------------------------------------------------------------------------------------------#

        # detecting if stepping on ladder---------------------------#
        if mc_rect_center.collidelist(ladder_rect_list) != -1:
            getLadder = True
            left_over_hp = hp
            ladder_sfx.set_volume(1)
            ladder_sfx.play()
        # ----------------------------------------------------------#

        clock.tick(60)  # 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                run = False

            # movement down----------------------------------------#
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                if mc_rect_down.collidelist(flood_rect_list) != -1:
                    hp -= 1
                    y_change -= UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    water_step()

                elif canMoveDown:
                    y_change -= UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    tile_step()

            # movement left_---------------------------------------#
            elif keys[pygame.K_LEFT]:
                if mc_rect_left.collidelist(flood_rect_list) != -1:
                    hp -= 1
                    x_change += UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    water_step()

                elif canMoveLeft:
                    x_change += UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    tile_step()

            # movement up------------------------------------------#
            elif keys[pygame.K_UP]:
                if mc_rect_up.collidelist(flood_rect_list) != -1:
                    hp -= 1
                    y_change += UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    water_step()

                elif canMoveUp:
                    y_change += UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    tile_step()

            # movement right---------------------------------------#
            elif keys[pygame.K_RIGHT]:
                if mc_rect_right.collidelist(flood_rect_list) != -1:
                    hp -= 1
                    x_change -= UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    water_step()

                elif canMoveRight:
                    x_change -= UNIT * 1
                    actions_left -= 1
                    total_actions += 1
                    tile_step()

        draw_gui()
        pygame.display.update()

    # -----------------------------------------------------------------------#
    death_screen = True
    while death_screen:

        WIN.blit(death_img, (0, 0))
        death_level = ingame_font.render("Level: " + str(num_rooms), 1, (255, 255, 255))
        WIN.blit(death_level, (int(UNIT * 3 / 4 - UNIT / 20), int(UNIT * 0.9)))

        death_screen_title = death_screen_font.render("YOU DIED", 1, (255, 255, 255))
        WIN.blit(death_screen_title, (int(5.15 * UNIT), int(4.1 * UNIT)))

        death_screen_next = ingame_font.render("Press Enter to Continue", 1, (255, 255, 255))
        WIN.blit(death_screen_next, (int(6.15 * UNIT), 8 * UNIT))
        WIN.blit(end_credit, (UNIT * 0.5, WIN.get_height() * 0.9))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            death_screen = False
