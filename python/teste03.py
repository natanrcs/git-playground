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
        