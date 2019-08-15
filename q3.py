n = int(raw_input('Digite o numero de alunos: '))
soma = 0
cont = 0
alturas = []

for k in range(n):
    idade = int(raw_input('Digite a idade do aluno: '))
    altura =float(raw_input('Digite a altura do aluno: '))
    soma = soma + altura
    if idade > 13:
        alturas.append(altura)

media = float(soma / n)

for k in range(len(alturas)):
    if alturas[k] < media:
        cont += 1

print cont, 'alunos com mais de 13 anos tem altura inferior a media de alturas! '
