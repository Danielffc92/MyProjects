#Estamos a criar a classe carro
class Carro:
    def __init__(self,marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade

#Definir que a variavel marca como string   
    def __str__(self):
        return self.marca
    
#Definir que a variavel velocidade é um inteiro
    def __int__(self):
        return self.velocidade
    
#Estamos a definir a marca do carro    
    def nomedocarro(self):
        print(f'O marca do carro é {self.marca}!')    
        
#Estamos a definir a velocidade do carro
    def velocidademaxima(self):
        print(f'A velocidade máxima do carro é {self.velocidade} km/h!')
        
    @staticmethod
    def vencedor(Carro1,Carro2,Carro3):
        if Carro1.velocidade > Carro2.velocidade and Carro1.velocidade > Carro3.velocidade:
            return Carro1
        elif Carro2.velocidade > Carro1.velocidade and Carro2.velocidade > Carro3.velocidade:
            return Carro2
        elif Carro3.velocidade > Carro1.velocidade and Carro3.velocidade > Carro2.velocidade:
            return Carro3
        else:
            return None
            


print('-------------- Bem vindo à corrida do século!!! --------------')
print('Escolha com que Carro deseja correr e boa sorte na corrida!!')
print()

Carro1 = Carro('Volvo', 200)
Carro2 = Carro('BMW', 220) 
Carro3 = Carro('Mercedes', 225)

print('Carro 1:', Carro1)
print('Carro 2:', Carro2)
print('Carro 3:', Carro3)
print()

escolhacarro = int(input('Qual o Carro que quer escolher para a corrida? (1,2,3): '))

if escolhacarro == 1:
    escolhido = Carro1
elif escolhacarro == 2:
    escolhido = Carro2
elif escolhacarro == 3:
    escolhido = Carro3
else:
    escolhido = None
    print('Não escolheu nenhum carro!!')

print('----------') 
Carro1.nomedocarro()   
Carro1.velocidademaxima()

print('----------') 
Carro2.nomedocarro()   
Carro2.velocidademaxima()

print('----------') 
Carro3.nomedocarro()   
Carro3.velocidademaxima()

print('----------')
vencedor = Carro.vencedor(Carro1,Carro2,Carro3)

if vencedor:
   print(f'O carro vencedor é o {vencedor.marca} com a velocidade de {vencedor.velocidade} km/h!')
else:
    print('Não temos Vencedor!!')

print('----------') 
if escolhido == vencedor:
    print('PARANBÉNS O TEU CARRO VENCEU!! *,* ')
else:
    print('Nao escolheste o carro vencedor!! :( ')
