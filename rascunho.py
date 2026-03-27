produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [[10000, 2500],[5000, 40],[7000, 1200],[20000, 1500],[5800, 1300],[7200, 2500],[200, 800], [3300, 700],[1900, 400]]

for nome,i in zip(produtos,produtos_ecommerce):
    valor = i[0] * i[1]
    print(f"O total de {nome}(s) vendidos foi de {valor}")




             




