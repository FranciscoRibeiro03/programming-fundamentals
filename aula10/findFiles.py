import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)
    return


def findFiles(path, ext):
    # Complete...
    lst = []
    filesList = os.listdir(path)
    for fname in filesList:
        newPath = os.path.join(path, fname)
        if os.path.isfile(newPath):
            if newPath.endswith(ext):
                lst.append(newPath)
        elif os.path.isdir(newPath):
            lst += findFiles(newPath, ext)
    return lst


def main():
    print("Testing printDirFiles('..'):")
    printDirFiles("..")

    print("\nTesting findFiles('.', '.py'):")
    lst = findFiles(".", ".py")
    print('\n'.join(lst))
    assert isinstance(lst, list)

    print("\nTesting findFiles('..', '.csv'):")
    lst = findFiles("..", ".csv")
    print('\n'.join(lst))

if __name__ == "__main__":
    main()

