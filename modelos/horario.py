class Horario:
    def __init__(self):
        self.asignaciones = []

    def agregar(self, asignacion):
        self.asignaciones.append(asignacion)

    def eliminar_ultima(self):
        if self.asignaciones:
            self.asignaciones.pop()