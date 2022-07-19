import Usuario
import UsuarioFactory
import AdmDepartamento

class AdmDepartamentoFactory(UsuarioFactory):
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str) -> Usuario:
        return AdmDepartamento(nome, cpf, email, senha, None, None)