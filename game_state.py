from random import choice

class GameState:
    def __init__(self):
        self.players = {
            "player1": {
                "name": None,
                "hand": [0, 1, 2, 3],
                "throw": None,
                "guess": None,
                "score": 0
            },
            "player2": {
                "name": "Sophia",
                "hand": [0, 1, 2, 3],
                "throw": None,
                "guess": None,
                "score": 0
            },
            "player3": {
                "name": "Laura",
                "hand": [0, 1, 2, 3],
                "throw": None,
                "guess": None,
                "score": 0
            }
        }
    
    def set_player_name(self, player, name):
        if player in self.players:
            self.players[player]['name'] = name

    def get_player_name(self, player):
        return self.players[player]['name'] if player in self.players else None

    def set_player_throw(self, player, throw):
        if player in self.players:
            self.players[player]['throw'] = throw

    def gen_starting_player(self):
        self.player_keys = list(self.players.keys())
        self.current_player = choice(self.player_keys)
        self.current_index = self.player_keys.index(self.current_player)

    def rotate_turns(self, player_keys, current_index):
        return (current_index + 1) % len(player_keys)
    
    def set_machine_throw(self, key, value):
        if key in self.players:
            self.players[key]['throw'] = value

    def get_machine_throw(self, key):
        return choice(self.players[key].get('hand'))



    def get_player2_guess(self, player2_throw, existing_guesses):
        while True:
            guess = choice(self.players['player1']['hand']) + choice(self.players['player3']['hand']) + player2_throw
            if guess not in existing_guesses:
                return guess

    def get_player3_guess(self, player3_throw, existing_guesses):
        while True:
            guess = choice(self.players['player1']['hand']) + choice(self.players['player2']['hand']) + player3_throw
            if guess not in existing_guesses:
                return guess

    existing_guesses = []
    def calculate_existing_guesses(self, players):
        return [players[key]['guess'] for key in players if players[key]['guess'] is not None]

    def calculate_total_of_sticks(self, players):
        total_sticks = 0
        for player in players.values():
            if player['throw'] is not None:
                try:
                    total_sticks += int(player['throw'])
                except ValueError:
                    print(f"Invalid throw value for player {player['name']}. Skipping.")
            else:
                print(f"Throw value is None for player {player['name']}. Skipping.")
        return total_sticks

    def reset_players_attributes(self):
        for player in self.players.values():
            player['hand'] = [0, 1, 2, 3]
            player['score'] = 0

    def check_winner(self, total_sticks, players, player_keys, current_index):
        while True:
            game_over = False
            winner = None
            
            for player_key in players:
                player = players[player_key]
                if total_sticks == player['guess']:
                    player['score'] += 1
                    if player['hand']:
                        player['hand'].pop()
                    if len(player['hand']) == 0:
                        game_over = True
                        winner = player_key
                        break
            
            if game_over:
                return winner
            
            # Rotate turns
            current_index = self.rotate_turns(player_keys, current_index)
            
            # Initialize guesses for the next round
            for player in players.values():
                player['guess'] = None