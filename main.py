from game import Game
from Player import Player
from Shared import *
from drawings import draw_cards, convert_images
from menu import BasicMenu
import pygame

pygame.init()

player1 = Player(1, 'Player1')
player2 = Player(2, 'P2')
player3 = Player(3, 'P3')
player4 = Player(4, 'P4')

menu = BasicMenu(500, 500, 100, 30, ['1', '2', '3 option'],
                 colors['neon green'],
                 colors['midnight green'],
                 colors['midnight green'],
                 colors['neon green'],
                 colors['rosewood'],
                 colors['flame']
                 )

card_menu = BasicMenu(465, 400, 150, 40, ['Guard', 'Priest', 'Baron', 'Handmaid', 'Prince', 'King', 'Countess', 'Princess'],
                      colors['flame'],
                      colors['rosewood'],
                      colors['rosewood'],
                      colors['flame'],
                      colors['midnight green'],
                      colors['neon green']
                      )

game = Game([player1, player2, player3, player4])
game.restart()
game.begin_turn()
convert_images(game.display)

print(game.deck)
print(len(game.deck))
print((5/6) * display_width - card_width)

running = True
while running:
    data_past = game.get_data()
    data_next = dict()
    chosen_card = -1
    command = ''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.restart()
                game.begin_turn()

            if event.key == pygame.K_ESCAPE: running = False

        elif event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()

            card_menu.aimed_option = -1
            poss = card_menu.get_option_poss()
            for i in range(len(poss)):
                if poss[i][0] <= x <= poss[i][2] and poss[i][1] <= y <= poss[i][3]:
                    card_menu.set_aimed_option(i)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            poss = card_menu.get_option_poss()
            for i in range(len(poss)):
                if poss[i][0] <= x <= poss[i][2] and poss[i][1] <= y <= poss[i][3]:
                    card_menu.set_aimed_option(i, True)

        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()

            if data_past['needed info'] is None:
                poss = [get_card_draw_position(amount_of_cards=2)]
                command = 'casted card'
                print('choosing card')

            else:
                if data_past['needed info'] > 0 and data_past['target'] is None:
                    poss = [get_card_draw_position(places[i + 1]) for i in range(3)]
                    command = 'target'
                    print('choosing player')

                elif data_past['needed info'] > 1 and data_past['guess']is None:
                    command = 'guess'
                    print('ESTE NENI')

            for i in range(len(poss)):
                for j in range(len(poss[i])):
                    if poss[i][j][0] < x < poss[i][j][0] + card_width and poss[i][j][1] < y < poss[i][j][1] + card_height:
                        if data_past['needed info'] is None: chosen_card = j
                        else: chosen_card = i
                        data_next[command] = chosen_card
                        game.update(data_next)
                        print(chosen_card)
                        break

            poss = card_menu.get_option_poss()
            for i in range(len(poss)):
                if poss[i][0] <= x <= poss[i][2] and poss[i][1] <= y <= poss[i][3]:
                    card_menu.set_aimed_option(i, False)

    game.display.fill(0)
    game.draw_board()
    draw_text('Debug BITCH', colors['flame'], [800, 900], 50, game.display, fonts['blessed'])
    #card_menu.draw(game.display)
    pygame.display.update()

quit()
