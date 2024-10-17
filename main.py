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
