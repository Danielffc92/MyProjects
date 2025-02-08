print(' ---------- Bem-vindo à Escolha do Caminho ---------- ')
print()

caminhos = str(input('Deseja ir por que Caminho? (A/B/C) '))

def escolhaCaminho():         
    if caminhos == "A" or caminhos == "a":
        print('Escolheu o Caminho A! Boa escolha é o melhor caminho! :D ')
        
    elif caminhos == "B" or caminhos == "b":
         print('Escolheu o Caminho B! Podia ter sido uma escolha melhor! :S ')
         
    elif caminhos == "C" or caminhos == "c":
        print('Escolheu o Caminho C! PÉSSIMA ESCOLHA! ESTE É O PIOR CAMINHO!!!! :@ ')
        
    else:
        print('Pff escolha um caminho.')
        
escolhaCaminho()
print()