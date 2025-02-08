from abc import ABC, abstractmethod
import random

class lutador(ABC):
    
    @abstractmethod
    def atacar(self):
        pass
        
    @abstractmethod
    def defender(self, dano_recebido):
        pass
    
    @abstractmethod
    def obtervida(self):
        pass
    

class Superman(lutador):
    def __init__(self,ataquenormal,vida, dano):
        self.ataquenormal = ataquenormal
        self.vida = vida
        self.dano = dano
        self.pocoes = 3
    
    def atacar(self):
        if random.random() > 0.5:
            return self.ataquenormal + self.dano
        else:
            return (self.ataquenormal + self.dano) * 2
        
    def defender(self, dano_recebido):
        if random.random() > 0.5:
            print(f"O Superman defendeu-se! Vida restante: {self.vida}")
        else:
            self.vida -= dano_recebido
            print(f"O Superman não conseguiu defender-se! Vida restante: {self.vida}")
    
    def obtervida(self):
        if self.pocoes > 0:
            self.vida = 2000
            self.pocoes -= 1
            print(f"O Superman regenerou a vida totalmente! Poções restantes: {self.pocoes}")
        else:
            print("O Superman não tem mais poções!")


class MulherMaravilha(lutador):
    def __init__(self,ataquenormal,vida, dano):
        self.ataquenormal = ataquenormal
        self.vida = vida
        self.dano = dano
        self.pocoes = 3
    
    def atacar(self):
        if random.random() > 0.5:
            return self.ataquenormal + self.dano
        else:
            return (self.ataquenormal + self.dano) * 2
        
    def defender(self, dano_recebido):
        if random.random() > 0.5:
            print(f"A Mulher Maravilha defendeu-se! Vida restante: {self.vida}")
        else:
            self.vida -= dano_recebido
            print(f"A Mulher Maravilha não conseguiu defender-se! Vida restante: {self.vida}")
    
    def obtervida(self):
        if self.pocoes > 0:
            self.vida = 2000
            self.pocoes -= 1
            print(f"A Mulher Maravilha regenerou a vida totalmente! Poções restantes: {self.pocoes}")
        else:
            print("A Mulher Maravilha não tem mais poções!")


class Thor(lutador):
    def __init__(self,ataquenormal,vida, dano):
        self.ataquenormal = ataquenormal
        self.vida = vida
        self.dano = dano
        self.pocoes = 3
    
    def atacar(self):
        if random.random() > 0.5:
            return self.ataquenormal + self.dano
        else:
            return (self.ataquenormal + self.dano) * 2
        
    def defender(self, dano_recebido):
        if random.random() > 0.5:
            print(f"O Thor defendeu-se! Vida restante: {self.vida}")
        else:
            self.vida -= dano_recebido
            print(f"O Thor não conseguiu defender-se! Vida restante: {self.vida}")
    
    def obtervida(self):
        if self.pocoes > 0:
            self.vida = 2000
            self.pocoes -= 1
            print(f"O Thor regenerou a vida totalmente! Poções restantes: {self.pocoes}")
        else:
            print("O Thor não tem mais poções!")

heroi1 = Superman(150, 2000, 300)
heroi2 = MulherMaravilha(140, 2200, 290)
heroi3 = Thor(180, 1500, 400)

def escolher_heroi(mensagem, escolha_proibida=None):
    while True:
        escolha = input(mensagem)
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha in [1, 2, 3] and escolha != escolha_proibida:
                return escolha
            elif escolha == escolha_proibida:
                print("Você já escolheu este herói! Escolha um herói diferente.")
            else:
                print("Escolha inválida! Por favor, escolha um número entre 1 e 3.")
        else:
            print("Entrada inválida! Por favor, digite um número.")

print(' ---------------- Programa de Luta de super Herois!! ---------------- ')
print()

print('Por favor escolha dois Super Heroi para o sua luta:')
print('1 = Superman')
print('2 = Mulher Maravilha')
print('3 = Thor')

escolha1 = escolher_heroi('Qual o primeiro Super-Herói? (1, 2, 3): ')
escolha2 = escolher_heroi('Qual o segundo Super-Herói? (1, 2, 3): ', escolha_proibida = escolha1)

lutadores = [heroi1, heroi2, heroi3]
heroi_escolhido1 = lutadores[escolha1 - 1]
heroi_escolhido2 = lutadores[escolha2 - 1]

print(f"Heróis escolhidos: {type(heroi_escolhido1).__name__} e {type(heroi_escolhido2).__name__}")

print()
print("A luta começou!")

while heroi_escolhido1.vida > 0 and heroi_escolhido2.vida > 0:

    acao = input(f"{type(heroi_escolhido1).__name__}, você quer 'atacar' ou 'usar poção'? ").lower()
    if acao == "atacar":
        dano1 = heroi_escolhido1.atacar()
        print(f"{type(heroi_escolhido1).__name__} atacou causando {dano1} de dano!")
        heroi_escolhido2.defender(dano1)

    if heroi_escolhido2.vida <= 0:
        print(f"{type(heroi_escolhido2).__name__} foi derrotado!")
        break

    acao = input(f"{type(heroi_escolhido2).__name__}, você quer 'atacar' ou 'usar poção'? ").lower()
    if acao == "atacar":
        dano2 = heroi_escolhido2.atacar()
        print(f"{type(heroi_escolhido2).__name__} atacou causando {dano2} de dano!")
        heroi_escolhido1.defender(dano2)

    if heroi_escolhido1.vida <= 0:
        print(f"{type(heroi_escolhido1).__name__} foi derrotado!")
        break

if heroi_escolhido1.vida > 0:
    print(f"{type(heroi_escolhido1).__name__} é o vencedor com {heroi_escolhido1.vida} de vida restante!")
else:
    print(f"{type(heroi_escolhido2).__name__} é o vencedor com {heroi_escolhido2.vida} de vida restante!")
    
    

