#!/usr/bin/env python3 
#creador: Hans Saldias
from colorama import init, Fore, Back, Style
init()
print(Style.BRIGHT+Fore.RED+"""
Author:      Hans Saldias
Creado:      viernes 07 de julio 2023
Uso:         sacar promedios 
Motivo:      practica de programacion
Lenguaje:    python

\n\n""")

print(Style.BRIGHT+Fore.LIGHTBLUE_EX+"""
                                               ############################
                                               || sacador de promedios   ||
                                               ############################

      \n\n""")
print("Script para sacar promedios uso libre\n")
nombre = input("Ingrese nombre COMPLETO del alumno: ").title()
 
materias = int(input("Ingrese cantidad de notas: "))
 
contador = 0
suma = 0

while contador < materias:
    try:
        nota = float(input('\nINGRESE NOTAS DEL ESTUDIANTE: '))
        suma += nota
        contador +=1
    except:
        print("\nIngreso ivalido, intente nuevamente\n")
resultado = suma / materias
resultado = round(resultado, 1)
print(f"""\nNombre estudiante: {nombre} 
      
Promedio del estudiante: {resultado}""")


      