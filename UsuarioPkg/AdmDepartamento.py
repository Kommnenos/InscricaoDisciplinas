import matriculaPkg
import Usuario

class AdmDepartamento(Usuario):
    def __init__(self, nome: str, cpf: str, email: str, senha: str, numero_adm: int, cargo: str):
        super().__init__(nome, cpf, email, senha)
        self._numero_adm = numero_adm
        self._cargo = cargo