def countdownIf(n):
    assert n >= 0
    print(n)
    if n < 1:
        return print("Stop")
    countdownIf(n - 1)

def countdownWhile(n):
    assert n >= 0
    while n >= 0:
        print(n)
        n -= 1

def main():
    countdownWhile(5)

main()