import datetime
import curso
import disciplina


class Periodo:
    def __init__(self, disciplinas: list[discisplinaPkg.Disciplina], ano: int, creditos: int, max_credito: int):
        self._disciplinas = disciplinas
        self._ano = ano
        self._creditos = creditos
        self._max_credito = max_credito

    def consultar_disciplinas_aluno_do_periodo(self):
        pass
