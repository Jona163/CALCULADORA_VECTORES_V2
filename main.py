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
