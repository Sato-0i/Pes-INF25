class Aluno:
        def __init__(self,nome,idade):
                self.nome = nome
                self.idade = idade

Luiz = Aluno ("luiz Shalatovesck", 16)
Vitoria = Aluno ("Vitoria Garcia",17 )
Vitor = Aluno ("Vitor Roberto de Oliveira", 16)

alunos = [Luiz, Vitoria, Vitor]

for alunos in alunos:
    print ("Aluno" , aluno.nome, "idade", aluno.idade)
