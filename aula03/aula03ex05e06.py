def max2(num1, num2):
    return num1 if num1 > num2 else num2

def max3(num1, num2, num3):
    max = max2(num1, num2)
    max = max2(max, num3)
    return max


def main():
    n1 = float(input("Introduz o primeiro número: "))
    n2 = float(input("Introduz o segundo número: "))
    n3 = float(input("Introduz o terceiro número: "))
    max = max3(n1, n2, n3)
    print(f"O maior número entre {n1} e {n2} e {n3} é {max}")

main()