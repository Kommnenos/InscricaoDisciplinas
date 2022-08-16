from abc import ABC, abstractmethod
from app.models.usuarioPkg.Usuario import Usuario


class UsuarioFactory(ABC):
    @abstractmethod
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        pass