def lerFicheiro(nome):
    newDict = {}
    count = 0
    with open(nome) as f:
        for line in f:
            line = line.rstrip()
            matricula, marca, nif = line.split(';')
            newDict[matricula] = (marca, nif)
            count += 1
    print("Foram importados {} registos.".format())
    return newDict

def main():
    ...

main()