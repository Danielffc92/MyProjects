class ContaBancaria:
    def __init__(self, nometit, nconta, saldo):
        self.__nometit = nometit
        self.__nconta = nconta
        self.__saldo = saldo 
    
    def __str__(self):
        return f"Titular: {self.__nometit}, Número da Conta: {self.__nconta}, Saldo: {self.__saldo:.2f}€"    
    
    def __int__ (self):
        return self.__nconta
    
    def __float__ (self):
        return self.__saldo
        
    def levantar(self, quantia):
        if self.__saldo >= quantia and quantia > 0:
            self.__saldo -= quantia
            return f"Levantamento de {quantia:.2f}€ realizado com sucesso!"
        else:
            return "Saldo insuficiente"
            
    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia
            return f"Depósito de {quantia:.2f}€ realizado com sucesso!"
        else:
            return "Erro no depósito: quantia inválida. Verifique o saldo da sua conta"
            
    def verificarSaldo(self):
        return f"O saldo da conta é: {self.__saldo:.2f}€"
        
    def titular(self):
        return f"O nome do titular da conta é: {self.__nometit:.2f}"
        
    def numeroConta(self):
        return f"O número da conta é: {self.__nconta}"


print(' ------------------ Programa de gestão de contas bancárias ------------------')
print()

nometitular = input('Digite o nome do titular da conta: ')
nconta = int(input('Digite o número da conta: '))
saldo_inicial = float(input('Digite o saldo inicial da sua conta: '))

conta = ContaBancaria(nometitular, nconta, saldo_inicial)

print('Bem Vindo(a)', nometitular)
print('Deseja levantar dinheiro - opção 1')
print('Deseja depositar dinheiro - opção 2')
print('Deseja verificar saldo - opção 3')

operacoes = int(input('Qual das operações deseja realizar? (1,2,3): '))

if operacoes == 1:
    valorLev = float(input('Digite o valor que deseja levantar: '))
    print(conta.levantar(valorLev))
elif operacoes == 2:
    valorDep = float(input('Digite o valor que deseja depositar: '))
    print(conta.levantar(valorDep))
elif operacoes == 3:
    print(conta.verificarSaldo())
else:
    print('Operação inválida!!')

print("\nDetalhes da sua conta:")
print(conta) 
