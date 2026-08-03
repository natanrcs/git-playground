user_admin = {
    "name": "natan","password":"3591"
}
def login():
    user = input("digite seu nome: ")
    password = input("digite sua senha: ")
    if user == user_admin.get("name") and password == user_admin.get("password"):
        print("acesso liberado!")
    else:
        print("acesso negado!")
login()