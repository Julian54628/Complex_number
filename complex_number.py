import math
def complex_sum(a,b):
    return (a[0]+b[0],a[1]+b[1])


def complex_multiplication(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def complex_division(a,b):
    return((a[0]*b[0]+a[1]*b[1])/(b[0]**2 * b[1]**2),
           (b[0]*a[1]-a[0]*b[1])/(b[0]**2 * b[1]**2))

def complex_rest(a,b):
    return (a[0]-b[0],a[1]-b[1])

def complex_module(a,b):
    return math.sqrt(a**2 + b**2)

def complex_conjugated(a,b):
    return (a,-b)

def Cartesian_to_polar(a,b):
    p = complex_module(a,b)
    tetta = math.atan(b/a)
    return (p,tetta)

def polar_to_Cartesian(a,b):
    return (a*math.cos(b),a*math.sin(b))

def fase(a,b):
    return math.atan(b/a)
