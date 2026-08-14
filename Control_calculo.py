# SISTEMA DE CONTROL Y CÁLCULO DE PROMEDIO ACADÉMICO

# clase padre
class Evaluacion:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")


#clase hija 1
class Examen(Evaluacion):
    def __init__(self, nombre, nota, tipo_examen):
        super().__init__(nombre, nota)
        self.tipo_examen = tipo_examen

    def obtener_informacion(self):
        return f"{self.nombre} (Examen {self.tipo_examen}): {self.nota:.2f} pts"


# clase hija 2
class TrabajoPractico(Evaluacion):
    def __init__(self, nombre, nota, es_grupal):
        super().__init__(nombre, nota)
        self.es_grupal = es_grupal

    def obtener_informacion(self):
        modalidad = "Grupal" if self.es_grupal else "Individual"
        return f"{self.nombre} (Trabajo {modalidad}): {self.nota:.2f} pts"