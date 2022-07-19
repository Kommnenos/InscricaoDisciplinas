from abc import ABC, abstractmethod
import disciplina
import Usuario
import EstadoInscricao

class InterfaceInscricao(ABC):
    _currentState : EstadoInscricao 
    
    @abstractmethod
    def inscreve_aluno(self, aluno: Usuario.Aluno, disciplina: disciplina.Disciplina) -> bool:
        pass