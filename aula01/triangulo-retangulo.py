import math

catetoA = float(input('Introduz o comprimento do cateto A: '))
catetoB = float(input('Introduz o comprimento do cateto B: '))

hipotenusa = math.hypot(catetoA, catetoB)

print(f'Comprimento da Hipotenusa: {hipotenusa}')

angulo = math.degrees(math.acos(catetoA/hipotenusa))

print(f'O ângulo em graus entre o lado A e a hipotenusa é {angulo:.2f}')