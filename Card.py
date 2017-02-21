class Card:
    def __init__(self, name, value, img_path, info, amount_in_deck):
        self.name = name
        self.value = value
        self.required = info
        self.img_path = img_path
        self.amount_in_deck = amount_in_deck

    def __int__(self):
        return self.value

    def __str__(self):
        return self.name

    def get_info(self):
        return [self.value, self.name, self.required]

    def get_amount(self):
        return self.amount_in_deck

    def effect(self, players, data):
        pass


class Guard(Card):
    def effect(self, players, data):
        if int(players[data['target']].get_hand()[0]) == data['guess']:
            players[data['caster']].kill(int(players[data['target']]))
            players[data['target']].die()
guardCard = Guard("Guard", 1, r"/pics/1.jpg", 2, 5)


class Priest(Card):
    def effect(self, players, data):
        players[data['caster']].see_hand(int(players[data['target']]), players[data['target']].get_hand())
priestCard = Priest("Priest", 2, "/pics/2.jpg", 1, 2)


class Baron(Card):
    def effect(self, players, data):
        print(players[data['caster']].get_hand())
        card_value_1 = int(players[data['caster']].get_hand()[0][0])
        card_value_2 = int(players[data['target']].get_hand()[0][0])

        if card_value_1 == card_value_2:
            players[data['caster']].see_hand(players[data['target']], players[data['target']].get_hand())
            players[data['target']].see_hand(players[data['caster']], players[data['caster']].get_hand())

        elif card_value_1 > card_value_2: 
            players[data['caster']].kill(players[data['target']])
            players[data['target']].die()

        else:
            players[data['target']].kill(players[data['caster']])
            players[data['caster']].die()
baronCard = Baron("Baron", 3, "/pics/3.jpg", 1, 2)


class Handmaid(Card):
    def effect(self, players, data):
        players[data['caster']].change_targetability(False)
handmaidCard = Handmaid("Handmaid", 4, "/pics/4.jpg", 0, 2)


class Prince(Card):
    def effect(self, players, data):
        card_value = int(players[data['target']].lose_card())

        if card_value == 8:
            players[data['caster']].kill(players[data['target']])
            players[data['target']].die()
princeCard = Prince("Prince", 5, "/pics/5.jpg", 1, 2)


class King(Card):
    def effect(self, players, data):
        card1 = players[data['caster']].lose_card(disc=False)
        card2 = players[data['target']].lose_card(disc=False)
        players[data['caster']].receive_card(card2)
        players[data['target']].receive_card(card1)
kingCard = King("King", 6, "/pics/6.jpg", 1, 1)


class Countess(Card):
    pass
countessCard = Countess("Countess", 7, "/pics/7.jpg", 0, 1)


class Princess(Card):
    def effect(self, players, data):
        players[data['caster']].die()
princessCard = Princess("Princess", 8, "/pics/8.jpg", 0, 1)

all_cards = [guardCard, priestCard, baronCard, handmaidCard, princeCard, kingCard, countessCard, princessCard]
