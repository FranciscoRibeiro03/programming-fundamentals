def intersects(a1, b1, a2, b2):
    assert a1 <= b1
    assert a2 <= b2

    return not (b1 <= a2 or b2 <= a1)

def main():
    print("Vamos usar intervalos da forma [a1, b1[ e [a2, b2[")
    a1 = float(input("a1? "))
    b1 = float(input("b1? "))
    a2 = float(input("a2? "))
    b2 = float(input("b2? "))
    if intersects(a1, b1, a2, b2):
        print("Estes intervalos intersetam-se.")
    else:
        print("Estes intervalos não se intersetam.")

main()