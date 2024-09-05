menbroNum = 1122  # Esse numero eh do cartao que o cliente tem em maos

while True:
    nome = input("Seu nome: ")
    cardnum = int(input("Numero do seu cartao membro: "))
    if cardnum == menbroNum:
        print("Seja bem vindo novamente")
        break
    else:
        print("Nao a registros. Faca sua reserva pelo numero 053-553-777")
        

user = nome
nRegistro = cardnum

listadias = ["Segunda", "Terca", "Quinta", "Sexta"]
listaN = ["Quarta", "Sabado", "Domingo"]


def reservando(listadias, listaN, user):
    pedido = input("Qual dia voce quer reservar?:")
    if pedido in listadias:
        print(f"{user}Sua Reserva esta confirmada para {pedido}")
    elif pedido in listaN:
        print("Neste dia a clinica esta fechada")
    else:
        print("Dia nao identificado")


reservando(listadias, listaN, user)
