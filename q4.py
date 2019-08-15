k = 0
i = 0
vetor1 = []
vetor2 = []
vetorUni = []
vetorInt = []

n1 = int(raw_input('Digite a quantidade de elementos do vetor1: '))
n2 = int(raw_input('Digite a quantidade de elementos do vetor2: '))

for k in range(n1):
    num1 = int(raw_input('Digite os elementos do vetor1: '))
    vetor1.append(num1)
    vetorUni.append(num1)

for k in range(n2):
    num2 = int(raw_input('Digite os elementos do vetor2: '))
    vetor2.append(num2)
    vetorUni.append(num2)

for k in range(len(vetor1)):
    for i in range(len(vetor2)):
        if vetor1[k] == vetor2[i]:
            vetorInt.append(vetor1[k])

if len(vetor1) == 0 or len(vetor2) == 0:
    print 'Vazio'
else:
    print 'Vetor1: ', vetor1
    print 'Vetor2: ', vetor2
    print 'Vetor uniao: ', vetorUni
    print 'Vetor Interccao: ', vetorInt
