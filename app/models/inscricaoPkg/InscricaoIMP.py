
from disciplinaPkg.Disciplina import Disciplina
from UsuarioPkg.Aluno import Aluno
from UsuarioPkg.AdmDepartamento import AdmDepartamento
from Iinscricao import InterfaceInscricao


class InscricaoIMP(InterfaceInscricao):
    def __init__(self, estado_fase_inscricao):
        self._estado_fase_inscricao = estado_fase_inscricao

    def inscreve_aluno(self, aluno: Aluno, disciplina: Disciplina) -> bool:
        pass

    def mudar_fase(self, adm: AdmDepartamento):
        pass

    def atualiza_perfil(self, aluno: Aluno):
        pass

    def defere_alunos_automaticamente(self, aluno: Aluno):
        pass