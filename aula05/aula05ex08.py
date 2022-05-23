def ispalindrome(string):
    return True if string == string[::-1] else False
    
def main():
    userInput = input("Introduz uma string: ")
    print(f"Essa string {'é' if ispalindrome(userInput) else 'não é'} um palíndromo.")

main()