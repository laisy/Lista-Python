n = int(raw_input('Informe a quantidade de pessoas: ' ))
info = {}
pessoas = []
cont = 0
posi = []
posi.append(cont)

for k in range(n):
        nome = raw_input('Nome: ')
        cont += 1
        posi.append(cont)
        tel = int(raw_input('Telefone: '))
        cont += 1
        posi.append(cont)
        id = int(raw_input('Idade: '))
        cont += 1
        posi.append(cont)

        pessoas.append(id)
        pessoas.append(tel)
        pessoas.append(nome)

for i in range(len(pessoas)):
        info.update({posi[i] : pessoas[i]})

print info
