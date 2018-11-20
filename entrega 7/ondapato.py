# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:28:56 2018

@author: Benjamín Castro Pohl
"""
from numpy import *
#seccion1
N=1000
L=150000
B=100
S=0.001
n=0.045
ss=0
Co=1.485
NC=1 #puede ser un numero menor a 1 tambien 
tfin=600
tfin=tfin*600
g=32.3

dx=L/(N-1)

def promedio(valores):
	sumaParcial=0
	for valor in valores:
		sumaParcial+=valor
	cantidadValores = len(valores)
	return sumaParcial/float(cantidadValores)


def ycritical(units, z, b, Q):
    yc = 1.0                       # Altura inicial para proceso iterativo
     # Condición del sistema de unidades (SI o SB)
    if units == "SI":
        g  = 9.81                  # [SI=> 9.81 m*s^-2] Gravedad nominal terrestre
    else:
        g  = 32.2                  # [SB=> 32.2 pie*s^-2] Gravedad nominal terrestre
    # Función de aproximación:
    def D(y):                      # Definición de función argumento NR
        global A, P
        # Parámetros de calculo:
        k   = Q**2./g              # [m^5 o pie^5] Constante del modelo 
        A   = y*(b + z*y)          # [m^2 o pie^2] Área mojada
        T   = b + 2.*z*y           # [m o pie] Ancho superficial (dA/dy)
        dT  = 2.*z                 # Derivada total de T respecto a y (dT/dy)  
        # Función objetivo y su primera derivada total
        f   = A**3. - k*T          # Función objetivo f(y) = 0
        df  = 3.*A**2.*T - k*dT    # Derivada total  df(y)/dy
        return f/df                # Segundo termino de formula de NR
    # Proceso de aproximaciones sucesivas
    tol = abs(D(yc))               # Tolerancia iteración 1
    while tol > 1e-6:
        yc1 = yc - D(yc)           # Formula de NR
        tol = abs(yc1-yc)          # Tolerancia del paso
        yc  = yc1                  # Mutación de y
    return yc                      # [m o pie] altura critica


def ynormal(units, n, S, z, b, Q):
    yn = ycritical(units, z, b, Q)         # Altura inicial para proceso iterativo
    # Condición del sistema de unidades:
    if units == 'SI':
        C_0  = 1.00                        # Factor de conversión unidades (SI)
    else:
        C_0  = 1.49                        # Factor de conversión unidades (SB)
    # Función de aproximación:
    def D(y):                              # Definición de función argumento NR
        global A, P
        # Parámetros de calculo:
        k   = (Q*n/(C_0*S**0.5))**3.       # [m^8 o pie^8] Constante del modelo hidráulico 
        A   = y*(b + z*y)                  # [m^2 o pie^2] Área mojada
        P   = b + 2.*y*(z**2.+1.)**0.5     # [m o pie] Perímetro mojado
        T   = b + 2.*z*y                   # [m o pie] Ancho superficial (dA/dy)
        dP  = 2.*(z**2.+1.)**0.5           # Derivada total de P respecto a y (dP/dy)  
        # Función objetivo y su derivada total
        f   = A**5. - k*P**2.              # Función objetivo f(y)=0
        df  = 5.*A**4.*T - 2.*k*P*dP       # Derivada total df(y)/dy
        return f/df                        # Segundo termino de ecuación de NR
    # Proceso de aproximaciones sucesivas:
    tol = abs( D(yn) )                     # Tolerancia iteración 1
    while tol > 1e-6:
        yn1 = yn - D(yn)                   # Ecuación de NR
        tol = abs(yn1 - yn)                # Tolerancia del paso
        yn  = yn1                          # Mutación de y
    return yn                              # [m o pie] altura normal del canal
A = yn*(b+ss*yn)

x = linspace(0, L, N)
#por si dx no es cte
#for i in range(1,N+1)
    
#   x(i)=(i-1)*dx
   
#FALTA DEFINIR CONDICIONES INICIALES
   
   
t=0
k=0
while t<Tfin:
    k+=1
    dt=NC*dx/promedio(V(k,1:N))
