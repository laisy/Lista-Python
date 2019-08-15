atleta = []
salto = []
k = 0
i = 0
j = 0
saltos = []
soma = 0

nome = raw_input('Digite o nome do atleta: ')
for i in range(5):
    dist = float(raw_input('Digite a distancia do salto: '))
    salto.append(dist)
    soma += dist
escolha = raw_input('Deseja descartar o menor salto? (sim ou nao): ')
if escolha == 'sim':
    for j in range(len(salto)):
        menorSalto = salto[0]
        if (salto[j] > menorSalto):
            saltos.append(salto[j])
if escolha == 'nao':
    for j in range(len(salto)):
        saltos.append(salto[j])

media = soma / len(saltos)

print 'Nome:', nome, ' ', 'Saltos:', saltos, ' ', 'Media:', media
