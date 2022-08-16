from Usuario import Usuario
from abc import ABC, abstractmethod


class InterfaceValidaLogin(ABC):
    @abstractmethod
    def verifica_email(self, email: str, token) -> Usuario:
        pass

    def verifica_senha(self, senha: str, token) -> bool:
        pass