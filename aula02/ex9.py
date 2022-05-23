ctp = float(input('Introduz a tua nota da CTP: '))
cp = float(input('Introduz a tua nota da CP: '))

if ctp < 6.5 or cp < 6.5:
    print('Nota final: 66')
    exit(1)

notaFinal = ctp * 0.36 + cp * 0.64

if notaFinal < 10:
    atpr = float(input('Introduz a tua nota de ATPR: '))
    apr = float(input('Introduz a tua nota de APR: '))

    tp = max(ctp, atpr)
    p = max(cp, apr)

    if (tp < 6.5 or p < 6.5):
        print('Nota final: 66')
        exit(1)

    notaFinal = tp * 0.36 + p * 0.64

print(f'Nota final: {notaFinal}')