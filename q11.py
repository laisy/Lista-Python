dic = {}
classi = []
possi = ['1lugar', '2lugar', '3lugar', '4lugar', '5lugar', '6lugar']
total = {}
corredores = []
media = 0

for k in range(6):
    corredor = raw_input('Digite o nome do corredor: ')
    soma = 0
    corredores.append(corredor)
    for i in range(10):
        voltas = float(raw_input('Informe o tempo das voltas: '))
        dic[corredor + str(i)] = voltas
        soma += voltas
        media = float(soma/10)
        classi.append(media)


melhorVolta = 0
for k in dic:
    n = dic[k]
    if (melhorVolta < n):
        melhorVolta = n
        corr = k

classi.sort()

for i in range(len(possi)):
    total.update({possi[i] : classi[i]})

print 'Melhor Volta:', '\n', melhorVolta, 'de', corr
print 'Classificacao final: ', '\n', total
