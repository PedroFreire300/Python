produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

produtos_ecommerce = [
    [10000, 2500],
    [5000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

# Pegando quantidade e preço do livro
quantidade = produtos_ecommerce[1][0]
preco_antigo = produtos_ecommerce[1][1]

valor_antigo = quantidade * preco_antigo
print(f"Valor antigo: R${valor_antigo:.2f}")

# Aplicando aumento de 10%
preco_novo = preco_antigo * 1.10
produtos_ecommerce[1][1] = preco_novo

valor_novo = quantidade * preco_novo
print(f"Valor novo: R${valor_novo:.2f}")

diferenca = valor_novo - valor_antigo
print(f"O livro sofreu um aumento de R${diferenca:.2f}")