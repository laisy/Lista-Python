k = 0
idade = []
altura = []

for k in range(5):
    id = int(raw_input('Digite a idade: '))
    idade.append(id)
    alt = float(raw_input('Digite a altura: '))
    altura.append(alt)

idade.reverse()
altura.reverse()

print 'Idades inverso: ', idade
print 'Alturas inverso: ', altura
    
