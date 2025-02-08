class conta:
    def __init__(self, titular, numerodeconta, quantidade):
        self.titular = titular
        self.numerodeconta = numerodeconta
        self.quantidade = quantidade
        
    def info(self):
        print(f'O nome do Titular é {self.titular}, o número de conta é {self.numerodeconta}, e tem {self.quantidade}€.')  

conta1 = conta('Daniel', 2876531, 1000)
conta2 = conta('Rafaela', 4358791, 350) 



conta1.info()
conta2.info()

if conta1.quantidade > conta2.quantidade:
    print(f'A {conta1.titular} tem mais dinheiro!')
else:
    print(f'A {conta2.titular} tem mais dinheiro!')