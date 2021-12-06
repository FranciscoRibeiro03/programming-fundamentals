moradores = 4
vezesPorDia = 2 * moradores
alturaEmM = 3

distanciaAnoEmM = alturaEmM * vezesPorDia * 365
distanciaAnoEmKm = distanciaAnoEmM / 1000

tempoEmSegundos = distanciaAnoEmM

# Início Exercício tempo.py
s = tempoEmSegundos % 60
m = tempoEmSegundos // 60 % 60
h = tempoEmSegundos // 60 // 60 % 60

tempoFormatado = "{:02d} horas, {:02d} minutos e {:02d} segundos".format(h, m, s)
# Fim Exercício tempo.py


print(f'O elevador percorre {distanciaAnoEmKm} km por ano e está em funcionamento durante {tempoFormatado}.')