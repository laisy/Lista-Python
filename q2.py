k = 0
num = []
par = []
impar = []

for k in range(20):
    numero = int(raw_input('Digite um numero:'))
    num.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print 'Numeros: ', num
print 'Pares: ', par
print 'Impares: ', impar 
