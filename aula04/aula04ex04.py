def factorial(n):
   assert isinstance(n, int), "n should be an int"
   assert n >= 0            , "n should not be negative"
   # Complete aqui
   if n == 0: return 1
   for i in range(1, n):
      n *= i
   return n