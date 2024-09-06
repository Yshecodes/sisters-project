
# ユーザー名とパスワードの変数をwhile文の外へ移動した。Colocou p fora do While essas variaveis
username = None
passw = None

while True:
    username = input("Type username:")  # login変数名をusernameに変更した。Ok
    passw = input("Type your password:")
    pwCheck = input("Confirm your password:")  # confirm変数名をpwCheckに変更した.
    if passw == pwCheck:  # Acho que daria no msm if in e ==.Nesse caso.
        # Agr nao sei se um pesa mais que outro.
        print("Subscription completed")  # concludeをcompletedに変更した Ficou melhor
        print("-"*25)  # alterei pra diminuir o codigo escrito
        break
    else:
        print("Error in password confirmation")


# userとpasswordの変数を削除した。Ok


def logar_in(user, password):
    log1 = input("Enter your username:")  # 画面表示テキストを変えました Ok
    pass1 = input("Enter your password:")  # 画面表示テキストを変えました Ok
    if user == log1 and password == pass1:
        print("Welcome to your Account")
        print("--------( ^ _ ^ )--------")
    else:
        print("Access denied")
        print("*********( -_- )*********")


print("Login")  # SubscribeをLoginに変更した Aqui era soh p testar o Gitpush
logar_in(username,passw)  # 変更後の変数名に直した  Aqui soh tinha faltado 
# um espaco depois do username, passw por isso estava vermelho