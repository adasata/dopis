import pygame
import os
from Card import all_cards
from Shared import *

images = dict()

for card in all_cards:
    image = pygame.image.load(os.environ['PYTHONPATH'] + card.img_path)
    images[str(card)] = image

images['back'] = pygame.image.load(os.environ['PYTHONPATH'] + '/pics/back.jpg')


def convert_images(surf):
    for key in images.keys():
        images[key] = images[key].convert(surf)


def draw_cards(players, player_on_turn, surface):
    for i in range(len(players)):
        hand = players[(player_on_turn + i) % len(players)].get_hand()
        discard = players[(player_on_turn + i) % len(players)].get_discard()
        poss_h = get_card_draw_position(places[i], len(hand))
        poss_d = get_played_card_position(places[i], len(discard))

        for j in range(len(hand)):
            if i == player_on_turn or players[player_on_turn].does_know(int(players[(player_on_turn + i) % len(players)])):
                surface.blit(images[hand[j][1]], poss_h[j])# + [poss[j][0] + card_width, poss[j][1] - card_height])

            else: surface.blit(images['back'], poss_h[j])

        for j in range(len(discard)):
            surface.blit(images[discard[j][1]], poss_d[j])
