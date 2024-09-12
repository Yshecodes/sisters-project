from random import choice
from time import sleep   # タイムモジュールからsleep()関数をインポートしました。

players = {
"player1": {
    "name": None,
    "hand": [0, 1, 2, 3],
    "guess": None,
    "score" : 0
},
"player2": {
    "name": "Sophia",
    "hand": [0, 1, 2, 3],
    "guess": None,
    "score" : 0
},
"player3": {
    "name": "Laura",
    "hand": [0, 1, 2, 3],
    "guess": None,
    "score" : 0
}
}

player_names = list(players.keys())
current_player = choice(player_names)
current_index = player_names.index(current_player) % len(player_names)

def rotate_turns(player_names, current_index):
    current_index = (current_index + 1) % len(player_names)
    return current_index

def get_player_throw(players, key):
    while True:
        value = int(input(f"Voce tem {len(players[key]['hand']) - 1} palitos. \
Quantos palitos estarao na sua mao? "))
        limit_number = 0
        if value in players[key]['hand']:
            return value
        elif (value) < (limit_number):
            print("Please enter a valid number from 0 to 3")
        else:
            print("Please enter a valid number")


def get_player2_throw(players, key):
    return choice(players[key]['hand'])


def get_player3_throw(players, key):
    return choice(players[key]['hand'])


def get_player_guess():
    guess = int(input("Adivinhe quantos palitos tem ao todo: "))
    return guess 


def get_player2_guess(player2_throw, existing_guesses):
    while True:
        guess = choice(players['player1']['hand']) + choice(players['player3']['hand']) + player2_throw
        if guess not in existing_guesses:
            return guess


def get_player3_guess(player3_throw, existing_guesses):
    while True:
        guess = choice(players['player1']['hand']) + choice(players['player2']['hand']) + player3_throw
        if guess not in existing_guesses:
            return guess
        
def reset_players_attributes(players, current_player):
    for player_key in players:
        players[player_key]['hand'] = [0, 1, 2, 3]
        players[player_key]['score'] = 0
        players[player_key]['guess'] = None
        current_player = choice(player_names)
        


def game_start(players, key, player_names, current_player, current_index, rotate_turns ):
    print("-" * 60)
    sleep(2) 
    players['player1']['name'] = input("Hi! What's your name? ")
    print(f"Welcome {players[key]['name']}! Let's play!")
    print(f"{players[current_player]['name']} starts this time!")
    print("Players choose your throw!")
    
    while True:
        player1_throw = get_player_throw(players, "player1")
        player2_throw = get_player2_throw(players, "player2")
        player3_throw = get_player3_throw(players, "player3")
    
        total_of_sticks = player1_throw + player2_throw + player3_throw
    
        for _ in range(len(players)):
            current_player_key = player_names[current_index]
            existing_guesses = [players[p]['guess'] for p in player_names
                            if players[p]['guess'] is not None]
        
            if current_player_key == "player1":
                print(f"Your turn {players['player1']['name']}, what's  your guess?")
                guess = get_player_guess()
                players['player1']['guess'] = guess
                existing_guesses.append(guess)
                print(f"players{players['player1']['name']} guessed {guess}.")
                
            elif current_player_key == "player2":
                print(f"Your turn {players['player2']['name']}, what's your guess?")
                guess = get_player2_guess(player2_throw, existing_guesses)
                players['player2']['guess'] = guess
                existing_guesses.append(guess)
                print(f"players{players['player2']['name']} guessed {guess}.")
                
            elif current_player_key == "player3":
                print(f"Your turn {players['player3']['name']}, what's your guess?")
                guess = get_player3_guess(player3_throw, existing_guesses)
                players['player3']['guess'] = guess
                existing_guesses.append(guess)
                print(f"players{players['player3']['name']} guessed {guess}.")
        
            current_index = rotate_turns(player_names, current_index)
        
        game_over = False
        
        if total_of_sticks == players['player1']['guess']:
            print(f"You win! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}! Great guess!")
            players['player1']['score'] += 1
            if players['player1']['hand']:
                players['player1']['hand'].pop()
            if (len(players['player1']['hand']) - 1) == 0:
                print(f"CONGRATULATIONS {players['player1']['name']}! You won!")
                game_over = True
            
        elif total_of_sticks == players['player2']['guess']:
            print(f"You lose! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}! {players['player2']['name']} got this one!")
            players['player2']['score'] += 1
            if players['player2']['hand']:
                players['player2']['hand'].pop()
            if (len(players['player2']['hand']) - 1) == 0:
                print(f"{players['player2']['name']} won! Better luck next time!")
                game_over = True
            
        elif total_of_sticks == players['player3']['guess']:
            print(f"You lose! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}! {players['player3']['name']} got this one!")
            players['player3']['score'] += 1
            if players['player3']['hand']:
                players['player3']['hand'].pop()
            if (len(players['player3']['hand']) - 1) == 0:
                print(f"{players['player3']['name']} won! Better luck next time!")
                game_over = True
            
        else: 
            # Done
            print(f"No one guessed it right! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}")
            
        print("-"*60)
        print(f"{players['player1']['name']}'s Score {players['player1']['score']}")
        print(f"{players['player2']['name']}'s Score {players['player2']['score']}")
        print(f"{players['player3']['name']}'s Score {players['player3']['score']}")
        print("-"*60)
        
        current_index = rotate_turns(player_names, current_index)
    
        if game_over: 
            play_again = input("Play again?").lower()  
            if play_again not in ("yes", "y"):
                print("See you next time!") 
                break
            else:
                # Todo reset to a new game order
                reset_players_attributes(players, current_player) 
                

game_start(players, 'player1', player_names, current_player, current_index, rotate_turns)
