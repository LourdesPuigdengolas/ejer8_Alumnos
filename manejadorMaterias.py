from claseMateria import Materia

class gestorMaterias:
    materias=[]
    def __init__(self,materias ):
        self.__listaMaterias= materias

    def promAplazo(materias):
        for i in range(len(Materia)):
            if Materia[i].__nota < 4:
                cont=''
                m=''
                m+= Materia.__nota 
                cont+=1
                promApz= m/cont 
        print(f'El promedio con aplazo es de: {promApz}') 
    
    def promSinAplaz(self):
        for i in range(len(Materia)):
            if Materia[i].__nota >= 4:
                cont=''
                m=''
                m+= Materia.__nota 
                cont+=1
                prom= m/cont 
        print(f'El promedio sin aplazo es de: {prom}') 

    def alumPromocional(self):
        if Materia.__nota >= 7:
            return self
       
    
