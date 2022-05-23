import math

def findZero(func, a, b, tol):
	if func(a) * func(b) > 0:
		print("Não existe uma raíz real no intervalo especificado!")
		return None
		
	while abs(b - a) > tol:
		mid = (a + b) / 2
		funcMid = func(mid)
		if funcMid == 0:
			return mid
		if func(a) * funcMid < 0:
			b = mid
		else:
			a = mid
	return (a + b) / 2

def main():
	funct = lambda x: x + math.sin(10 * x)
	print(findZero(funct, 0.2, 0.4, 0.001))

if __name__ == "__main__":
    main()