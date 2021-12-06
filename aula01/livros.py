pf = 20
pc = 24.95
imp = 0.23
spa = 0.2

lucroPorLivro = ( (pc - spa) / (1 + imp) ) - pf
impostoPorLivro = imp * pc

exemplares = int(input('Quantos livros foram vendidos? '))

lucroTotal = lucroPorLivro * exemplares
taxasTotal = spa * exemplares
impostoTotal = impostoPorLivro * exemplares

print(f'Para uma tiragem de {exemplares:.0f} livros, a livraria teve um lucro de {lucroTotal:.2f}€, foram coletados {impostoTotal:.2f}€ em impostos e foram reunidos {taxasTotal:.2f}€ em taxas.')