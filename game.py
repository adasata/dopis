import pygame
import random
from Shared import *
from Card import all_cards
from Player import Player
from drawings import draw_cards


class Game:
    def __init__(self, players=list()):
        self.players = list()

        self.data = dict()
        self.keys = ['caster', 'target', 'guess', 'casted card', 'needed info']
        for key in self.keys: self.data[key] = None

        for i, nick in enumerate(players):
            self.players.append(Player(i, nick))

        self.player_on_turn = -1

        self.deck = []
        for card in all_cards:
            for i in range(card.get_amount()):
                self.deck.append(card.get_info())

        self.display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Love Letter')

    def get_player_on_turn(self):
        return self.player_on_turn

    def get_participants(self):
        return self.players

    def get_data(self):
        return self.data

    def draw_board(self):
        draw_cards(self.players, self.player_on_turn, self.display)

    def draw_card(self, p_index):
        self.players[p_index].receive_card(self.deck[-1])
        self.deck.pop(-1)

    def cast(self):
        card = self.players[self.player_on_turn].lose_card(self.data['casted card'])[0]
        self.data['caster'] = self.player_on_turn
        all_cards[card - 1].effect(self.players, self.data)

    def restart(self):
        self.player_on_turn = 0

        for player in self.players:
            player.empty_hand()

        self.deck = []
        for card in all_cards:
            for i in range(card.get_amount()):
                self.deck.append(card.get_info())
        random.shuffle(self.deck)

        for player in self.players:
            self.draw_card(int(player))

    def begin_turn(self):
        self.player_on_turn = 0#(self.player_on_turn + 1) % len(self.players)
        self.data = dict()
        for key in self.keys: self.data[key] = None

        for player in self.players:
            if len(player.get_hand()) < 1 and player.is_alive(): self.draw_card(player)

        if not self.players[self.player_on_turn].get_targetability():
            self.players[self.player_on_turn].change_targetability(True)

        self.draw_card(self.player_on_turn)
        self.data = dict()
        for key in self.keys: self.data[key] = None

    def update(self, data):
        for key in data.keys():
            if self.data[key] is None:
                self.data[key] = data[key]
                print('updating', key)
                print(self.data)

        if self.data['casted card'] is not None and len(self.players[self.player_on_turn].get_hand()) == 2:
            self.data['needed info'] = self.players[self.player_on_turn].get_hand()[self.data['casted card']][2]
            print('menim', self.data)
            print(self.players[self.player_on_turn].get_hand()[self.data['casted card']][2])

        if (self.data['needed info'] is None) or (self.data['needed info'] > 0 and self.data['target'] is None) or (self.data['needed info'] > 1 and self.data['guess'] is None): return
        print('tu')
        self.cast()
        self.begin_turn()
