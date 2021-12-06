def main():
    count = 0
    total = 0
    while True:
        userInput = input("Introduz um número real: ")
        if (userInput == ""):
            break
        total += float(userInput)
        count += 1
    print(f"Números introduzidos: {count}")
    print(f"Média dos números introduzidos: {total/count}")

main()