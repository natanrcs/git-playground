DATABASE = []

def atualizar():
    antigo = input("Produto que deseja mudar: ")
    novo = input("Nome produto: ")
    if antigo in DATABASE:
        indice = DATABASE.index(antigo)
        DATABASE[indice] = novo
        print("Atualizado com sucesso!")
    else:
        print("Produto nao encontrado!")

def cadastrar():
    produto = input("Cadastre: ")
    DATABASE.append(produto)
    print("Cadastro com sucesso!")

def listar():
    for i in DATABASE:
        print(f"Todos produtos cadastrados: {i}")

def deletar():
    delete = input("Escolha um produto: ")
    if delete in DATABASE:
        DATABASE.remove(delete)
        print("Deletado com sucesso")
    else:
        print("Produto nao encontrado!")
        
while True:
    print("""
1 - Cadastrar
2 - Deletar
3 - Listar
4 - Atualizar
5 - Sair
""")
    try:
        option = int(input("Escolha um metodo: "))
    except ValueError:
        print("Apenas numeros!")
    if option ==1:
        cadastrar()
    elif option ==2:
        deletar()
    elif option ==3:
        listar()
    elif option ==4:
        atualizar()
    elif option ==5:
        print("Saindo")
        break
    else:
        print("Tente novamente!")