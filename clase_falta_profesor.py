""" 
1 Alumno es el profesor
1 Alumno es asistente

A - Pedir la edad de los companeros que vinieron hoy a clase y ordenarlos de menor a mayor.

B - El mayor es el profesor y el menor es el asistente: Quien es quien?
"""

def obtener_companeros(cantidad_companeros):
    companeros = [];
    for i in range(cantidad_companeros):
        nombre = input("Ingresa el nombre: ");
        edad = int(input("Ingrese la edad: "));
        companero = (nombre, edad);
        companeros.append(companero);
    companeros.sort(key = lambda x: x[1]);
    asistente = companeros[0][0];
    profesor = companeros[-1][0];
    return asistente, profesor;

cantidad_alumnos = int(input("Ingresa el numero de alumnos que asistieron: "));
asistente, profesor = obtener_companeros(cantidad_alumnos);

print(f"El profesor es: {profesor} y su asistente es {asistente}");

