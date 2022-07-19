import Usuario
import matriculaPkg

class Aluno(Usuario):
    def __init__(self, nome: str, cpf: str, email: str, senha: str, matricula: matriculaPkg.Matricula):
        super().__init__(nome, cpf, email, senha)
        self._matricula = matricula