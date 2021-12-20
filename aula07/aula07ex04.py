def gerarJogos(listaEquipas):
   assert len(listaEquipas) >= 2, "Requires two or more teams!"
   lista = []
   for eq1 in listaEquipas:
      for eq2 in listaEquipas:
         if eq1 == eq2:
            continue
         lista.append((eq1, eq2))
   return lista

def main():
    print("Introduz os nomes das equipas, uma de cada vez, e carrega no Enter quando terminares.")
    listaEquipas = []
    while True:
        equipasInput = input("Introduz o nome de uma equipa: ")
        if equipasInput == '':
            break
        listaEquipas.append(equipasInput.strip())
    listaJogos = gerarJogos(listaEquipas)
    print(listaJogos)

main()