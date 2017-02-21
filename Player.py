class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.kills = list()
        self.alive = True
        self.game_index = -1
        self.hand = list()
        self.discard = list()
        self.can_be_targetted = True
        self.not_seen_cards = list()
        self.known_players_hands = dict()

    def __int__(self):
        return int(self.id)

    def add_game_index(self, index):
        self.game_index = index

    def get_index(self):
        return self.game_index

    def get_hand(self):
        return self.hand

    def get_discard(self):
        return self.discard

    def get_targetability(self):
        return self.can_be_targetted

    def does_know(self, player_number):
        if player_number in self.known_players_hands.keys() and self.known_players_hands[player_number] is not None: return True
        return False

    def receive_card(self, card):
        self.hand.append(card)

    def lose_card(self, card_index=0, disc=True):
        if disc: self.discard.append(self.hand[card_index])
        return self.hand.pop(card_index)

    def is_alive(self):
        return self.alive

    def die(self):
        self.alive = False
        for i in range(len(self.hand)):
            self.discard.append(self.hand.pop(-1))

    def kill(self, player_id):
        self.kills.append(player_id)

    def see_hand(self, player_id, cards):
        self.known_players_hands[player_id] = cards

    def empty_hand(self):
        self.hand = []

    def change_targetability(self, new):
        self.can_be_targetted = new

    def reset(self):
        self.kills = list()
        self.alive = True
        self.hand = list()
        self.discard = list()
        self.can_be_targetted = True
        self.not_seen_cards = list()
        self.known_players_hands = dict()
