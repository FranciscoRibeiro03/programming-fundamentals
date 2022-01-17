def calcMedian(lst):
    orderedList = sorted(lst)
    orderedListLen = len(orderedList)
    lenDivByTwo = orderedListLen//2 - 1
    if orderedListLen % 2 == 1:
       return orderedList[lenDivByTwo+1]
    else:
       return ( orderedList[lenDivByTwo] + orderedList[lenDivByTwo+1] ) / 2
    
def main():
    lists = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
        ([6, 4, 7, 1, 7, 0, 5, 2, 7, 8], 5.5),
        ([7, 4, 8, 2, 7], 7),
        ([8, 4, 2, 4, 6], 4),
        ([8, 4, 2, 4, 6, 7], 5.0),
        ([1, 2], 1.5),
        ([1], 1),
        ([7, 3, 6, 2, 4], 4)
    ]

    print("{:>5}   {:^8}    {:<5}".format("Teste", "Esperado", "Atual"))
    for list in lists:
        median = calcMedian(list[0])
        passTest = "Pass" if list[1] == median else "Fail"
        print("{:>5} - {:>8} == {:<5}".format(passTest, list[1], median))

main()