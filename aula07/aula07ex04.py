def main():
    print("Introduz os nomes das equipas, uma de cada vez, e carrega no Enter quando terminares.")
    listaEquipas = []
    while True:
        equipasInput = input("Introduz o nome de uma equipa: ")
        if equipasInput == '':
            break
        listaEquipas.append(equipasInput.strip())
    print(listaEquipas)

main()