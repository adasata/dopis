import pygame
import os


class BreakException(Exception):
    print("Breaking Exception")

display_width = 1080
display_height = 1080

card_width = 118
card_height = 164
space_between_cards = 30
discard_x_shift = 50
discard_y_shift = 50
place_numbers_horizontal = {'left':1, 'down':3, 'up':3, 'right':5}
place_numbers_vertical = {'down':5, 'left':2, 'right':2, 'up':1}
places = ['down', 'right', 'up', 'left']

colors = dict()
colors['white'] = [255, 255, 255]
colors['black'] = [0, 0, 0]
colors['wisteria'] = [142, 68, 173]
colors['emerald'] = [46, 204, 113]
colors['neon green'] = [57, 255, 20]
colors['midnight green'] = [0, 73, 83]
colors['rosewood'] = [101, 0, 11]
colors['flame'] = [226, 88, 34]

fonts = dict()
fonts['blessed'] = './fonts/BLESD.ttf'


def get_card_draw_position(place='down', amount_of_cards=1):
    c_hor = place_numbers_horizontal[place] * display_width / 6
    c_vert = place_numbers_vertical[place] * display_height / 6

    if amount_of_cards == 1: return [[c_hor - card_width/2, c_vert - card_height/2]]

    else: return [[c_hor - (card_width + space_between_cards/2), c_vert - card_height/2],
                  [c_hor + space_between_cards/2, c_vert - card_height/2]]


def get_played_card_position(place='down', amount_of_cards=1):
    if place == 'down': ky = -1
    else: ky = 1

    if place == 'up': kx = -1
    else: kx = 1

    c_hor = place_numbers_horizontal[place] * display_width / 6
    c_vert = (place_numbers_vertical[place] * display_height / 6) + ky*(card_height + space_between_cards)

    poss = [[c_hor - card_width/2, c_vert - card_height/2]]
    for i in range(amount_of_cards - 1):
        poss.append([poss[-1][0] + kx*discard_x_shift, poss[-1][1] + ky*discard_y_shift])

    return poss


def draw_text(message, color, pos, size, surface, font):
    font = pygame.font.Font(font, size)
    surf = font.render(message, 0, color)
    surface.blit(surf, pos)
