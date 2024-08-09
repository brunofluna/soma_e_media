#atividade 14
numeros = []
quant_notas = int(input('Informe a quantidade de notas: '))

while quant_notas >= 1:

    notas = int(input('Informe a nota: ')) 
    numeros.append(notas)
    quant_notas -=1 
print(numeros)
    
media = sum(numeros)/ len(numeros)
print(media)