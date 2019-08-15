notas = []
qnt = 0
soma = 0
cont = 0
valAcima = 0
val = 0
conta = 0

n = str(raw_input('Informe as notas: \n'))
notas.append(n)
while n != '-1':
    n = str(raw_input())
    qnt += 1
    if n != '-1':
        notas.append(n)

print 'Quantidade valores lidos:', qnt
print 'Notas: ', (" ".join(notas))

print 'Ordem inversa: '
for k in range(qnt):
    num = notas[-1- k]
    print num

for k in range(len(notas)):
    soma = soma + float(notas[k])
print 'Soma: ', soma

mediaa = float(soma / qnt)
media =  round(mediaa, 2)
print 'Media: ', media

for k in range(len(notas)):
    val = float(notas[k])
    if val > media:
        cont += 1
    if val < 9:
        conta += 1

print 'Quantidade de valores acima da media: ', cont
print 'Quantidade de valores abaixo de nove: ', conta
print 'Fim!'
