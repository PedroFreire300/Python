qtd_convidados = int(input("Qual a quantidade convidados?"))

lista = []

for i in range(qtd_convidados):
    nomes = input(f"Nome do convidado {i}: " )

    lista.append(nomes)

print(lista)




