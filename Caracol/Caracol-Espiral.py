# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:49:54 2019

@author: Administrador
"""
def archivo():
    return "D:\Caracol\Matriz.txt"
def size(l):
    return len(l[0])
def leer_archivo(txt):
    return [[int(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(txt).readlines()]]]

def spiralReading(l,direction,deeper,size,i,j):
    print(l[i][j])
    if(direction%4==0):
        if(j<size-deeper-1 ):
            spiralReading(l,direction,deeper,size,i,j+1)
        if(j==size-deeper-1 and deeper<int(size/2)):
            spiralReading(l,direction+1,deeper,size,i+1,j)

    if(direction%4==1):
        if(i<size-deeper-1):
            spiralReading(l,direction,deeper,size,i+1,j)
        if(i==size-deeper-1):
            spiralReading(l,direction+1,deeper,size,i,j-1)
    
    if(direction%4==2):
        if(j>0+deeper):
            spiralReading(l,direction,deeper,size,i,j-1)
        if(j==0+deeper and deeper<int((size-1)/2)):
            spiralReading(l,direction+1,deeper,size,i-1,j)
    
    if(direction%4==3):
        if(i>1+deeper):
            spiralReading(l,direction,deeper,size,i-1,j)
        if(i==1+deeper):
            spiralReading(l,direction+1,deeper+1,size,i,j+1)
    
spiralReading(leer_archivo(archivo()),0,0,size(leer_archivo(archivo())),0,0)