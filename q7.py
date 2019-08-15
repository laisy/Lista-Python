temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
soma = 0
acimaMedia = {}

for i in range(len(meses)):
    temp = float(raw_input('Informe a temperatura media considerando a ordem dos meses: \n'))
    soma += temp
    temperatura.append(temp)

media = float(soma/12)

for i in range(len(meses)):
    if(temperatura[i] > media):
        acimaMedia.update({meses[i] : temperatura[i]})

print 'Media das temperaturas anual: \n', media
print 'Meses com temperaturas acima da media: \n', acimaMedia
