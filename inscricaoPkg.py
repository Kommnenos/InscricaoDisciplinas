from abc import ABC, abstractmethod
import discisplinaPkg

import UsuarioPkg


class InterfaceInscricao(ABC):
    @abstractmethod
    def inscreve_aluno(self, aluno: UsuarioPkg.Aluno, disciplina: discisplinaPkg.Disciplina) -> bool:
        pass


class InscricaoIMP(InterfaceInscricao):
    def __init__(self, estado_fase_inscricao):
        self._estado_fase_inscricao = estado_fase_inscricao

    def inscreve_aluno(self, aluno: UsuarioPkg.Aluno, disciplina: discisplinaPkg.Disciplina) -> bool:
        pass

    def mudar_fase(self, adm: UsuarioPkg.AdmDepartamento):
        pass

    def atualiza_perfil(self, aluno: UsuarioPkg.Aluno):
        pass

    def defere_alunos_automaticamente(self, aluno: UsuarioPkg.Aluno):
        pass


class EstadoInscricao(ABC):
    def inscreve_aluno(self, aluno: UsuarioPkg.Aluno, disciplina: discisplinaPkg.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: UsuarioPkg.AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass


class PrimeiraFase(EstadoInscricao):
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_instance(self) -> EstadoInscricao:
        return self._instance

    def inscreve_aluno(self, aluno: UsuarioPkg.Aluno, disciplina: discisplinaPkg.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: UsuarioPkg.AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass

class SegundaFase(EstadoInscricao):
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_instance(self) -> EstadoInscricao:
        return self._instance

    def inscreve_aluno(self, aluno: UsuarioPkg.Aluno, disciplina: discisplinaPkg.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: UsuarioPkg.AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass

class Indisponivel(EstadoInscricao):
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_instance(self) -> EstadoInscricao:
        return self._instance

    def inscreve_aluno(self, aluno: UsuarioPkg.Aluno, disciplina: discisplinaPkg.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: UsuarioPkg.AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass
