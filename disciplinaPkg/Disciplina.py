import curso


class Disciplina:
    def __init__(self, nome: str, codigo: int, numero_vagas: int, deferidos, curso: curso.Curso, perfil: int):
        self._nome = nome
        self._codigo = codigo
        self._numero_vagas = numero_vagas
        self._deferidos = deferidos
        self._curso = curso
        self._perfil = perfil

    def consultar_alunos_disciplina(self):
        pass

    def consultar_numero_vagas_disciplina(self) -> int:
        pass
