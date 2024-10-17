# Autor: Jonathan Hernández
# Fecha: 17 octubre 2024
# Descripción: Calculadora Vectorial en Python Version 2.
# GitHub: https://github.com/Jona163

from cmath import acos, asin, cos, pi, sqrt, tan
import fractions
from re import U
import math
from unittest import result
from xml.etree.ElementTree import tostring
from numpy import arctan
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from fractions import Fraction                          
from decimal import Decimal


class ParOrdenado:
    def __init__(self,a,b):
        self.real = int(a)
        self.imaginario = int(b)

def graficarComp(lista, colores = ["r", "g", "b"]):
    x = [0]*len(lista)
    y = [0]*len(lista)
    u = []
    v = []
    for vector in lista:
      u.append(vector.real)
      v.append(vector.imaginario)
    
    izda = min(-1, min(u)-1)
    dcha = max(1, max(u)+1)
    abajo = min(-1, min(v)-1)
    arriba = max(1, max(v)+1)

    plt.quiver(x, y, u, v,  angles='xy', scale_units='xy', scale=1,
               color=colores)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlim([izda, dcha])
    plt.ylim([abajo, arriba])
    plt.xlabel('x')
    plt.ylabel('y')
    return plt.gca()


def switch(case, q, w, e, r):
    sw={
    }
    return sw.get(case,default())

def default():
    return "La opcion %s no existe en el menu"% case

repetir=True
while repetir:
    print("**************Graficadora de Vectores**************")
    print("1. Graficar 2D")
    print("2. Grafiar 3D")
    case=int(input("Selecciona una Opcion "))

    if case == 1:
        print("**************Graficadora de Vectores**************")
        print("1. Graficar por Coordenadas")
        print("2. Grafiar por Magnitud y angulo")
        print("3. Operaciones basicas de vectores")
        print("4. Ecuacionn de la recta")
        case2=int(input("Selecciona una Opcion ")) 

        if case2 == 1:
            v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 1 a 4: "))

            if v == 1:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                infovector=ParOrdenado(a,b)
                ax = graficarComp([infovector])
                ax.set_title("Vectores")
                plt.show()
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 2:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                infovector=ParOrdenado(a,b)
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                infovector2=ParOrdenado(a2,b2)
                ax = graficarComp([infovector, infovector2])
                ax.set_title("Vectores")
                plt.show()
                r=input(("\033[1;32m"+"Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(a+a2)
                    ry=(b+b2)
                    Result=math.sqrt(((rx*rx)+(ry*ry)))
                    angulo=(math.atan(ry/rx))*(180/pi)
                    if angulo>0:
                        ang=angulo+180
                    elif angulo<0:
                        ang=angulo-180
                    xr=Result*math.cos(ang)
                    yr=Result*math.sin(ang)
                    Vr=ParOrdenado(xr,yr)
                    ax = graficarComp([Vr])
                    ax.set_title("Vectores")
                    plt.show()
                else:
                    "OK :)"
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 3:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                infovector=ParOrdenado(a,b)
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                infovector2=ParOrdenado(a2,b2)
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                a3=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                b3=int(input())
                infovector3=ParOrdenado(a3,b3)
                ax = graficarComp([infovector,infovector2,infovector3])
                ax.set_title("Vectores")
                plt.show()
                r=input(("\033[1;32m"+"Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(a+a2+a3)
                    ry=(b+b2+b3)
                    Result=math.sqrt(((rx*rx)+(ry*ry)))
                    angulo=(math.atan(ry/rx))*(180/pi)
                    if angulo>0:
                        ang=angulo+180
                    elif angulo<0:
                        ang=angulo-180
                    xr=Result*math.cos(ang)
                    yr=Result*math.sin(ang)
                    Vr=ParOrdenado(xr,yr)
                    ax = graficarComp([Vr])
                    ax.set_title("Vectores")
                    plt.show()
               else:
                    "OK :)"
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 4:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                infovector=ParOrdenado(a,b)
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                infovector2=ParOrdenado(a2,b2)
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                a3=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                b3=int(input())
                infovector3=ParOrdenado(a3,b3)
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 4"
                a4=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 4")
                b4=int(input())
                infovector4=ParOrdenado(a4,b4)
                ax = graficarComp([infovector,infovector2,infovector3,infovector4])
                ax.set_title("Vectores")
                plt.show()
                r=input(("\033[1;32m"+"Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(a+a2+a3+a4)
                    ry=(b+b2+b3+b4)
                    Result=math.sqrt(((rx*rx)+(ry*ry)))
                    angulo=(math.atan(ry/rx))*(180/pi)
                    if angulo>0:
                        ang=angulo+180
                    elif angulo<0:
                        ang=angulo-180
                    xr=Result*math.cos(ang)
                    yr=Result*math.sin(ang)
                    Vr=ParOrdenado(xr,yr)
                    ax = graficarComp([Vr])
                    ax.set_title("Vectores")
                    plt.show()
                else:
                    "OK :)"
            rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
            if rep == "s" or rep == "S":
                repetir = True
            else:
                repetir=False
        elif case2 == 2:
            v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 1 a 4: "))

            if v == 1:
                print("\033[1;32m"+"Ingresa la magnitud del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa Ingresa el angulo del  vector : 1")
                b=int(input())
                x=(a*math.cos(b))
                y=(a*math.sin(b))
                infovector=ParOrdenado(x,y)
                ax = graficarComp([infovector])
                ax.set_title("Vectores")
                plt.show()
            elif v == 2:
                print("\033[1;32m"+"Ingresa la magnitud del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 1")
                b=int(input())
                x=(a*math.cos(b))
                y=(a*math.sin(b))
                infovector=ParOrdenado(x,y)
                print("\033[1;32m"+"Ingresa la magnitud del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 2")
                b2=int(input())
                x2=(a2*math.cos(b2))
                y2=(a2*math.sin(b2))
                infovector2=ParOrdenado(x2,y2)
                ax = graficarComp([infovector, infovector2])
                ax.set_title("Vectores")
                plt.show()
                r=input(("\033[1;32m"+"Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(x+x2)
                    ry=(y+y2)
