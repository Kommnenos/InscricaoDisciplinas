from abc import ABC, abstractmethod
import matriculaPkg

class Usuario(ABC):
    def __init__(self, nome: str, cpf: str, email: str, senha: str):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._senha = senha


