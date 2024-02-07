

class Proceso:
    def __init__(self, no_proceso=None, nombre=None, num1=None, num2=None, operador=None, id=None, time=None):
        self._no_proceso = no_proceso
        self._nombre = nombre
        self._num1 = num1
        self._num2 = num2
        self._operador = operador
        self._id = id
        self._time = time

    def __str__(self):
        return f'''
            ID empleado: {self._no_proceso}, Nombre empleado: {self._nombre},
            Rol empleado: {self._num1} CURP empleado: {self._num2},
            RFC empleado: {self._operador}, Domicilio empleado: {self._id},
            Telefono empleado: {self._time}
        '''

   #Metodos get y set
    @property
    def no_proceso(self):
        return self._no_proceso
    @no_proceso.setter
    def no_proceso(self, no_proceso):
        self._no_proceso = no_proceso

    @property
    def nombre(self):
         return self._nombre
    @nombre.setter
    def nombre(self, nombre):
            self._nombre = nombre

    @property
    def num1(self):
         return self._num1
    @num1.setter
    def num1(self, num1):
            self._num1 = num1

    @property
    def num2(self):
        return self._num2
    @num2.setter
    def num2(self, num2):
            self._num2 = num2

    @property
    def operador(self):
        return self._operador
    @operador.setter
    def operador(self, operador):
            self._operador = operador

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
            self._id = id

    @property
    def time(self):
            return self._time
    @time.setter
    def time(self, time):
            self._time = time

   # Fin de metodos get y set

