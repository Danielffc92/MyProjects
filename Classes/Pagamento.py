class FormaDePagamento():
    def __init__(self):
        pass
    
    def processarPagamento(self):
        print("O seu pagamento está a ser processado...")
        
class CartaoCredito(FormaDePagamento):
    def __init__(self, numerocartao, nome, validadecartao, CVC):
        super().__init__()
        self.numerocartao = numerocartao
        self.nome = nome
        self.validadecartao = validadecartao
        self.CVC = CVC
        
    def __str__(self):
        return f"Nome: {self.nome}, validade: {self.validadecartao}"
        
    def processarPagamento(self):
        print(f" O pagamento está a ser processado através do cartão nº: {self.numerocartao}, com a validade {self.validadecartao}, com o nome {self.nome}")
        
class Paypal(FormaDePagamento):
    def __init__(self, email, nomeConta):
        super().__init__()
        self.email = email
        self.nomeConta = nomeConta
        
    def __str__(self):
        return f"Email: {self.email}, Nome da Conta: {self.nomeConta}"
        
    def processarPagamento(self):
        print(f"O pagamento por Paypal está a ser processado através do e-mail: {self.email}, com o nome de conta {self.nomeConta}")
        
        

print("Por favor, escolha um dos métodos de pagamento abaixo:")
print("1. Paypal")
print("2. Cartão de Crédito")

escolha = input("Digite o número da sua escolha (1 ou 2): ")

while escolha not in ['1', '2']:
    print("Opção inválida! Por favor, escolha novamente:")
    escolha = input("Digite o número da sua escolha (1 ou 2): ")
    
    if escolha == "1":
        email = input('Digite o seu email: ')
        nomeconta = input('Digite o nome da conta: ')
        pagamento_paypal = Paypal(email, nomeconta)
        pagamento_paypal.processarPagamento()
    
    elif escolha == "2":
        numerocartao = int(input('Digite o número do cartão: '))
        nome = input('Digite o nome no Cartão: ')
        validadecartao = input('Digite a validade do cartão: ')
        CVC = int(input('Digite o número CVC do cartão: '))
        pagamento_cartao = CartaoCredito(numerocartao, nome, validadecartao, CVC)
        pagamento_cartao.processarPagamento()

