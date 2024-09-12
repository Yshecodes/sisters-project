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

#関数に変えました。
def gen_starting_player(players):
    player_names = list(players.keys())
    current_player = choice(player_names)
    current_index = player_names.index(current_player)
    return player_names, current_player, current_index

def rotate_turns(player_names, current_index):
    current_index = (current_index + 1) % len(player_names)
    return current_index

def get_player_throw(players, key):
    while True:
        value = int(input(f"Voce tem {len(players[key]['hand']) - 1} palitos. \
Quantos palitos estarao na sua mao? "))
        print("-" * 60)
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
        
def reset_players_attributes(players):
    for player_key in players:
        players[player_key]['hand'] = [0, 1, 2, 3]
        players[player_key]['score'] = 0


def game_start(players, key, gen_starting_player ,rotate_turns ):
    print("-" * 60)
    sleep(1) 
    players['player1']['name'] = input("Hi! What's your name? ")
    print(f"Welcome {players[key]['name']}! Let's play!")
    print("-" * 60)
    player_names, current_player, current_index = gen_starting_player(players)
    print(f"{players[current_player]['name']} starts this time!")
    print("Players choose your throw!")
    print("-" * 60)
    
    while True:
        print(f"Jogador que comeca: {players[current_player]['name']}")
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
                print("-" * 60)
                
            elif current_player_key == "player2":
                print(f"Your turn {players['player2']['name']}, what's your guess?")
                guess = get_player2_guess(player2_throw, existing_guesses)
                players['player2']['guess'] = guess
                existing_guesses.append(guess)
                print(f"players{players['player2']['name']} guessed {guess}.")
                print("-" * 60)
                
            elif current_player_key == "player3":
                print(f"Your turn {players['player3']['name']}, what's your guess?")
                guess = get_player3_guess(player3_throw, existing_guesses)
                players['player3']['guess'] = guess
                existing_guesses.append(guess)
                print(f"players{players['player3']['name']} guessed {guess}.")
                print("-" * 60)
        
            current_index = rotate_turns(player_names, current_index)
        
        game_over = False
        
        if total_of_sticks == players['player1']['guess']:
            print(f"You win! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}! Great guess!")
            players['player1']['score'] += 1
            if players['player1']['hand']:
                players['player1']['hand'].pop()
            if (len(players['player1']['hand']) - 1) == 0:
                print("-" * 60)
                print(f"CONGRATULATIONS {players['player1']['name']}! You won!")
                print("-" * 60)
                game_over = True
            
        elif total_of_sticks == players['player2']['guess']:
            print(f"You lose! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}! {players['player2']['name']} got this one!")
            players['player2']['score'] += 1
            if players['player2']['hand']:
                players['player2']['hand'].pop()
            if (len(players['player2']['hand']) - 1) == 0:
                print("-" * 60)
                print(f"{players['player2']['name']} won! Better luck next time!")
                print("-" * 60)
                game_over = True
            
        elif total_of_sticks == players['player3']['guess']:
            print(f"You lose! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}! {players['player3']['name']} got this one!")
            players['player3']['score'] += 1
            if players['player3']['hand']:
                players['player3']['hand'].pop()
            if (len(players['player3']['hand']) - 1) == 0:
                print("-" * 60)
                print(f"{players['player3']['name']} won! Better luck next time!")
                print("-" * 60)
                game_over = True
            
        else:
            print(f"No one guessed it right! {players['player2']['name']} threw {player2_throw}. {players['player3']['name']} threw {player3_throw}. You threw {player1_throw}. Total is {total_of_sticks}")
            
        print("-"*60)
        print(f"{players['player1']['name']}'s Score {players['player1']['score']}")
        print(f"{players['player2']['name']}'s Score {players['player2']['score']}")
        print(f"{players['player3']['name']}'s Score {players['player3']['score']}")
        print("-"*60)
        
        print(f"Round final: {existing_guesses}")
        
        current_index = rotate_turns(player_names, current_index)
        
        #ラウンドごとに各プレイヤーの推量を初期化している。
        for player in players:
            players[player]['guess'] = None
    
        if game_over: 
            play_again = input("Play again?").lower()  
            if play_again not in ("yes", "y"):
                print("See you next time!") 
                break
            else:
                #プレイヤースコアとハンドを初期化します。
                reset_players_attributes(players)
                #初プレイヤーの順番を再度決める。
                player_names, current_player, current_index = gen_starting_player(players)

game_start(players, 'player1', gen_starting_player, rotate_turns)