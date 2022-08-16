import datetime
from app.models.cursoPkg.Curso import Curso
from .Periodo import Periodo


class Matricula:
    def __init__(self, data_matricula: datetime.date, curso: Curso, status: str, ra: int, ira: int,
                 perfil: int, periodo: Periodo):
        self._data_matricula = data_matricula
        self._curso = curso
        self._status = status
        self._ra = ra
        self._ira = ira
        self._perfil = perfil
        self._periodo = periodo