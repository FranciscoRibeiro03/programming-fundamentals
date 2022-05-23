l = float(input('Quantos litros foram abastecidos? '))

preco = l * 1.4

if (l > 40):
    preco = preco * 0.9

print(f'Preço a pagar por {l} litros de combustível: {preco}€')