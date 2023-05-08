from claseAlumno import Alumno
from claseMateria import Materia
from manejadorMaterias import gestorMaterias
from manejadorAlum import arregloNumPy
import csv

if __name__=='__main__':

    arreAlumnos=arregloNumPy(0,8)   #arreglo del manejadorAlum

    materias= []        #inicializar lista del manejadorMaterias
    with open("materiasAprobadas.csv") as archivo:
                reader = csv.reader(archivo, delimiter=',')
                next(reader, None)      #Omitir el encabezado del archivo
                for fila in reader: 
                        unaMateria= Materia(fila[0], fila[1], fila[2], int(fila[3]), fila[4])
                        materias.append(unaMateria)


    print(f"--- MENU: ---")
    print(f"[1]. Informar promedio von aplazos y sin aplazos . ")
    print(f"[2]. Ver alumnos promocionales")
    print(f"[3]. Lista ordenada de alumnos")
    print(f"[0]. Salir")
    opcion= int(input("Ingrese el numero de opción que desea: "))
        
    while opcion != 0: 
                if opcion == 1:
                        dnii= int(input=('Ingrese su DNI: '))
                        Materia.promAplazo(arreAlumnos)
                        Materia.promSinAplaz(arreAlumnos)

                elif opcion ==2:
                         for i in range(len(Materia)):
                            alum= materias[i].alumPromocional(materias)
                         for i in range(len(Alumno)):
                            arreAlumnos.__promocionales(alum)
                            Alumno.listarAlumProm(alum)  
                
                elif opcion ==3:
                    for i in range(len(Alumno)):
                       arreAlumnos[i].odenar__lt__()

                opcion= int(input("Ingrese el numero de opción que desea: "))

