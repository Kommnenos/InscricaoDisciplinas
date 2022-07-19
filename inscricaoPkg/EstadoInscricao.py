from abc import ABC, abstractmethod
import disciplina

import Usuario

class EstadoInscricao(ABC):
    def inscreve_aluno(self, aluno: Usuario.Aluno, disciplina: disciplina.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: Usuario.AdmDepartamento, inscricao_imp: InscricaoIMP):
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

    def inscreve_aluno(self, aluno: Usuario.Aluno, disciplina: disciplina.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: Usuario.AdmDepartamento, inscricao_imp: InscricaoIMP):
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

    def inscreve_aluno(self, aluno: Usuario.Aluno, disciplina: disciplina.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: Usuario.AdmDepartamento, inscricao_imp: InscricaoIMP):
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

    def inscreve_aluno(self, aluno: Usuario.Aluno, disciplina: disciplina.Disciplina,
                       inscricao_imp: InscricaoIMP) -> bool:
        pass

    def mudar_fase(self, adm: Usuario.AdmDepartamento, inscricao_imp: InscricaoIMP):
        pass

