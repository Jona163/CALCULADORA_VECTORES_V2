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
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 4")
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
                print("\033[1;32m"+"Ingresa la magnitud del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 1")
                b=int(input())
                x=(a*math.cos(b))
                y=(a*math.sin(b))
                infovector=ParOrdenado(x,y)
                print("\033[1;32m"+"Ingresa Ingresa la magnitud del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 2")
                b2=int(input())
                x2=(a2*math.cos(b2))
                y2=(a2*math.sin(b2))
                infovector2=ParOrdenado(x2,y2)
                print("\033[1;32m"+"Ingresa la magnitud del vector : 3")
                a3=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 3")
                b3=int(input())
                x3=(a*math.cos(b3))
                y3=(a*math.sin(b3))
                infovector3=ParOrdenado(x3,y3)
                ax = graficarComp([infovector,infovector2,infovector3])
                ax.set_title("Vectores")
                plt.show()
                r=input(("\033[1;32m"+"Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(x+x2+x3)
                    ry=(y+y2+y3)
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
                    #Hasta aqui github de hoy  17
                else:
                    "OK :)"
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]: ")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 4:
                print("\033[1;32m"+"Ingresa la magnitud : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 1")
                b=int(input())
                x=(a*math.cos(b))
                y=(a*math.sin(b))
                infovector=ParOrdenado(x,y)
                print("\033[1;32m"+"Ingresa la magnitud en el eje x del vector : 2")
                a=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 2")
                b=int(input())
                x2=(a*math.cos(b))
                y2=(a*math.sin(b))
                infovector2=ParOrdenado(x2,y2)
                print("\033[1;32m"+"Ingresa la magnitud del vector : 3")
                a=int(input())
                print("Ingresa el angulo del  vector : 3")
                b=int(input())
                x3=(a*math.cos(b))
                y3=(a*math.sin(b))
                infovector3=ParOrdenado(x3,y3)
                print("\033[1;32m"+"Ingresa la magnitud del vector : 4")
                a=int(input())
                print("\033[1;32m"+"Ingresa el angulo del  vector : 4")
                b=int(input())
                x4=(a*math.cos(b))
                y4=(a*math.sin(b))
                infovector4=ParOrdenado(x4,y4)
                ax = graficarComp([infovector,infovector2,infovector3,infovector4])
                ax.set_title("Vectores")
                plt.show()
                r=input(("\033[1;32m"+"Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(x+x2+x3+x4)
                    ry=(y+y2+y3+y4)
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
        elif case2 == 3:
            print("**************Graficadora de Vectores**************")
            print("1.Suma")
            print("2.Resta")
            print("3.Producto punto")
            print("4.Producto cruz")
            case3=int(input("Selecciona una opccion: "))

            if case3 == 1:
                v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 2 a 4: "))

                if v == 2:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    v=[]
                    x=a+a2
                    y=b+b2
                    V=[x,y]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    if r == 1:
                        Vr=ParOrdenado(x,y)
                        ax = graficarComp([Vr])
                        ax.set_title("Vectores")
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
                elif v == 3:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    x=a+a2+a3
                    y=b+b2+b3
                    V=[x,y]
                    print("Su vector resultante es: ", V)
                    if r == 1:
                        Vr=ParOrdenado(x,y)
                        ax = graficarComp([Vr])
                        ax.set_title("Vectores")
                        plt.show()
                    else:
                        print("BYE :)")
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
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a4=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b4=int(input())
                    x=a+a2+a3+a4
                    y=b+b2+b3+b4
                    V=[x,y]
                    print("Su vector resultante es: ", V)
                    if r == 1:
                        Vr=ParOrdenado(x,y)
                        ax = graficarComp([Vr])
                        ax.set_title("Vectores")
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
            elif case3 == 2:
                v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 2 a 4: "))

                if v == 2:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    v=[]
                    x=a-a2
                    y=b-b2
                    V=[x,y]
                    print("Su vector resultante es: ", V)
                    if r == 1:
                        Vr=ParOrdenado(x,y)
                        ax = graficarComp([Vr])
                        ax.set_title("Vectores")
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
                elif v == 3:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    x=a-a2-a3
                    y=b-b2-b3
                    V=[x,y]
                    print("Su vector resultante es: ", V)
                    if r == 1:
                        Vr=ParOrdenado(x,y)
                        ax = graficarComp([Vr])
                        ax.set_title("Vectores")
                        plt.show()
                    else:
                        print("BYE :)")
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
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a4=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b4=int(input())
                    x=a-a2-a3-a4
                    y=b-b2-b3-b4
                    V=[x,y]
                    print("Su vector resultante es: ", V)
                    if r == 1:
                        Vr=ParOrdenado(x,y)
                        ax = graficarComp([Vr])
                        ax.set_title("Vectores")
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
            elif case3 == 3:
                print("\033[1;32m"+"Como vas a calcular")
                print("\033[1;32m"+"1. Por componentes")
                print("\033[1;32m"+"2. Por magnitudes y angulos")
                n=int(input())
                if n == 1:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    infovector=ParOrdenado(a,b)
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    mag1 = sqrt((a*a)+(b*b))
                    mag2 = sqrt((a2*a2)+(b2*b2))
                    magr = (mag1*mag2)
                    r = (a*a2) + (b*b2)
                    te = acos((r)/(magr))
                    t=te.real
                    tt=math.degrees(t)
                    print("\033[1;32m"+"Teta : ",tt)
                    pr = (magr)*(cos(tt))
                    prr=pr.real
                    print("\033[1;32m"+"Su producto punto es: ",prr)
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
                elif n == 2:
                    print("\033[1;32m"+"Ingrese la magnitud del vector A: ")
                    m1=int(input())
                    print("\033[1;32m"+"Ingrese la magnitud del vector B: ")
                    m2=int(input())
                    mr = (m1*m2)
                    print("\033[1;32m"+"Ingresa el angulo: ")
                    a=int(input())
                    pr = (mr)*(cos(a))
                    prr = pr.real
                    print("\033[1;32m"+"Su producto punto es: ",prr)   
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
            elif case3 == 4:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                A=[a,b]
                B=[a2,b2]
                pp=np.cross(A, B)
                print("\033[1;32m"+"Su producto cruzado es: ",pp)
                rep=(input(("¿Desea graficar mas vectores? S/N")))
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
        elif case2 == 4:
            print("Ingresa la cordenadas x del vector")
            x1=int(input())
            print("Ingresa la cordenada y del vector")
            y1=int(input())
            print("Ingresa la cordenadas a del vector directriz")
            a=int(input())
            print("Ingresa la cordenada b del vector directriz")
            b=int(input())
            t=1

            x=a*t+x1
            y=b*t+y1
            xy=[x,y]
            print("Su vector complementario es: ",xy)

            ax = plt.axes()
            ax.arrow(0,0, x1,y1 , head_width=0.5, head_length=0.1,color='blue')
            ax.arrow(x1,y1, a,b , head_width=0.5, head_length=0.1, color='green')
            ax.arrow(0,0, x,y , head_width=0.5, head_length=0.01, color='red')
            plt.show()

            
    elif case == 2:
        print("**************Graficadora de Vectores**************")
        print("1. Graficar por Coordenadas")
        print("2. Operaciones basicas")
        case2=int(input("Selecciona una Opcion ")) 

        if case2 == 1:
            v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 1 a 4: "))

            if v == 1:
                print("Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                x = np.array([[0,a]])
                print("Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                y = np.array([[0,b]])
                print("Ingresa la coordenada en el eje z del vector : 1")
                c=int(input())
                z= np.array([[0,c]])
                fig = plt.figure()
                ax1 = fig.add_subplot(111,projection='3d')
                ax1.plot_wireframe(x, y, z)
                plt.show()
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 2:
                print("Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                x = np.array([[0,a]])
                print("Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                y = np.array([[0,b]])
                print("Ingresa la coordenada en el eje z del vector : 1")
                c=int(input())
                z = np.array([[0,c]])
                print("Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                x2 = np.array([[0,a2]])
                print("Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                y2 = np.array([[0,b2]])
                print("Ingresa la coordenada en el eje z del vector : 2")
                c2=int(input())
                z2 = np.array([[0,c2]])
                fig = plt.figure()
                ax1 = fig.add_subplot(111,projection='3d')
                ax1.plot_wireframe(x, y, z)
                ax1.plot_wireframe(x2, y2, z2)
                plt.show()
                r=input(("Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(a+a2)
                    xr = np.array([[0,rx]])
                    ry=(b+b2)
                    yr = np.array([[0,ry]])
                    rz=(c+c2)
                    zr = np.array([[0,rz]])
                    Result=math.sqrt((rx*rx)+(ry*ry)+(rz*rz))
                    angulo=(math.acos(rx/Result))
                    angulo2=(math.acos(ry/Result))
                    angulo3=(math.acos(rz/Result))
                    ang=math.degrees(angulo)
                    ang2=math.degrees(angulo2)
                    ang3=math.degrees(angulo3)
                    fig = plt.figure()
                    ax1 = fig.add_subplot(111,projection='3d')
                    ax1.plot_wireframe(xr, yr, zr)
                    print("ANGULOS DEL VECTOR R: ")
                    print("Angulo alpha : ",ang)
                    print("Angulo beta : ",ang2)
                    print("Angulo gama : ",ang3)
                    plt.show()
                else:
                    "OK :)"
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 3:
                print("Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                x = np.array([[0,a]])
                print("Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                y = np.array([[0,b]])
                print("Ingresa la coordenada en el eje z del vector : 1")
                c=int(input())
                z = np.array([[0,c]])
                print("Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                x2 = np.array([[0,a2]])
                print("Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                y2 = np.array([[0,b2]])
                print("Ingresa la coordenada en el eje z del vector : 2")
                c2=int(input())
                z2 = np.array([[0,c2]])
                print("Ingresa la coordenada en el eje x del vector : 3")
                a3=int(input())
                x3 = np.array([[0,a3]])
                print("Ingresa la coordenada en el eje y del vector : 3")
                b3=int(input())
                y3 = np.array([[0,b3]])
                print("Ingresa la coordenada en el eje z del vector : 3")
                c3=int(input())
                z3 = np.array([[0,c3]])
                fig = plt.figure()
                ax1 = fig.add_subplot(111,projection='3d')
                ax1.plot_wireframe(x, y, z)
                ax1.plot_wireframe(x2, y2, z2)
                ax1.plot_wireframe(x3, y3, z3)
                plt.show()
                r=input(("Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(a+a2+a3)
                    xr = np.array([[0,rx]])
                    ry=(b+b2+b3)
                    yr = np.array([[0,ry]])
                    rz=(c+c2+c3)
                    zr = np.array([[0,rz]])
                    Result=math.sqrt((rx*rx)+(ry*ry)+(rz*rz))
                    angulo=(math.acos(rx/Result))
                    angulo2=(math.acos(ry/Result))
                    angulo3=(math.acos(rz/Result))
                    ang=math.degrees(angulo)
                    ang2=math.degrees(angulo2)
                    ang3=math.degrees(angulo3)
                    fig = plt.figure()
                    ax1 = fig.add_subplot(111,projection='3d')
                    ax1.plot_wireframe(xr, yr, zr)
                    print("ANGULOS DEL VECTOR R: ")
                    print("Angulo alpha : ",ang)
                    print("Angulo beta : ",ang2)
                    print("Angulo gama : ",ang3)
                    plt.show()
                else:
                    print("OK :)")
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif v == 4:
                print("Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                x = np.array([[0,a]])
                print("Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                y = np.array([[0,b]])
                print("Ingresa la coordenada en el eje z del vector : 1")
                c=int(input())
                z = np.array([[0,c]])
                print("Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                x2 = np.array([[0,a2]])
                print("Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                y2 = np.array([[0,b2]])
                print("Ingresa la coordenada en el eje z del vector : 2")
                c2=int(input())
                z2 = np.array([[0,c2]])
                print("Ingresa la coordenada en el eje x del vector : 3")
                a3=int(input())
                x3 = np.array([[0,a3]])
                print("Ingresa la coordenada en el eje y del vector : 3")
                b3=int(input())
                y3 = np.array([[0,b3]])
                print("Ingresa la coordenada en el eje z del vector : 3")
                c3=int(input())
                z3 = np.array([[0,c3]])
                print("Ingresa la coordenada en el eje x del vector : 4")
                a4=int(input())
                x4 = np.array([[0,a4]])
                print("Ingresa la coordenada en el eje y del vector : 4")
                b4=int(input())
                y4 = np.array([[0,b4]])
                print("Ingresa la coordenada en el eje z del vector : 4")
                c4=int(input())
                z4 = np.array([[0,c4]])
                fig = plt.figure()
                ax1 = fig.add_subplot(111,projection='3d')
                ax1.plot_wireframe(x, y, z)
                ax1.plot_wireframe(x2, y2, z2)
                ax1.plot_wireframe(x3, y3, z3)
                ax1.plot_wireframe(x4, y4, z4)
                plt.show()
                r=input(("Desea calcular el vector resultante S/N: "))
                if r == "s" or r == "S":
                    rx=(a+a2+a3)
                    xr = np.array([[0,rx]])
                    ry=(b+b2+b3)
                    yr = np.array([[0,ry]])
                    rz=(c+c2+c3)
                    zr = np.array([[0,rz]])
                    Result=math.sqrt((rx*rx)+(ry*ry)+(rz*rz))
                    angulo=(math.acos(rx/Result))
                    angulo2=(math.acos(ry/Result))
                    angulo3=(math.acos(rz/Result))
                    ang=math.degrees(angulo)
                    ang2=math.degrees(angulo2)
                    ang3=math.degrees(angulo3)
                    fig = plt.figure()
                    ax1 = fig.add_subplot(111,projection='3d')
                    ax1.plot_wireframe(xr, yr, zr)
                    print("ANGULOS DEL VECTOR R: ")
                    print("Angulo alpha : ",ang)
                    print("Angulo beta : ",ang2)
                    print("Angulo gama : ",ang3)
                    plt.show()
                else:
                    print("OK :)")
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
        elif case2 == 2:
            print("***********MENU**********")
            print("1. SUMA")
            print("2. RESTA")
            print("3. PRODUCTO PUNTO")
            print("4. PRODUCTO CRUZADO")
            print("5. ECUACION DEL PLANO")
            case3=int(input("Ingrese una opccion: "))


            if case3 == 1:
                v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 2 a 4: "))

                if v == 2:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    v=[]
                    x=a+a2
                    y=b+b2
                    z=c+c2
                    V=[x,y,z]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    if r == 1:
                        xx=np.array([[0,x]])
                        yy=np.array([[0,y]])
                        zz=np.array([[0,z]])
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111,projection='3d')
                        ax1.plot_wireframe(xx, yy, zz)
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
                elif v == 3:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 3")
                    c3=int(input())
                    x=a+a2+a3
                    y=b+b2+b3
                    z=c+c2+c3
                    V=[x,y,z]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    if r == 1:
                        xx=np.array([[0,x]])
                        yy=np.array([[0,y]])
                        zz=np.array([[0,z]])
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111,projection='3d')
                        ax1.plot_wireframe(xx, yy, zz)
                        plt.show()
                        #hasta aqui git hoy
                    else:
                        print("BYE :)")
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
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 3")
                    c3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 4")
                    a4=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 4")
                    b4=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 4")
                    c4=int(input())
                    x=a+a2+a3+a4
                    y=b+b2+b3+b4
                    z=c+c2+c3+c4
                    V=[x,y,z]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    #hasta aqui git hoy 19/10
                    if r == 1:
                        xx=np.array([[0,x]])
                        yy=np.array([[0,y]])
                        zz=np.array([[0,z]])
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111,projection='3d')
                        ax1.plot_wireframe(xx, yy, zz)
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
            elif case3 == 2:
                v=int(input("\033[1;32m"+"Digite la cantidad de vectores a graficar de 2 a 4: "))

                if v == 2:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    v=[]
                    x=a-a2
                    y=b-b2
                    z=c-c2
                    V=[x,y,z]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    if r == 1:
                        xx=np.array([[0,x]])
                        yy=np.array([[0,y]])
                        zz=np.array([[0,z]])
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111,projection='3d')
                        ax1.plot_wireframe(xx, yy, zz)
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
                elif v == 3:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 3")
                    c3=int(input())
                    x=a-a2-a3
                    y=b-b2-b3
                    z=c-c2-c3
                    V=[x,y,z]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    if r == 1:
                        xx=np.array([[0,x]])
                        yy=np.array([[0,y]])
                        zz=np.array([[0,z]])
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111,projection='3d')
                        ax1.plot_wireframe(xx, yy, zz)
                        plt.show()
                    else:
                        print("BYE :)")
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
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 3")
                    a3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 3")
                    b3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 3")
                    c3=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 4")
                    a4=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 4")
                    b4=int(input())
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 4")
                    c4=int(input())
                    x=a-a2-a3-a4
                    y=b-b2-b3-b4
                    z=c-c2-c3-c4
                    V=[x,y,z]
                    print("Su vector resultante es: ", V)
                    r=int(input("Desea graficvarlo 1.SI 2.NO: "))
                    if r == 1:
                        xx=np.array([[0,x]])
                        yy=np.array([[0,y]])
                        zz=np.array([[0,z]])
                        fig = plt.figure()
                        ax1 = fig.add_subplot(111,projection='3d')
                        ax1.plot_wireframe(xx, yy, zz)
                        plt.show()
                    else:
                        print("BYE :)")
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
            elif case3 == 3:
                print("\033[1;32m"+"¿Como deseas consegurilo")
                print("\033[1;32m"+"1. Por componentes")
                print("\033[1;32m"+"2. Por magnitudes y angulos")
                m=int(input())

                if m == 1:
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                    a=int(input())
                    x = np.array([[0,a]])
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                    b=int(input())
                    y = np.array([[0,b]])
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                    c=int(input())
                    z = np.array([[0,c]])
                    print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                    a2=int(input())
                    x2 = np.array([[0,a2]])
                    print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                    b2=int(input())
                    y2 = np.array([[0,b2]])
                    print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                    c2=int(input())
                    z2 = np.array([[0,c2]])
                    mag1 = sqrt((a*a)+(b*b)+(c*c))
                    mag2 = sqrt((a2*a2)+(b2*b2)+(c2*c2))
                    magr = (mag1*mag2)
                    r = ((a*a2) + (b*b2) + (c*c2))
                    te = asin((r/magr))
                    tt=te.real
                    t=math.degrees(tt)
                    print("\033[1;32m"+"Teta : ",t)
                    pr = (magr)*(cos(t))
                    p=pr.real
                    print("\033[1;32m"+"Su producto punto es: ",p)
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
                elif m == 2:
                    print("\033[1;32m"+"Ingrese la magnitud del vector A: ")
                    m1=int(input())
                    print("\033[1;32m"+"Ingrese la magnitud del vector B: ")
                    m2=int(input())
                    mr = (m1*m2)
                    print("\033[1;32m"+"Ingresa el angulo: ")
                    a=int(input())
                    pr = (mr)*(cos(a))
                    p=pr.real
                    print("\033[1;32m"+"Su producto punto es: ",p)
                    rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                    if rep == "s" or rep == "S":
                        repetir = True
                    else:
                        repetir=False
            elif case3 == 4:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                c=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                c2=int(input())
                A=[a,b,c]
                B=[a2,b2,c2]
                pp=np.cross(A, B)
                print("\033[1;32m"+"Su producto cruzado es: ",pp)
                print("\033[1;32m"+"¿Desea obtener sus componentes? 1. YES 2.NO")
                n2=int(input())
                if n2 == 1:
                    ma=sqrt((a*a)+(b*b)+(c*c))
                    ma2=sqrt((a2*a2)+(b2*b2)+(c2*c2))
                    mr=sqrt((pp[0]*pp[0])+(pp[1]*pp[1])+(pp[2]*pp[2]))
                    mm=(ma*ma2)
                    te=asin((mr)/(mm))
                    t=te.real
                    tt=math.degrees(t)
                    maa=ma.real
                    ma22=ma2.real
                    mp=mm.real
                    print("Magnitud de A:",maa )
                    print("Magnitud de B: ",ma22)
                    print("Magnitud del producto: ",mp)
                    print("Angulo Teta: ",tt)
                print("\033[1;32m"+"¿Desea graficarlo? 1. YES 2.NO")
                n=int(input())
                if n == 1:
                    x=np.array([[0,pp[0]]])
                    y=np.array([[0,pp[1]]])
                    z=np.array([[0,pp[2]]])
                    fig = plt.figure()
                    ax1 = fig.add_subplot(111,projection='3d')
                    ax1.plot_wireframe(x, y, z)
                    plt.show()
                elif n == 2:
                    print("BYE :)")
                rep=(input(("¿Desea graficar mas vectores? S/N")))
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
            elif case3 == 5:
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 1")
                a=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 1")
                b=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 1")
                c=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje x del vector : 2")
                a2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje y del vector : 2")
                b2=int(input())
                print("\033[1;32m"+"Ingresa la coordenada en el eje z del vector : 2")
                c2=int(input())
                A=[a,b,c]
                B=[a2,b2,c2]
                pp=np.cross(A, B)
                perMag=(np.dot(pp,pp))**0.5
                ecc=(pp[0]*a)+(pp[1]*b)+(pp[2]*c)
                
                if ecc>0:
                    D=0-ecc
                elif ecc<=0:
                    D=0+ecc
                print("El parametro D de la ecuacion es: ",D)
                print("La ecuacion general del plano es; ",pp[0],"x",pp[1],"y",pp[2],"z + ",D)
                r=int(input("¿Desea gfaficarla? 1.SI 2.NO: "))
                if r==1:
                    x=np.array([[0,a]])
                    y=np.array([[0,b]])
                    z=np.array([[0,c]])
                    x2=np.array([[0,a2]])
                    y2=np.array([[0,b2]])
                    z2=np.array([[0,c2]])
                    mag=math.sqrt((pp[0]*pp[0])+(pp[1]*pp[1])+(pp[2]*pp[2]))
                    u1=Fraction(1/mag)
                    u=((-(b+c)/a),(-(a+c)/b),(-((a+b)/c)))
                    b3=b2*-1
                    v=[b3,a,0]
                    v1=np.cross(v,[0,1,0])
                    if v1[2]<0:
                        v2=v1[2]*-1
                        v3=v2+pp[2]
                    elif pp[2]<0:
                        v2=(pp[2]*-1)
                        v3=v1[2]+v2
                    elif v1[2]<0 and pp[2]<0:
                        v2=v1[2]*-1
                        v22=(pp[2]*-1)
                        v3=v2+v22
                    else:
                        v3=v1[2]+pp[2]
                    x3=np.array([[0,v1[0]]])
                    y3=np.array([[0,v1[1]]])
                    z3=np.array([[0,v3]])
                    fig = plt.figure()
                    ax1 = fig.add_subplot(111,projection='3d') 
                    ax1.plot_wireframe(x, y, z, color='b')
                    ax1.plot_wireframe(x2, y2, z2, color='y')                        
                    ax1.plot_wireframe(x3, y3, z3, color='g')
                    ax1.plot(np.array([0,0]), np.array([0,0]), np.array([0,0]), marker='o', color='y')
                    plt.show()

                else:
                    print("BYE")
                rep=(input(("¿Desea graficar mas vectores? S/N")))
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False
