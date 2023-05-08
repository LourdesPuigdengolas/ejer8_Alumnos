class Alumno:  #dni;apellido;nombre;carrera;a�oquecursa
    __dniA=''
    __apell=''
    __nom=''
    __carrera=''
    __anioCursa=''
    def __init__(self, dniA,apell,nom,carrera,anioCursa):
        __dniA=dniA
        __apeall=apell
        __nom=nom
        __carrera=carrera
        __anioCursa=anioCursa

    def get_dniA(self):
        return self.__dniA

    def get_apell(self):
        return self.__apell
    def get_nom(self):
        return self.__nom
    def get_carrera(self):
        return self.__carrera
    def get_anioCursa(self):
        return self.__anioCursa

