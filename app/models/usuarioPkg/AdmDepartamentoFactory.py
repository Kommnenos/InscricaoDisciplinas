from UsuarioPkg.Usuario import Usuario
from UsuarioFactory import UsuarioFactory
from AdmDepartamento import AdmDepartamento


class AdmDepartamentoFactory(UsuarioFactory):
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        return AdmDepartamento(nome, cpf, email, senha, None, None)