import Usuario
import InterfaceValidaLogin

class ValidaDadosUsuarioIMP(InterfaceValidaLogin):
    def verifica_email(self, email: str, token) -> Usuario:
        pass

    def verifica_senha(self, senha: str, token) -> bool:
        pass