def mdc(a, b):
    r = a % b
    return b if r == 0 else mdc(b, r)

def main():
    a = int(input("Introduz um número a: "))
    b = int(input("Introduz um número b: "))
    print(f"Máximo Divisor Comum: {mdc(a,b)}")

main()