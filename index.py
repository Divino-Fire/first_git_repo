from Math import sqrt

def quad(a, b, c):
	return [(-b + sqrt(b**2 - 4*a*c))/(2*a), -b - sqrt(b**2 - 4*a*c))/(2*a)]
