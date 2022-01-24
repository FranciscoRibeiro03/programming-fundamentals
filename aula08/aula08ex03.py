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

"""

    startTime = datetime.now().timestamp()
    prime = [True for i in range(n + 1)]
    p = 2
    while (p**2 <= n):
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    primeList = set()
    for p in range(n + 1):
        if prime[p]:
            primeList.add(p)
    endTime = datetime.now().timestamp()
    time = endTime - startTime
    return primeList, time
"""

def main():
    list, time = primesUpTo(1000000)
    print(list)
    print('Quantidade de números primos: ', len(list))
    print('Tempo demorado a processar: ', time)

main()