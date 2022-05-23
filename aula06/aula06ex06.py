from fileinput import filename


def compareFiles(fileName1, fileName2):
    if fileName1 == fileName2: return True
    with open(fileName1, 'rb') as f1:
        with open(fileName2, 'rb') as f2:
            while True:
                f1Read = f1.read(1024)
                f2Read = f2.read(1024)
                if f1Read != f2Read:
                    return False
                if not f1Read:
                    return True
    
print(compareFiles("teste.txt", "teste copy.txt"))