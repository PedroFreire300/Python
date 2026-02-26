meta = 10000
vendas = [ ['João', 15000], ['Julia', 27000], ['Marcus', 9900], ['Maria', 3750], ['Ana', 10300],['Alon', 7870], ]
#seu código aqui

qtd_vendedores = 0

for vendedores in vendas :
    if vendedores[1]>meta:
        
        qtd_vendedores += 1

print(qtd_vendedores)