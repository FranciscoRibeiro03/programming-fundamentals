from datetime import datetime

def primesUpTo(n):
    startTime = datetime.now().timestamp()
    primeList = set(range(2, n+1))
    for i in range(2, n+1):
        for j in range(2, n+1):
            primeList.discard(i*j)
    endTime = datetime.now().timestamp()
    time = endTime - startTime
    return primeList, time

def main():
    list, time = primesUpTo(1000000)
    print(list)
    print('Quantidade de números primos: ', len(list))
    print('Tempo demorado a processar: ', time)

main()