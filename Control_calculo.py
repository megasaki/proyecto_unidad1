
class Evaluacion:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")

class Examen(Evaluacion):
    def __init__(self, nombre, nota, tipo_examen):
        super().__init__(nombre, nota)
        self.tipo_examen = tipo_examen

    def obtener_informacion(self):
        return f"{self.nombre} (Examen {self.tipo_examen}): {self.nota:.2f} pts"

class TrabajoPractico(Evaluacion):
    def __init__(self, nombre, nota, es_grupal):
        super().__init__(nombre, nota)
        self.es_grupal = es_grupal

    def obtener_informacion(self):
        modalidad = "Grupal" if self.es_grupal else "Individual"
        return f"{self.nombre} (Trabajo {modalidad}): {self.nota:.2f} pts"


registro_academico = [
    TrabajoPractico("Tarea 1", 85.0, es_grupal=False),
    Examen("Examen Parcial 1", 68.0, tipo_examen="Parcial"),
    TrabajoPractico("Sistemático 1", 92.0, es_grupal=True)
]


def mostrar_notas_precargadas(registro):
    print("\n--- NOTAS REGISTRADAS EN LA ASIGNATURA ---")
    if not registro:
        print("No hay evaluaciones registradas.")
        return

    for i, evaluacion in enumerate(registro):
        print(f"{i + 1}. {evaluacion.obtener_informacion()}")


def registrar_nota(registro):
    print("\n--- REGISTRAR NUEVA EVALUACIÓN ---")
    print("Tipo de actividad:")
    print("1. Examen")
    print("2. Trabajo Práctico")        
    
    while True:
        try:
            opcion_tipo = int(input("Seleccione el tipo (1 o 2): "))
            if opcion_tipo in [1, 2]:
                break 
            else:
                print(" Error: Selección inválida. Por favor, ingrese el número 1 o 2.")
        except ValueError:
            print(" Error: Debe ingresar un número entero (1 o 2). No se aceptan letras.")

    while True:
        nombre_evaluacion = input("Ingrese el nombre de la evaluación: ").strip()
        
        if not nombre_evaluacion:
            print(" Error: El nombre no puede estar vacío.")
        elif not any(letra.isalpha() for letra in nombre_evaluacion):
            print(" Error: El nombre debe contener letras (ej. 'Tarea 2'). No ingrese solo números.")
        else:
            break 
    
    while True:
        try:
            nota_input = float(input("Ingrese la nota obtenida (0 - 100): "))

            if 0 <= nota_input <= 100:
                if opcion_tipo == 1:
                    nueva_evaluacion = Examen(nombre_evaluacion, nota_input, "General")
                else:
                    nueva_evaluacion = TrabajoPractico(nombre_evaluacion, nota_input, es_grupal=False)
                
                registro.append(nueva_evaluacion)
                print(f" Éxito: '{nombre_evaluacion}' guardada correctamente con {nota_input:.2f} pts.")
                break
            else:
                print(" Error: La nota debe estar entre 0 y 100. Intente de nuevo.")

        except ValueError:
            print(" Error: Por favor, ingrese un número válido (ej. 85 o 78.5).")

def calcular_promedio_y_estado(registro):
    print("\n--- BALANCE ACADÉMICO Y ESTADO ---")
    if not registro:
        print("No hay datos suficientes.")
        return
    
    lista_notas = [evaluacion.nota for evaluacion in registro]
    promedio = sum(lista_notas) / len(lista_notas)

    if promedio >= 70.0:
        estado = "APROBADO"
    elif 60.0 <= promedio < 70.0:
        estado = "EN RIESGO"
    else:
        estado = "REPROBADO"

    print(f"Promedio acumulado actual: {promedio:.2f} / 100 pts")
    print(f"Estado de la asignatura: [{estado}]")


def generar_metricas(registro):
    print("\n--- MÉTRICAS Y RENDIMIENTO DETALLADO ---")
    if not registro:
        print("No hay notas suficientes para generar métricas.")
        return
    
    lista_notas = [ev.nota for ev in registro]
    lista_nombres = [ev.nombre for ev in registro]

    nota_maxima = max(lista_notas)
    nota_minima = min(lista_notas)

    idx_max = lista_notas.index(nota_maxima)
    idx_min = lista_notas.index(nota_minima)
    promedio_actual = sum(lista_notas) / len(lista_notas)

    print(f" Proyección: Nota más alta: {nota_maxima:.2f} pts ({lista_nombres[idx_max]})")
    print(f" Proyección: Nota más baja: {nota_minima:.2f} pts ({lista_nombres[idx_min]})")

    if promedio_actual >= 70.0:
        print(" Proyección: ¡Ya tienes el promedio suficiente para aprobar la asignatura!")
    else:
        puntos_faltantes = 70.0 - promedio_actual
        print(f" Proyección: Te faltan {puntos_faltantes:.2f} pts en tu promedio acumulado para alcanzar la nota mínima de aprobación (70 pts).")



def ejecutar_sistema():
    while True:
        print()
        print("==========================================")
        print(" SISTEMA DE NOTAS ACADÉMICAS ")
        print("==========================================")
        print("1. Ver notas registradas (Datos iniciales)")
        print("2. Registrar una nueva nota")
        print("3. Calcular promedio y estado académico")
        print("4. Generar métricas de rendimiento")
        print("5. Salir")

        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))

            if opcion == 1:
                mostrar_notas_precargadas(registro_academico)
            elif opcion == 2:
                registrar_nota(registro_academico)
            elif opcion == 3:
                calcular_promedio_y_estado(registro_academico)
            elif opcion == 4:
                generar_metricas(registro_academico)
            elif opcion == 5:
                print("\nSistema finalizado. ¡Éxito en la materia!")
                break
            else:
                print(" Error: Opción no válida. Ingrese un número del 1 al 5.")

        except ValueError:
            print(" Error: Ingrese únicamente el número de la opción elegida (1, 2, 3, 4 o 5).")

if __name__ == "__main__":
    ejecutar_sistema()