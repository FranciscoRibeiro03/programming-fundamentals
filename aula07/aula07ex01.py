from sys import argv


def getDict():
    lettersDict = {}
    with open(argv[1], encoding="utf-8") as file:
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
    assert len(argv) > 1, "Need at least one argument"
    letras = getDict()
    for key, value in sorted(letras.items()):
        print("{} - {}".format(key, value))

main()