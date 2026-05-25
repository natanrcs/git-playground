def numeroMaior():
    numeros=[]
    for i in range(3):
        number=int(input("Digite um numero: "))
        numeros.append(number)
        maiorNumero=max(numeros)
        menorNumero=min(numeros)
        print(f"O numero maior é:{maiorNumero} e o menor é: {menorNumero}")
numeroMaior()