# Example program developed in TP class.
# jmr@ua.pt 2018

altura = float(input("Altura (m)? " ))
peso = float(input("Peso (kg)? "))

imc = peso / altura**2

print("IMC:", imc, "kg/m²")   # show result

