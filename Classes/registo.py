from alunos import Aluno

aluno1 = Aluno("Daniel", 32, "Programação Python", "1000")
aluno2 = Aluno("Rafaela", 30, "Masters SQL", "345")
aluno3 = Aluno("Tiago", 24, "HTML Masters", "250")
aluno4 = Aluno("Marcel", 27, "Redes e infrastruturas", "677")
aluno5 = Aluno("Miguel", 35, "Redes e infrastruturas", "890")
aluno6 = Aluno("António", 31, "Programação Python", "1020")

print(' ------------- Programa de adição de Alunos -------------')
print()

novoaluno = str(input('Deseja criar novo aluno?  (S/N)')).upper()
    
# Lista para adicionar novos alunos
ListaAlunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6] 

def adicionaraluno():

    global ListaAlunos
    
    if novoaluno == "S":
        #Colectar os dados do novo aluno
        nome = str(input('Digite o nome do Aluno(A): '))
        idade = int(input('Digite a Idade do Aluno(a): '))
        curso = str(input('Digite o Curso do Aluno(a): '))
        matricula = str(input('Digite o número de matricula do Aluno(a): '))
        
         # Criar um novo aluno
        novo_aluno = Aluno(nome, idade, curso, matricula)
        
        # Adicionar novo aluno à lista
        ListaAlunos.append(novo_aluno)  

        #Mostra os dados do novo aluno
        print()
        print("Novo aluno adicionado com sucesso! \n")
        print("Dados do novo aluno: ")
        print(f"Nome: {novo_aluno.nome}")
        print(f"idade: {novo_aluno.idade}")
        print(f"curso: {novo_aluno.curso}")    
        print(f"Nº matricula: {novo_aluno.matricula}")    
    else:
        print("Não foi adicionado nenhum aluno.")
        
#chamar função que vai mostrar os dados da nova inscrição 
adicionaraluno()
adicionaraluno()


alunosExistentes = str(input('Deseja ver a lista dos alunos existentes?  (S/N)')).upper()

def mostrar_alunos_existentes():  

    if alunosExistentes == "S":
        print(f"Lista de Alunos já existentes: \n")
      

        global ListaAlunos
      
        for aluno in ListaAlunos:
            aluno.informacoes()
    else:
        print("A lista está vazia! Não existem alunos inscritos em nenhum curso.")

print()

alunosExistentesdetalhes = str(input('Deseja ver os detalhes dos alunos existentes?  (S/N)')).upper()
      
def mostrar_detalhes_alunos():
    if alunosExistentesdetalhes == "S":
        print(f"Lista detalhad dos Alunos: \n")
    
        for aluno in ListaAlunos:
            aluno.informacao_detalhada()

#chamar função dos alunos existentes
mostrar_alunos_existentes()
mostrar_detalhes_alunos()
