def getDict():
    lettersDict = {}
    with open('pg3333.txt', encoding="utf-8") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char not in lettersDict:
                        lettersDict[char] = 1
                    else:
                        lettersDict[char] += 1
    return lettersDict

def main():
    letras = getDict()
    for key, value in sorted(letras.items()):
        print("{} - {}".format(key, value))

main()