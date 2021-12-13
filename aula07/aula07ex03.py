# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^50} : {:<}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^50} : {:<}".format(num, dic[num][0], dic[num][1]))

def addContact(dic):
    number = input("Introduz o número que queres adicionar: ")
    name = input("Introduz o nome correspondente ao número: ")
    address = input("Introduz a morada correspondente ao contacto: ")
    dic[number] = (name, address)
    print("Adicionado o contacto {} com o número {} e morada {}".format(name, number, address))

def removeContact(dic):
    number = input("Introduz o número que queres remover da lista: ")
    name = dic[number][0]
    dic.pop(number)
    print("Removido o contacto {}, associado ao número {}".format(name, number))

def searchNumber(dic):
    number = input("Introduz o número que queres procurar: ")
    if number in dic:
        print("O contacto associado ao número {} é {}.".format(number, dic[number][0]))
    else:
        print("Nenhum contacto associado ao número {}".format(number))

def filterPartName(contacts: dict, partName: str):
    """Returns a new dict with the contacts whose names contain partName."""
    newDict = {}
    for contact in contacts:
        name = contacts[contact][0]
        if partName in name:
            newDict[contact] = (name, contacts[contact][1])
    return newDict


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro", "Aveiro"),
        "387719992": ("Maria Matos", "Porto"),
        "887555987": ("Marta Maia", "Coimbra"),
        "876111333": ("Carlos Martins", "Lisboa"),
        "433162999": ("Ana Bacalhau", "Viseu")
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addContact(contactos)
        elif op == "R":
            removeContact(contactos)
        elif op == "N":
            searchNumber(contactos)
        elif op == "P":
            pesquisa = input("Introduz o nome que queres procurar: ")
            partDict = filterPartName(contactos, pesquisa)
            print("Contactos com \"{}\":".format(pesquisa))
            listContacts(partDict)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

