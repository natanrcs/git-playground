class Carro:
    def __init__(self, marca, modelo, cavalos):
        self.marca = marca
        self.modelo = modelo
        self.cavalos = cavalos

    def ligar(self):
        return f"O {self.modelo} está ligado. Ele possui {self.cavalos} cavalos e é da marca {self.marca}."

    def desligar(self):
        return f"O {self.modelo} está desligado."


carro1 = Carro("Audi", "Q3", 500)
carro2 = Carro("GM", "Celta Life", 70)
carro3 = Carro("Volws","Jetta",300)

print(carro1.ligar())
print(carro1.desligar())

print(carro2.ligar())
print(carro2.desligar())

print(carro3.ligar())
print(carro3.desligar())

class Contabancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self,valor):
        if valor <= 0:
            return "Valor tem que ser maior que 0!"
        elif valor > self.saldo:
            return "Vc nao tem saldo suficiente!"
        else:
            self.saldo -= valor
            return "Saque com sucesso"
        

    
    def depositar(self,valor):
        if valor <= 0:
            return "Deposito acima de 0!"
        else:
            self.saldo += valor
        return f"{valor} depositado com sucesso!"
    
    def consultar_saldo(self):
        return f"Titular:{self.titular} Seu saldo é de:{self.saldo}"

conta1 = Contabancaria("Natan",100)
conta2 = Contabancaria("Gabi",500)
print(conta1.consultar_saldo())
print(conta1.depositar(100))
print(conta1.sacar(50))


        
        