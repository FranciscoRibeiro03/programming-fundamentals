def shorten(string):
    shortString = ""
    for i in string:
        if i.isupper():
            shortString += i
    return shortString
    
def main():
    userInput = input("Introduz uma string: ")
    print(f"Abreviado: {shorten(userInput)}")

main()