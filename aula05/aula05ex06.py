def countDigits(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count
    
def main():
    userInput = input("Introduz uma string: ")
    print(f"Nessa string há {countDigits(userInput)} números.")

main()