from abc import ABC, abstractmethod
from disciplinaPkg.Disciplina import Disciplina
from UsuarioPkg.Aluno import Aluno
import EstadoInscricao


class InterfaceInscricao(ABC):
    _currentState : EstadoInscricao 
    
    @abstractmethod
    def inscreve_aluno(self, aluno: Aluno, disciplina: Disciplina) -> bool:
        pass
