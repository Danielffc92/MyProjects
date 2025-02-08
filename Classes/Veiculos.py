class Veiculo:
    
    def __init__(self,marca, ano):
        self.marca = marca
        self.ano = ano
    
    def __str__(marca):
        return marca
    
    def __int__(ano):
        return ano
    
    def infoGerais(self):
        print(f"A marca do veiculo é {self.marca} e foi fabricado no ano {self.ano}.")

class Carro(Veiculo):
    def __init__(self, marca, ano, numeroportas):
        super().__init__(marca, ano)
        self.numeroportas = numeroportas
        
    def __str__(marca):
        return marca
    
    def __int__(ano, numeroportas):
        return super().__init__(numeroportas)
    
    def infoGerais(self):
        print(f"A marca do carro é {self.marca}, foi fabricado no ano {self.ano}, e tem {self.numeroportas} portas.")
  
class Mota(Veiculo):
    
    def __init__(self, marca, ano, tipodemota):
        super().__init__(marca, ano)
        self.tipodemota = tipodemota
        
    def __str__(marca, tipodemota):
        return super().__init__(tipodemota)
    
    def __int__(ano):
        return ano
    
    def infoGerais(self):
        print(f"A marca da mota é {self.marca}, foi fabricada no ano {self.ano}, e é do tipo: {self.tipodemota}.")
    
    
autocarro = Veiculo('Mercedes', 2004)
autocarro.infoGerais()

carro = Carro('Volvo', 2011, 5)
carro.infoGerais()

mota = Mota('Kawasaki', 2022, 'Scooter')
mota.infoGerais()