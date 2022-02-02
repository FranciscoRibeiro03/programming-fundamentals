import os

def main():
    diretorio = "examples/"
    fileList = os.listdir(diretorio)
    size = len(max(fileList, key=len))
    string = "{:<" + str(size) + "} - {:<10}"
    print(string.format("Nome", "Tamanho"))
    for file in fileList:
        if diretorio[-1] != '/': diretorio += '/'
        tamanho = os.stat(diretorio + file).st_size
        print(string.format(file, tamanho))

main()