import disciplina
import Usuario
import InterfaceInscricao

class InscricaoIMP(InterfaceInscricao):
    def __init__(self, estado_fase_inscricao):
        self._estado_fase_inscricao = estado_fase_inscricao

    def inscreve_aluno(self, aluno: Usuario.Aluno, disciplina: disciplina.Disciplina) -> bool:
        pass

    def mudar_fase(self, adm: Usuario.AdmDepartamento):
        pass

    def atualiza_perfil(self, aluno: Usuario.Aluno):
        pass

    def defere_alunos_automaticamente(self, aluno: Usuario.Aluno):
        pass