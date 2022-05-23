# Alínea a)
def inputFloatList():
    list = []
    while True:
        userInput = input('Introduz um número: ')
        if (userInput == ''): break
        if (userInput.isnumeric()):
            list.append(float(userInput))
        else:
            print('Não introduziste um número!')
    return list

# Alínea b)
def countLower(lst, v):
    assert len(lst) > 0
    count = 0
    for i in range(len(lst)):
        if (lst[i] < v):
            count += 1
    return count

# Alínea c)
def minmax(lst):
    assert len(lst) > 0
    min = lst[0]
    max = lst[0]
    for i in range(len(lst)):
        elemento = lst[i]
        if max < elemento:
            max = elemento
        if min > elemento:
            min = elemento
    return min, max

# Alínea d)
def main():
    lista = inputFloatList()
    min, max = minmax(lista)
    media = ( min + max ) / 2
    lower = countLower(lista, media)
    print(f"\n Min: {min}")
    print(f" Max: {max}")
    print(f" Valores abaixo da média ({media}): {lower}\n")

main()