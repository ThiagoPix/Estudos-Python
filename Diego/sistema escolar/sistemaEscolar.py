import pandas as pd


class SistemaEscolar:
    def __init__(self, planilha):
        self.dados = pd.read_excel(planilha)

    def matricular_aluno(self, nome_aluno, turma):
        index_aluno = self._encontrar_aluno(nome_aluno)
        if index_aluno is not None:
            self.dados.at[index_aluno, 'Matriculado'] = True
            self.dados.at[index_aluno, 'Turma'] = turma
            self._salvar_planilha()

    def desmatricular_aluno(self, nome_aluno):
        index_aluno = self._encontrar_aluno(nome_aluno)
        if index_aluno is not None:
            self.dados.at[index_aluno, 'Matriculado'] = False
            self.dados.at[index_aluno, 'Turma'] = None
            self._salvar_planilha()

    def mudar_turma(self, nome_aluno, nova_turma):
        index_aluno = self._encontrar_aluno(nome_aluno)
        if index_aluno is not None:
            self.dados.at[index_aluno, 'Turma'] = nova_turma
            self._salvar_planilha()

    def cadastrar_aluno(self, nome_aluno, turma, matriculado):
        novo_aluno = pd.DataFrame({'Nome': [nome_aluno], 'Turma': [turma], 'Matriculado': [matriculado]})
        self.dados = pd.concat([self.dados, novo_aluno], ignore_index=True)
        self._salvar_planilha()

    def _encontrar_aluno(self, nome_aluno):
        index_aluno = self.dados.index[self.dados['Nome'] == nome_aluno].tolist()
        if index_aluno:
            return index_aluno[0]
        else:
            print(f"Aluno '{nome_aluno}' não encontrado.")
            return None

    def _salvar_planilha(self):
        self.dados.to_excel('dados_escolares.xlsx', index=False)


sistema = SistemaEscolar('sistema_escolar.xlsx')

sistema.matricular_aluno('João', 'A')

sistema.desmatricular_aluno('Maria')

sistema.mudar_turma('Pedro', 'B')

sistema.cadastrar_aluno('Carlos', 'C', True)
