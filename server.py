from game import Game

class GameServer:

    def __init__(self):
        self.games = dict()
        self.game_number = 0

    def handle(self, data):
        if data['command'] == 'new game':
            self.games[self.game_number] = Game(data['players'])
            self.game_number += 1
            return self.game_number - 1

        if data['command'] == 'get info':




