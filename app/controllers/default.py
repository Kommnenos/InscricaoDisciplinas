from app import app
from app.models.usuarioPkg.AlunoFactory import AlunoFactory
from app.models.usuarioPkg.Aluno import Aluno

@app.route("/")
def hello():
    aluno = AlunoFactory.criar_usuario("áquila", "50004053826", "aquila@estudante.ufscar.br", "teste")
    print(aluno._nome)
    print(aluno._senha)
    print(aluno._email)
    print(aluno._cpf)

    return "Hello, World!"