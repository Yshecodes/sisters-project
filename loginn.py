
#ユーザー名とパスワードの変数をwhile文の外へ移動した。
username = None
passw = None

while True:
    username = input("Type username:") #login変数名をusernameに変更した。
    passw = input("Type your password:")
    pwCheck = input("Confirm your password:") #confirm変数名をpwCheckに変更した。
    if passw == pwCheck:  #変更前の「if passw in confirm:」は特定の部分文字列が存在するかを調べる
        print("Subscription completed") #concludeをcompletedに変更した
        print("-------------------")
        break
    else:
        print("Error in password confirmation")


#userとpasswordの変数を削除した。


def logar_in(user, password):
    log1 = input("Enter your username:") #画面表示テキストを変えました
    pass1 = input("Enter your password:") #画面表示テキストを変えました
    if user == log1 and password == pass1:
        print("Welcome to your Account")
        print("--------( ^ _ ^ )-----------")
    else:
        print("Access denied")
        print("*********( -_- )*********")


print("Login") #SubscribeをLoginに変更した
logar_in(username,passw) #変更後の変数名に直した
