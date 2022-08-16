from app.models.usuarioPkg.Usuario import Usuario
from app.models.matriculaPkg.Matricula import Matricula


class Aluno(Usuario):
    def __init__(self, nome: str, cpf: str, email: str, senha: str, matricula: Matricula):
        super().__init__(nome, cpf, email, senha)
        self._matricula = matricula