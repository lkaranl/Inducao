#!/usr/bin/env python3.8
#####	NAME:				Indução Matemática
#####	VERSION:			0.3
#####	DESCRIPTION:			Indução Matemática  
#####	DATE OF CREATION:		19/08/2020
#####	LAST RELEASE			19/08/2020
#####	WRITTEN BY:			KARAN LUCIANO SILVA
#####	E-MAIL:				karanluciano1@gmail.com			
#####	DISTRO:				ARCH LINUX
#####	LICENSE:			GPLv3 			
#####	PROJECT:			https://github.com/lkaranl/Inducao

import time

vetor = []
x = int(input("Diga o numero de elementos: "))
y = x+1

def somar_elementos(lista):
    for i in range(1,y):
        vetor.append(i)
    soma = 0
    for numero in lista:
        soma += numero
    return soma    

def inducao(n):
    n = ((n*(n+1))/2)
    return int(n)



if __name__ == "__main__":
    inicio = time.time()
    print(somar_elementos(vetor)) 
    fim = time.time()
    print(fim - inicio)

    print("")

    inicio = time.time()
    print(inducao(x))
    fim = time.time()
    print(fim - inicio)  
