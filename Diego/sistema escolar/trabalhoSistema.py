import pandas as pd


class SistemaEducacional:
    def __init__(self, bancoDeDados):
        self.bancoDeDados = pd.read_excel(bancoDeDados)

    def ordenar(self):
        self.bancoDeDados = self.bancoDeDados.sort_values(by=[
            'Turma', 'Matriculado', 'Nome'
            ])

    def listaDeAlunos(self):
        resposta = str(input("""
Escolha:
1 - Lista Completa
2 - Matriculados
3 - Nao matriculados
Digite: """
                             ))

        if resposta == '1':
            print(self.bancoDeDados)

        elif resposta == '2':
            alunosMatriculados = self.bancoDeDados[self.bancoDeDados[
                'Matriculado'] == True]
            print(alunosMatriculados)

        elif resposta == '3':
            alunosNaoMatriculados = self.bancoDeDados[self.bancoDeDados[
                'Matriculado'] == False]
            print(alunosNaoMatriculados)

    def matricularAluno(self):
        resposta = int(input("""
Escolha:
1 - Aluno Novo
2 - Aluno Evadido
Digite: """))
        if resposta == 1:
            nome = str(input('Digite o nome do aluno: '))
            turma = str(input('Digite a turma do aluno: '))
            matricula = True

            alunoNovo = pd.DataFrame({
                'Nome': [nome],
                'Turma': [turma],
                'Matriculado': [matricula],
                'P1': [0.0],
                'P2': [0.0],
                'Trabalho': [0.0],
                'Media': [0.0],
                'Frequencia': [0.0],
                'Resultado': ['Reprovado']
                })

            self.bancoDeDados = pd.concat(
                [self.bancoDeDados, alunoNovo],
                )
            self.bancoDeDados.reset_index(drop=True, inplace=True)
        else:
            alunosNaoMatriculados = self.bancoDeDados[
                self.bancoDeDados['Matriculado'] == False]
            print(alunosNaoMatriculados)
            indice = int(input("""
Escolha o indice de um dos alunos nao matriculados
acima para reativar a matricula """))
            self.bancoDeDados.at[indice, 'Matriculado'] = True

    def desmatricularAluno(self):
        alunosMatriculados = self.bancoDeDados[
            self.bancoDeDados['Matriculado'] == True]
        print(alunosMatriculados)
        indice = int(input("""
Escolha o indice de um dos alunos matriculados
acima para desativar a matricula """))
        self.bancoDeDados.at[indice, 'Matriculado'] = False

    def lançamentoDeNota(self):
        self.bancoDeDados = self.bancoDeDados
        resposta = int(input("""
Escolha Aonde voce quer lançar a nota:
1 - P1
2 - P2
3 - Trabalho
Digite: """
                             ))
        if resposta == 1:
            for i in range(0, len(self.bancoDeDados)):
                nome = self.bancoDeDados.at[i, 'Nome']
                p1 = float(input(f'Digite a nota do aluno {nome}: '))
                self.bancoDeDados.at[i, "P1"] = p1

        elif resposta == 2:
            for i in range(0, len(self.bancoDeDados)):
                nome = self.bancoDeDados.at[i, 'Nome']
                p2 = float(input(f'Digite a nota do aluno {nome}: '))
                self.bancoDeDados.at[i, "P2"] = p2

        elif resposta == 3:
            for i in range(0, len(self.bancoDeDados)):
                nome = self.bancoDeDados.at[i, 'Nome']
                trab = float(input(f'Digite a nota do aluno {nome}: '))
                self.bancoDeDados.at[i, "Trabalho"] = trab

    def calcularMedia(self):
        for i in range(0, len(self.bancoDeDados)):
            media = round((
                self.bancoDeDados.at[i, 'P1'] + self.bancoDeDados.at[i, 'P2']
                + self.bancoDeDados.at[i, 'Trabalho']
                )/3, 2)
            self.bancoDeDados.at[i, "Media"] = media

    def frequencia(self):
        return 0


escola = SistemaEducacional("sistema_escolar.xlsx")
while True:
    resposta = int(input("""
-------- Sistema Educacional --------
| 1 - Matricular Aluno              |
| 2 - Desmatricular Aluno           |
| 3 - Lançamento de Notas           |
| 4 - Calcular Média                |
| 5 - Lista de Alunos               |
| 6 - Ordenar lista de Alunos       |
-------------------------------------
"""))
    if resposta == 1:
        escola.matricularAluno()
    elif resposta == 2:
        escola.desmatricularAluno()
    elif resposta == 3:
        escola.lançamentoDeNota()
    elif resposta == 4:
        escola.calcularMedia()
    elif resposta == 5:
        escola.listaDeAlunos()
    elif resposta == 6:
        escola.ordenar()
    else:
        break