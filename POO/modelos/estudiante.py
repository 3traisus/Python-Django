class Estudiante:
    # Declaran las variables de clase

    # Método constructor
    def __init__(self, control, nombre, sexo, correo_electronico, fecha_nacimiento, rfc, escuela_procedencia):
        # Variables de instancia
        self.control = control
        self.nombre = nombre
        self.sexo = sexo
        self.correo_electronico = correo_electronico
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        self.escuela_procedencia = escuela_procedencia
        self.estado = True

    # Método especial __str__(self)
    def __str__(self):
        return f" Control:{self.control}, Nombre:{self.nombre}, Correo electrónico:{self.correo_electronico},Estado:{self.estado} "

    # Método de instancia
    def cambiar_estado(self):
        self.estado = not self.estado


class ListaEstudiante:
    def __init__(self):
        self.lista_estudiantes = []

    # Método de instancia agregar_estudiante(estudiante) : boolean
    def agregar_estudiante(self, estudiante):
        # Verificar que no este repetido el numero de control
        indice = self.buscar_estudiante(estudiante.control)
        if indice == -1:
            self.lista_estudiantes.append(estudiante)
            return True
        else:
            return False

    # Método de instancia para buscar un estudiante
    def buscar_estudiante(self, ctrl):
        posicion = 0
        for estudiante in self.lista_estudiantes:
            if ctrl == estudiante.control:
                return posicion
            posicion += 1
        return -1 # No existe el estudiante en la lista

    # Método de instancia
    def eliminar_estudiante(self, ctrl):
        # Buscar estudiante
        indice = self.buscar_estudiante( ctrl )
        if indice != -1:
            self.lista_estudiantes[indice].cambiar_estado()
            return True
        return False

    # Método de instancia para mostrar el contenido
    def reporte_estudiante(self):
        # Ordenar la lista
        self.lista_estudiantes.sort( key= lambda t: t.nombre )
        for est in self.lista_estudiantes:
            print(est)

    # Método de instancia que actualice un estudiante
    def actualizar_estudiante(self, estudiante ):
        # Buscar al estudiante
        indice = self.buscar_estudiante( estudiante.control )
        if indice != -1:
            # Actualizar el registro
            self.lista_estudiantes.pop(indice)
            self.agregar_estudiante( estudiante )
            return True
        return False

# obj_estudiante1 = Estudiante("18420100", "Benito", "Masculino", "jose-luis@gmail.com", "1990/12/01", "JOLU19901201", "Preparatoria Julian de los Reyes")
# obj_estudiante2 = Estudiante("18420200", "Zacarias", "Masculino", "jose-luis@gmail.com", "1990/12/01", "JOLU19901201", "Preparatoria Julian de los Reyes")
# obj_estudiante3 = Estudiante("18420300", "Antonio", "Masculino", "jose-luis@gmail.com", "1990/12/01", "JOLU19901201", "Preparatoria Julian de los Reyes")
#
# lista = ListaEstudiante()
# lista.agregar_estudiante(obj_estudiante1)
# lista.agregar_estudiante(obj_estudiante2)
# lista.agregar_estudiante(obj_estudiante3)
#
# # lista.eliminar_estudiante("18420200")
#
# obj_estudiante_modififcado = Estudiante("18420100", "Jose Luis Gutierrez Hernandez", "Masculino", "jose.luis.gutierrez.hernandez@gmail.com", "1990/12/01", "JOLU19901201", "Preparatoria por Cooperación de Zacapu")
#
# # lista.actualizar_estudiante( obj_estudiante_modififcado )
# lista.reporte_estudiante()

