import math

def FormulaCuadratica(a, b, c):
	x1: float = 0
	x2: float = 0
	try:
		x1 = (-b + math.sqrt(math.pow(b, 2) - (4*a*c)))/2*a
		x2 = a*x1*2 + b*x1 + c
	except Exception as e:
		print(e)
	print(f"Los dos posibles valores de X son: {x1} y {x2}")

FormulaCuadratica(1, 8, 12)