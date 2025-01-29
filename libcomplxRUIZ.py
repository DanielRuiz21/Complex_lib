#SUMA

def sumacomplx(a,b):
    rta = (a[0]+b[0],a[1]+b[1])
    return rta

#RESTA

def restcomplx(a,b):
    rta = (a[0]-b[0],a[1]-b[1])
    return rta

#Multiplicacion
# #(a1 + b1i) × (a2 + b2i) = ((a1a2) − (b1b2)) + ((a1b2) + (a2b1))i

def multcplx(a,b):
    rtamult = (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    return rtamult

#CONJUGADO

def conjugcomplx(a):
    rtacon = (a[0],-a[1])
    return rtacon


#DIVISION_a/b

def divcplx(a,b):
    numerador = (multcplx(a,conjugcomplx(b)))
    denominador = b[0]**2 + b[1]**2
    rtadiv=(numerador[0]/denominador, numerador[1]/denominador)
    return(rtadiv)

#MODULO

def modulocomplx(a):
    rta = (a[0]**2 + a[1]**2)**(1/2)
    return rta



import math

#POLAR_CARTESIANO

def polcar(c):
    a = round(c[0]*math.cos(c[1]),2)
    b = round(c[0]*math.sin(c[1]),2)
    rta = (a,b)
    return rta


#CARTESIANO_POLAR

def carpol(c):
    r = round(modulocomplx(c),2)
    b = round(math.atan(c[1]/c[0]),2)
    rta = (r,b)
    return rta


#FASE

def fasecomplx(c):
    rta = round(math.atan(c[1]/c[0]),2)
    return rta




