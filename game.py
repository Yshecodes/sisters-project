from random import choice

player_score = 0
sophia_score = 0
laura_score = 0
player_hand = [0, 1, 2, 3]
sophia_hand = [0, 1, 2, 3]
laura_hand = [0, 1, 2, 3]


def get_player_throw():
    while True:
        value = int(input(f"Voce tem {len(player_hand) - 1} palitos. \
Quantos palitos estarao na sua mao? "))
        limit_number = 0
        if value in player_hand:
            return value
            break
        elif (value) < (limit_number):
            print("Please enter a valid number from 0 to 3")
        else:
            print("Please enter a valid number")
        

def get_sophia_throw():
    return choice(sophia_hand)


def get_laura_throw():
    return choice(laura_hand)


def get_player_guess():
    return int(input("Adivinhe quantos palitos tem ao todo: "))


def get_sophia_guess():
    while True:
        guess = choice(player_hand) + choice(laura_hand) + sophia_throw
        if(guess != player_guess):
            return guess


def laura_turn_guess():
    while True:
        guess = choice(player_hand) + choice(sophia_hand) + laura_throw
        if guess != player_guess and guess != sophia_guess:
            return guess


while True:
    print("-" * 60)

    player_throw = get_player_throw()
    sophia_throw = get_sophia_throw()
    laura_throw = get_laura_throw()
    
    print("Vôce está jogando com Sophia e Laura, cada uma pode ter de 0 a 3 palitos.")
    
    player_guess = get_player_guess()
    sophia_guess = get_sophia_guess()
    laura_guess = laura_turn_guess()
    
    print("-"*60)
    
    total_of_sticks = player_throw + sophia_throw + laura_throw
    
    print(f"Your guess: {player_guess}. Sophia's guess: {sophia_guess}. Laura's guess: {laura_guess}.")
    
    game_over = False
    
    if total_of_sticks == player_guess:
        print(f"You win! Sophia threw {sophia_throw}. Laura threw {laura_throw}. You threw {player_throw}. Total is {total_of_sticks}! Great guess!")
        player_score += 1
        if player_hand:
            player_hand.pop()
        if (len(player_hand) - 1) == 0:
            print("CONGRATULATIONS! You won!")
            game_over = True

    elif total_of_sticks == sophia_guess:
        print(f"You lose! Sophia threw: {sophia_throw}. Laura threw: {laura_throw}. You threw {player_throw}. Total is {total_of_sticks}! Sophia got this one!")
        sophia_score += 1
        if sophia_hand:
            sophia_hand.pop()
        if (len(sophia_hand) - 1) == 0:
            print("GAME OVER! Sophia won!")
            game_over = True

    elif total_of_sticks == laura_guess:
        print(f"You lose! Sophia threw: {sophia_throw}. Laura threw: {laura_throw}. You threw {player_throw}. Total is {total_of_sticks}! Laura won this one!")
        laura_score += 1
        if laura_hand:
            laura_hand.pop()
        if (len(laura_hand) - 1) == 0:
            print("GAME OVER! Laura won!") 
            game_over = True

    else: 
        print("No one guessed it right!")
        
    print("-"*60)
    print(f"Your Score {player_score}")
    print(f"Sophia's Score {sophia_score}")
    print(f"Laura's Score {laura_score}")
    print("-"*60)
    
    if game_over: 
        play_again = input("Do you want to play again?").lower()  
        if play_again not in ("yes"):  # mudei pra Yes
            print("See you next time!")  # Esse aqui nao sei como ficaria mais legal See you next time?
            break
        else: 
            player_hand = [0, 1, 2, 3]
            sophia_hand = [0, 1, 2, 3]
            laura_hand = [0, 1, 2, 3]
            player_score = 0
            sophia_score = 0
            laura_score = 0