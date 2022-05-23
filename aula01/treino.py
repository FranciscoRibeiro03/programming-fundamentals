horaSaidaEmM = 6 * 60 + 52
horaSaida = f"{(horaSaidaEmM // 60):02d}:{(horaSaidaEmM % 60):02d}"

distPasso = 1
ritmoPasso = 10
tempoPasso = distPasso * ritmoPasso

distTreino = 3
ritmoTreino = 6
tempoTreino = distTreino * ritmoTreino

distVolta = distPasso + distTreino
tempoVolta = distVolta * ritmoPasso

tempoTotal = tempoPasso + tempoTreino + tempoVolta

horaFinalEmM = horaSaidaEmM + tempoTotal

horaFinal = f"{(horaFinalEmM // 60):02d}:{(horaFinalEmM % 60):02d}"

print(f'Se sair de casa às {horaSaida}, chego a casa às {horaFinal}')