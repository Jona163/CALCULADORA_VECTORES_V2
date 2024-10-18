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
                        ang=angulo+180
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
                print("\033[1;32m"+"Teta : ",te)
                pr = (magr)*(cos(te))
                print("\033[1;32m"+"Su producto punto es: ",pr)
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
                print("\033[1;32m"+"Su producto punto es: ",pr)   
                rep=input("\033[1;32m"+"¿Desea graficar mas vectores? [S/N]")
                if rep == "s" or rep == "S":
                    repetir = True
                else:
                    repetir=False             

    elif case == 2:
        print("**************Graficadora de Vectores**************")
        print("1. Graficar por Coordenadas")
        print("2. Producto punto")
        print("3. Poducto Cruz")
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
