from abc import ABC, abstractmethod


class UsuarioFactory(ABC):
    @abstractmethod
    def createUsuario(self):
        pass
