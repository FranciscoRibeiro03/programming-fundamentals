def getDivisores(n):
    divisores = []
    for i in range(1, n+1):
        if n == i: continue
        if n % i == 0: divisores.append(i)
    return divisores

def getClass(n):
    somaDiv = 0
    for i in getDivisores(n):
        somaDiv += i
    if somaDiv < n:
        return "Deficiente"
    elif somaDiv == n:
        return "Perfeito"
    else:
        return "Abundante"

def main():
    for i in range(1, 101):
        print("{:3d} - Número {:10s} - Divisores: {}".format(i, getClass(i), getDivisores(i)))

main()