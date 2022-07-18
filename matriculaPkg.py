import datetime
import cursoPkg
import discisplinaPkg


class Periodo:
    def __init__(self, disciplinas: list[discisplinaPkg.Disciplina], ano: int, creditos: int, max_credito: int):
        self._disciplinas = disciplinas
        self._ano = ano
        self._creditos = creditos
        self._max_credito = max_credito

    def consultar_disciplinas_aluno_do_periodo(self):
        pass


class Matricula:
    def __init__(self, data_matricula: datetime.date, curso: cursoPkg.Curso, status: str, ra: int, ira: int,
                 perfil: int, periodo: Periodo):
        self._data_matricula = data_matricula
        self._curso = curso
        self._status = status
        self._ra = ra
        self._ira = ira
        self._perfil = perfil
        self._periodo = periodo
