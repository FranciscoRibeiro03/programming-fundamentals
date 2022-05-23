"""
Pretendemos um método que inverta a ordem dos dígitos de um número inteiro.
Por exemplo `reverseDigits(1234)` deve devolver `4321`.

Deve fazê-lo através da função _recursiva_ auxiliar `reverseAux`.
Eis um exemplo do cálculo:

    reverseAux(1234, 0)
    = reverseAux(123, 4)
    = reverseAux(12, 43)
    = reverseAux(1, 432)
    = reverseAux(0, 4321)
    = 4321

Não pode usar strings nem ciclos.
Note que `1234%10 = 4` e `1234//10 = 123`.
"""
def reverseDigits(value):
   return reverseAux(value, 0)

def reverseAux(partValue, partReversed):
   if partValue == 0:
      return partReversed
   return reverseAux(partValue//10, partReversed*10+partValue%10)

def main():
    print( reverseDigits(1234) )    # 4321
    print( reverseDigits(345) )     # 543
    print( reverseDigits(9) )       # 9
    print( reverseDigits(1245689) ) # 9865421

main()