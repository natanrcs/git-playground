DATABASE = []
user_admin =[
    {"name":"natan","password": "3591"},
    {"name":"gabi","password":"2501"},
    {"name":"melinda","password":"2505"},
    {"name":"will","password":"8890"},
    {"name":"dogao","password":"2567"}
]

def acess_login():
    user_name = input("digite seu nome: ")
    user_password = input("digite sua senha: ")
    for i in user_admin:
        if user_name == i.get("name") and user_password == i.get("password"):
            DATABASE.append(user_name)
            print("acesso liberado!")
            return
    print("acesso negado!")
acess_login()