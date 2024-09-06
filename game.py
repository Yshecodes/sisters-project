from random import choice

playerP = 0
machineP = 0


def playerchoice():
    playerC = int(input("Quantos palitos estara na sua mao de 0 a 3: "))
    return playerC


def adivinha():
    adivinhando = int(input("Adivinhe quantos palitos tem ao todo:"))
    return adivinhando


def Sophia():
    machinC = choice([0, 1, 2, 3])
    return machinC


def Laura():
    machinC = choice([0, 1, 2, 3])
    return machinC


while True:
    print("-"*60)
    PlayerChoose = playerchoice()
    print("Esta jogando voce, Sophia e Laura, cada uma escolheu de 0 a 3...")
    Adivin = adivinha()
    MachineChoice = Sophia()
    MachineChoose = Laura()
    
    print("-"*60)
    if PlayerChoose + MachineChoice + MachineChoose == Adivin:
        print(f"You win! Sophia choose {MachineChoice} and Laura \
choose{MachineChoose}")
        playerP += 1
    else:
        print(f"You lose! Sophia choose: {MachineChoice} and Laura \
choose: {MachineChoose}")
        machineP += 1
    
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