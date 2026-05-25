class Estudiantes:
    def __init__(self, nombre, apellido, numero_matricula, carrera):

        self.nombre = nombre
        self.apellido = apellido
        self.numero_matricula = numero_matricula
        self.carrera = carrera
        self.cursos = []



    def __str__(self):
        return f"Nombre :{self.nombre} - Apellido: {self.apellido} - Carrera: {self.carrera} - Matricula : {self.numero_matricula}"

    def registrar_estudiantes(self):
        print(f"\033[33mEstudiante registrado:\033[0m {self}")
             
    def baja_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)
            curso.alumnos_inscriptos.remove(self)
            print(f"\033[31m{self.nombre} se dio de baja de {curso.nombre_curso}\033[0m")
        else:
            print(f"{self.nombre} no está inscripto en {curso.nombre_curso}")

    def estado_estudiante(self):
        cursos_nombres = [c.nombre_curso for c in self.cursos]
        if cursos_nombres:
            print(f"{self.nombre} {self.apellido} - Cursos inscriptos: {', '.join(cursos_nombres)}")
        else:
            print(f"{self.nombre} {self.apellido} - No está inscripto en ningún curso")
         




   



class Cursos:
    def __init__(self, nombre_curso, codigo_curso, profesor, cantidad_alumnos):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.profesor = profesor
        self.cantidad_alumnos = cantidad_alumnos
        self.alumnos_inscriptos = []  

    def __str__(self):
        return (f"Curso: {self.nombre_curso} - Código: {self.codigo_curso} - "
                f"Profesor: {self.profesor} - Límite alumnos: {self.cantidad_alumnos} ")

    def registro_cursos(self):
        print(f"\033[33mCurso registrado:\033[0m {self}")
        if self.cantidad_alumnos <= 50:
            print(f"El curso de {self.nombre_curso} es poco numeroso")
        else:
            print(f"El curso de {self.nombre_curso} es numeroso")

    def inscribirse_cursos(self, alumno):
        if alumno in self.alumnos_inscriptos:
            print(f"{alumno.nombre} ya esta registrado en {self.nombre_cursocurso}")
            return
        
        if len(self.alumnos_inscriptos) < self.cantidad_alumnos:
            self.alumnos_inscriptos.append(alumno)
            alumno.cursos.append(self)
            print(f"{alumno.nombre} {alumno.apellido} se inscribió en {self.nombre_curso}")
        else:
            print("todos los cupos estan ocupados")

    def estado_curso(self):
        inscriptos = len(self.alumnos_inscriptos)
        cupos_disponibles = self.cantidad_alumnos - inscriptos
        print(f"{self.nombre_curso} - Código: {self.codigo_curso} - Profesor: {self.profesor}")
        print(f"Inscriptos: {inscriptos} | Cupos disponibles: {cupos_disponibles}")