class Aluno:
    def __init__(self, nome, idade, curso, matricula):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula
        
    def __str__(self, nome, curso, matricula):
        return (f"{self.nome} {self.curso} {self.matricula}")
    
    def __int__(self, idade):
        return (f"{self.idade}")
        
    def informacoes(self):
        print(f"O nome é {self.nome}.")
        print(f"A idade é {self.idade}.")
        
    def informacao_detalhada(self):
        print(f"O Aluno(a) chama-se {self.nome}, tem {self.idade} anos, está no curso {self.curso}, e tem a matricula nº {self.matricula}.")