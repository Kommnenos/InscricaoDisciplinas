import UsuarioFactory
import Usuario
import Aluno

class AlunoFactory(UsuarioFactory):
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        return Aluno(nome, cpf, email, senha, None)