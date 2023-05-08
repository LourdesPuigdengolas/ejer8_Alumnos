class Materia:   
    __dni=''
    __nomMateria=''
    __fecha=''
    __nota=''
    __aprobacion=''

    def __init__(self, dni, nomMateria, fecha,nota,aprobacion ):
        __dni= dni
        __nomMateria= nomMateria
        __fecha= fecha
        __nota=nota
        __aprobacion= aprobacion

    def get_dni(self):
      return self.__dni
    def get_nota(self):
      return self.__nota
    def get_nomMateria(self):
      return self.__nomMateria
    def get_fecha(self):
      return self.__fecha
    def get_aprobacion(self):
      return self.__aprobacion