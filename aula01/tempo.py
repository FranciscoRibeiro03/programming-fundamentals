tempoEmSegundos = int(input('Introduz um valor em segundos: '))

s = tempoEmSegundos % 60
m = tempoEmSegundos // 60 % 60
h = tempoEmSegundos // 60 // 60 % 60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))