# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

alunos = ["Ana", "João", "Maria", "Pedro", "Sofia", "Carlos", "Mariana", "Luís", "Laura", "Gabriel"]

aluno = choice(alunos)

print('O aluno escolhido foi:', aluno)