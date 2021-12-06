def Fibonacci(n):
    f0 = 0
    f1 = 1
    if n == 0: return 0
    for i in range(n-1):
        if i % 2 == 0:
            f0 += f1
        else:
            f1 += f0
    return max(f0, f1)

def FibRecursive(n):
    if n == 0: return 0
    if n == 1: return 1
    return FibRecursive(n-1) + FibRecursive(n-2)

def main():
    for i in range(15):
        print("{} - {} - {}".format(i, Fibonacci(i), FibRecursive(i)))

main()