from abc import ABC
from disciplinaPkg.Disciplina import Disciplina
from UsuarioPkg.Aluno import Aluno
from UsuarioPkg.AdmDepartamento import AdmDepartamento
from InscricaoIMP import InscricaoIMP


class EstadoInscricao(ABC):
    def inscreve_aluno(self, aluno: Aluno, disciplina: Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass


class PrimeiraFase(EstadoInscricao):
    _instancia = None

    @classmethod
    def instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def get_instancia(self) -> EstadoInscricao:
        return self._instancia

    def inscreve_aluno(self, aluno: Aluno, disciplina: Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass


class SegundaFase(EstadoInscricao):
    _instancia = None

    @classmethod
    def instance(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def get_instance(self) -> EstadoInscricao:
        return self._instancia

    def inscreve_aluno(self, aluno: Aluno, disciplina: Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass


class Indisponivel(EstadoInscricao):
    _instancia = None

    @classmethod
    def instance(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def get_instance(self) -> EstadoInscricao:
        return self._instancia

    def inscreve_aluno(self, aluno: Aluno, disciplina: Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass

