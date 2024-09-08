from random import choice

playerP = 0
sophiaP = 0
lauraP = 0

playerChoice = [0, 1, 2, 3]
def player_choice():
    playerC = int(input(f"Voce tem {len(playerChoice) - 1} palitos. Quantos palitos estarao na sua mao? > "))
    return playerC

def adivinha():
    adivinhando = int(input("Adivinhe quantos palitos tem ao todo:"))
    return adivinhando


sophiaChoice = [0, 1, 2, 3]
def sophia_choice():
    sophia = choice(sophiaChoice)
    return sophia

lauraChoice = [0, 1, 2, 3]
def laura_choice():
    laura = choice(lauraChoice)
    return laura

def sophia_guess():
    sophiaGuess = choice(playerChoice) + machineSophia
    return sophiaGuess

def laura_guess():
    lauraGuess = choice(playerChoice) + machineLaura
    return lauraGuess


while True:
    print("-"*60)
    PlayerChose = player_choice()
    print("Esta jogando voce, Sophia e Laura, cada uma escolheu de 0 a 3...")
    userGuess = adivinha()
    machineSophia = sophia_choice()
    machineLaura = laura_choice()
    sophiaGuessed = sophia_guess()
    lauraGuessed = laura_guess()
    
    print("-"*60)
    total = PlayerChose + machineSophia + machineLaura

    print(f"Your guessed: {userGuess}. Sophia's guessed: {sophiaGuessed}. Laura's guess: {lauraGuessed} ")

    if total == userGuess:
        print(f"You win! Sophia has {machineSophia} and Laura \
has {machineLaura}, you have {PlayerChose}. Total is {total}! Great guess!")
        playerP += 1
        if playerChoice:
            playerChoice.pop()
        if (len(playerChoice) - 1) == 0:
            print("CONGRATULATIONS! You won!")
            break

    elif total == sophiaGuessed:
        print(f"You lose! Sophia chose: {machineSophia} and Laura \
chose: {machineLaura}, you have {PlayerChose}. Total is {total}! Sophia got this one!")
        sophiaP += 1
        if sophiaChoice:
            sophiaChoice.pop()
        if (len(sophiaChoice) - 1) == 0:
            print("GAME OVER! Sophia won!")
            break

    elif total == lauraGuessed:
        print(f"You lose! Sophia chose: {machineSophia} and Laura \
chose: {machineLaura}, you have {PlayerChose}. Total is {total}! Laura won this one!")
        lauraP += 1
        if lauraChoice:
            lauraChoice.pop()
        if (len(sophiaChoice) - 1) == 0:
            print("GAME OVER! Laura won!")
            break
    else: print("No one guessed it right!")
    
    print("-"*60)
    print(f"Your Score {playerP}")
    print(f"Sophia's Score {sophiaP}")
    print(f"Laura's Score {lauraP}")

    print("-"*60)

# Todo implementar uma funcao pra chamar game start
chosetoplay = input("Quer começar uma nova partida?")
if chosetoplay in ("Sim", "sim", "s", "S"):
    pass
elif chosetoplay in ("Nao" "nao", "n", "N"):
    print("Até a próxima!")

