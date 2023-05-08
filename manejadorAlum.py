import numpy as np
from claseAlumno import Alumno

class arregloNumPy:
    __cantidad=0
    __dimension=0
    __incremento=10
    __alumnos=None
   
    def __init__(self, cantidad, dimension, incremento=8):
        self.__puntos= np.empty(dimension, dtype=Alumno)
        self.__cantidad=1
        self.__dimension=dimension
      

    def agregarAlumno(self, unAlumno):
        if self.__cantidad ==self.__dimension:
            self.__dimension+= self.__incremento
            self.__puntos.resize(self.__dimension)
        self.__puntos[self.__cantidad]= unAlumno
        self.__cantidad+=1

    def promocionales(self, unAlumno):
        for i in range(len(Alumno)):
            print(f'Promocionado: {self.__nom}.')

    
    def listarAlumProm(self,nom):
        print('DNI        Ap. y Nombre       Fecha      Nota    Año que cusa')
        for DNI, unAlumno in enumerate(Alumno):
            print(f'{nom}       {repr(Alumno)}')

    def odenar__lt__(self):
        intercambio=True
        while intercambio:
            intercambio =False
            for i in range(len(self.__alumnos)-1):
                 if (self.__alumnos[i] > self.__alumnos[i+1]):
                    self.__alumnos[i], self.__alumnos[i+1]= self.__alumnos[i+1], self.__alumnos[i]
                    intercambio=True

        
           
