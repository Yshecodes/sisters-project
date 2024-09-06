from random import choice

playerP = 0
machineP = 0

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

while True:
    print("-"*60)
    PlayerChose = player_choice()
    print("Esta jogando voce, Sophia e Laura, cada uma escolheu de 0 a 3...")
    Adivin = adivinha()
    machineSophia = sophia_choice()
    machineLaura = laura_choice()
    
    print("-"*60)
    if PlayerChose + machineSophia + machineLaura == Adivin:
        print(f"You win! Sophia chose {machineSophia} and Laura \
chose {machineLaura}")
        playerP += 1
        if playerChoice:
            playerChoice.pop()
        if (len(playerChoice) - 1) == 0:
            print("CONGRATULATIONS! You won!")
    else:
        print(f"You lose! Sophia chose: {machineSophia} and Laura \
chose: {machineLaura}")
        machineP += 1
        if sophiaChoice:
            sophiaChoice.pop()
        if lauraChoice:
            lauraChoice.pop()
        if (len(sophiaChoice) - 1) == 0:
            print("GAME OVER! The machine won!")
            break
        
    
    print("-"*60)
    print(f"Player Score {playerP}")
    print(f"Machine Score {machineP}")
    print("-"*60)

    chosetoplay = input("Voce quer continuar jogando?")
    if chosetoplay in ("Sim", "sim", "s", "S"):
        pass
    elif chosetoplay in ("Nao" "nao", "n", "N"):
        break
    else:
        break