

"""
    startTime = datetime.now().timestamp()
    primeList = set(range(2, n+1))
    for i in range(2, n+1):
        for j in range(2, n+1):
            primeList.discard(i*j)
    endTime = datetime.now().timestamp()
    time = endTime - startTime
    return primeList, time

"""





import math


def primesUpTo(n):
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
    return primeList

def primesUpTo2(n):
    A = {}
    for i in range(2, n+1):
        A[i] = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i]:
            j = i**2
            while j < n:
                print(j)
                A[j] = False
                j += i
    
    primeList = []

    for i in A:
        if A[i]:
            primeList.append(i)
    return primeList

def main():
    list = primesUpTo2(1000)
    print(list)
    print('Quantidade de números primos: ', len(list))

main()