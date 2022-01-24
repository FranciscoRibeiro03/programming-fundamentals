from datetime import datetime

def primesUpTo(n):
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

def main():
    # Testing:
    s, time = primesUpTo(1000)
    print(s)
    print('Quantidade de números primos: ', len(s))
    print('Tempo demorado a processar: ', time)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

