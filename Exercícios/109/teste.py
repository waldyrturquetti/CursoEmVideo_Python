import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobra(valor, True)}')
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.aumentar(valor,10, False)}')
print(f'diminuindo 10% de {moeda.moeda(valor)} temos {moeda.diminuir(valor,10, True)}')
