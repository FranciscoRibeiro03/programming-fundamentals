#ID: 

# Complete...

# Use esta instrução / Use this instruction:

"""

Rendimento        Taxa     Deducao
Até 10000         5%       0€
[10000, 20000[    10%      500€
20000+            15%      1500€

imposto = (taxa * rendimento) - deducao

Imposto: 1.25

"""




while True:
   rendimento = input("Rendimento? ")
   if rendimento == '': break

   rendimento = float(rendimento)
   if rendimento < 10000:
      t = 0.05
      d  = 0
   elif rendimento < 20000:
      t = 0.1
      d = 500
   else:
      t = 0.15
      d = 1500
   imposto = (t * rendimento) - d
   print("Imposto: {:.2f}".format(imposto))














"""
def taxaDeducao(rendimento):
   if rendimento > 20000:
      return [15, 1500]
   elif rendimento < 10000:
      return [5, 0]
   else:
      return [10, 500]

while True:
   info = input("Rendimento? ")    # Income?
   if not info:
      break
   
   rendimento = float(info)
   taxa, deducao = taxaDeducao(rendimento)
   
   imposto = ((taxa / 100) * rendimento) - deducao
   
   print("Imposto: {:.2f}".format(imposto))
"""