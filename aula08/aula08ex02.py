def getNomes():
    nomes = []
    with open('names.txt') as f:
        for line in f:
            line = line.strip('\n')
            if (line != 'Nome'):
                nomes.append(line)
    return nomes

def main():
    listaNomes = getNomes()
    dict = {}
    for nome in listaNomes:
        nomes = nome.split()
        if nomes[-1] in dict:
            dict[nomes[-1]].add(nomes[0])
        else:
            dict[nomes[-1]] = {nomes[0]}

    print('{:15} : {}'.format('Apelido', 'Nomes'))
    for apelido in dict:
        print('{:15} : {}'.format(apelido, dict[apelido]))


main()