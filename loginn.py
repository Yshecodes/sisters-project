while True:
    login = input("Type username:")
    passw = input("Type your password:")
    confirm = input("Confirme your password:")
    if passw in confirm:
        print("Subscription conclude")
        print("-------------------")
        break
    else:
        print("Error in password confirmation")


user = login
password = passw


def logar_in(user, password):
    log1 = input("Login:")
    pass1 = input("Password:")
    if user == log1 and password == pass1:
        print("Welcome to your Account")
        print("--------( ^ _ ^ )-----------")
    else:
        print("Access denied")
        print("*********( -_- )*********")


print("Subscribe")
logar_in(user, password)
