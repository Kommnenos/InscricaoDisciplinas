from UsuarioPkg.Aluno import Aluno
from cursoPkg.Curso import Curso
from UsuarioPkg.AdmDepartamento import AdmDepartamento


class MatriculaController:
    def matricular_aluno(self, aluno: Aluno, curso: Curso, adm_departamento: AdmDepartamento) -> bool:
        pass

    def desativar_matricula(self, adm_departamento: AdmDepartamento) -> bool:
        pass