qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while(valor > 0.0):
    soma += valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input("Digite um valor: "))

#caso divite um valor negativo o laço encerra
media = soma / qtd
print("\n Total da soma: ", soma)
print("\n Quantidades de valores digitados: ", qtd)
print("\n Média dos Valore: ", media)