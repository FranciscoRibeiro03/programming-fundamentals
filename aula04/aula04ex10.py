def isPrime(n):
    for i in range(2, n+1):
        if n == i: continue
        if n % i == 0: return False
    return True

def main():
    for i in range(1, 101):
        print("isPrime({:3d})? {}".format(i, isPrime(i)))

main()