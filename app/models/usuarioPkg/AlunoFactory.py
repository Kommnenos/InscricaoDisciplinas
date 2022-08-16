from app.models.usuarioPkg.UsuarioFactory import UsuarioFactory
from app.models.usuarioPkg.Usuario import Usuario
from app.models.usuarioPkg.Aluno import Aluno


class AlunoFactory(UsuarioFactory):
    def criar_usuario(nome: str, cpf: str, email: str, senha: str) -> Usuario:
        return Aluno(nome, cpf, email, senha, None)