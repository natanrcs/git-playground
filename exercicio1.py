def imparoupar(numero):
    if numero % 2 == 0:
        print(f"{numero} é Par")
    else:
        print(f"{numero} é Impar")
    return numero

while True:
    opcao=int(input("Escolha 1 a 3: "))
    if opcao == 1:
        msg="123456"
        print(msg)
    elif opcao == 2:
        try:
            novoNumero=int(input("Digite um numero: "))
            imparoupar(novoNumero)
        except ValueError:
            print("Somente números")
    elif opcao == 3:
        print("12345678")
    else:
        print("Saindo ...")
        break