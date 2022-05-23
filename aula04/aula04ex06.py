def leibnizPi4(n):
    rangeN = range(n)
    total = 0
    for i in rangeN:
        num = (-1)**i
        den = 2*i + 1
        total += (num/den)

    return total

def main():
    for i in range(10):
        print("{} - {}".format(10**i, leibnizPi4(10**i)*4))

main()