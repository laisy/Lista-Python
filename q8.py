n = int(raw_input()) + 1
lista = []
remane = []
dsk = []

for i in range(n):
    lista.append(i)

del lista[0]

for k in range(len(lista)):
        remane.append(lista[len(lista)-1-k])

cont = len(remane)

while cont > 1:
    dsk.append(remane[-1])
    del(remane [-1])
    remane.insert(0, remane[-1])
    del(remane [-1])
    cont -= 1


print "Cartas Descartadas: ",", ".join(map(str, dsk))
print "Carta remanescente:",", ".join(map(str, remane))
