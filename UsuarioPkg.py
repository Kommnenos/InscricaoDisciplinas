from abc import ABC, abstractmethod
import matriculaPkg


class Usuario(ABC):
    def __init__(self, nome: str, cpf: str, email: str, senha: str):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._senha = senha


class Aluno(Usuario):
    def __init__(self, nome: str, cpf: str, email: str, senha: str, matricula: matriculaPkg.Matricula):
        super().__init__(nome, cpf, email, senha)
        self._matricula = matricula


class AdmDepartamento(Usuario):
    def __init__(self, nome: str, cpf: str, email: str, senha: str, numero_adm: int, cargo: str):
        super().__init__(nome, cpf, email, senha)
        self._numero_adm = numero_adm
        self._cargo = cargo


class UsuarioFactory(ABC):
    @abstractmethod
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        pass


class AlunoFactory(UsuarioFactory):
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        return Aluno(nome, cpf, email, senha, None)


class AdmDepartamentoFactory(UsuarioFactory):
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        return AdmDepartamento(nome, cpf, email, senha, None, None)


class InteraceValidaLogin(ABC):
    @abstractmethod
    def verifica_email(self, email: str, token) -> Usuario:
        pass

    def verifica_senha(self, senha: str, token) -> bool:
        pass


class ValidaDadosUsuarioIMP(InteraceValidaLogin):
    def verifica_email(self, email: str, token) -> Usuario:
        pass

    def verifica_senha(self, senha: str, token) -> bool:
        pass
