# Solução para o ep1: exame prático de FP de 2018-01-12, sessão das 14:00.
# 
# Há múltiplas soluções válidas.  Esta é apenas uma possibilidade.
# Outras soluções diferem sobretudo pela forma de guardar os dados do problema.
#
# JMR@ua.pt 2018

# (a) Carrega dados a partir do ficheiro de veículos.
# Acrescenta os dados lidos a duas estruturas de dados:
#   vehicles - que tem os registos de (marca, nif) indexados por matrícula;
#   clients  - que tem as listas de matrículas indexadas por cliente.
# O dicionário vehicles é útil para as alíneas (b) e (g).
# clients permite implementar (c) e (g) de forma eficiente,
# sem ter de percorrer todos os veículos.
def loadClients(fname, vehicles, clients):
    f = open(fname, 'r')
    for l in f:
        (plate, brand, nif) = l.rstrip().split(';')
        vehicles[plate] = (brand, nif)
        if nif not in clients:
            clients[nif] = []
        clients[nif].append(plate)
    f.close()
    print('Foram importados {} registos'.format(len(vehicles)))
    return

# (b)
def printVehicles(vehicles):
    # Ordenar pelo cliente (nif) e pela matrícula:
    # (Ordenamos apenas uma lista das chaves do dicionário.)
    plates = sorted(vehicles.keys(), key = lambda p : (vehicles[p][1], p))
    for plate in plates:
        (brand, nif) = vehicles[plate]
        print(nif, ':', (plate, brand))
            # (O tuplo é impresso no formato desejado.)

# (c)
def printClientPlates(clients):
    for nif in clients:
        print(nif, ':', clients[nif])

# (d)
def validPlate(s):
    return len(s) == 8 \
            and s[0:2].isdigit() \
            and s[2] == '-' \
            and s[3:5].isalpha() \
            and s[5] == '-' \
            and s[6:8].isdigit()

# (e) Registar um novo acesso ao parque.
def newAccess(accesses):
    p = inputPlate('Matricula? ')
    d = inputPositive('Duracao? ')
    accesses.setdefault(p, []).append(d)
        # método setdefault é outra forma de forçar o preenchimento do
        # item de chave p com uma lista vazia, se não existir ainda.

# (e)
def inputPlate(msg):
    while True:
        m = input(msg)
        if validPlate(m): break
        print('Inválida!', end=' ')
    return m

# (e)
def inputPositive(msg):
    # input and return a positive int
    while True:
        v = int(input(msg))
        if v > 0: break
        print('Inválida!', end=' ')
    return v

# (f) Gravar acessos ao parque.
def savePark(fname, accesses):
    f = open(fname, 'w')
    # Criar lista a partir dos acessos:
    # (Usámos uma list comprehension.  Poderia ser feito de outra forma.)
    lst = [ (p, d) for p in accesses.keys() for d in accesses[p] ]
    # Ordenar:
    lst = sorted(lst, key=lambda t: t[1], reverse=True)
    # Percorrer e gravar no ficheiro:
    for (plate, dur) in lst:
        f.write('{};{}\n'.format(plate,dur))
    f.close()
    print('Ficheiro gravado com sucesso!')

# (g) Fatura para um cliente
def invoice(clients, vehicles, accesses, n):
    print('Fatura NIF: {}'.format(n))
    plates = clients[n]     # matrículas deste cliente
    print('{:10} {:16} {:>8} {:>8}'.format( \
            'Matricula', 'Marca', 'Duracao', 'Custo'))
    total = 0.0
    for plate in plates:    # percorrer cada matrícula
        brand = vehicles[plate][0]
        lstacc = accesses.get(plate, [])   # lista de acessos desta matrícula
        for dur in lstacc:
            cost = dur * 0.01
            total += cost
            print('{:10} {:16} {:>8} {:>8.2f}'.format( \
                    plate, brand, dur, cost))
    # Lazy way to align: use same format string with some empty strings...
    print('{:10} {:16} {:>8} {:>8.2f}'.format('Total:', '', '', total)) 

def menu():
    print('Opções disponíveis:')
    print('0 - Terminar')
    print('1 - Ler ficheiro de clientes')
    print('2 - Imprimir clientes ordenados')
    print('3 - Mostrar matriculas por cliente')
    print('4 - Adicionar acesso ao parque')
    print('5 - Gravar acessos ao parque')
    print('6 - Gerar fatura para um cliente')
    op = input('Opcao? ')
    return op

# (h)
def main():
    vehicles = {}   # veiculos: {plate: (brand, nif)}
    clients = {}    # veiculos por cliente: {nif: [plate, ...], ...}
    accesses = {}   # acessos ao parque: {plate: [duration, ...], ...}

    while True:
        op = menu()

        if op == '0':
            break;
            
        elif op == '1': # (a)
            s = input('Nome do ficheiro? ')
            loadClients(s, vehicles, clients)
            
        elif op == '2': # (b)
            printVehicles(vehicles)

        elif op == '3': # (c)
            if len(clients) > 0:
                printClientPlates(clients)
            else:
                print('Não existem clientes!')

        elif op == '4': # (e)
            newAccess(accesses)
            
        elif op == '5': # (f)
            if len(accesses) > 0:
                savePark('parque.csv', accesses)
            else:
                print('Não existem entradas no Parque!')
        
        elif op == '6': # (g)
            nif = input('NIF? ')
            invoice(clients, vehicles, accesses, nif)

        else:
            print('Opção inválida')  # Não era pedido...

    print('Obrigado por usar software desenvolvido em FP!')
    return

########

if __name__ == '__main__':
    main()

