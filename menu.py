from gestion import Estudiantes,Cursos

cursos_registrados =[]
alumnos_registrados = []
def menu():

    print("\n\t\033[32mREGISTRAR ESTUDIANTE\033[0m \033[31m( presione 1)\033[0m")
    print("\n\t\033[32mREGISTRAR CURSO\033[0m \033[31m(presione 2)\033[0m")
    print("\n\t\033[32mINSCRIPCION A CURSO\033[0m \033[31m( presione 3)\033[0m")
    print("\n\t\033[32mBAJA DE CURSOS\033[0m \033[31m( presione 4)\033[0m")
    print("\n\t\033[32mCONSULTA DE ESTADO\033[0m \033[31m( presione 5)\033[0m")
    print("\n\t\033[32mSALIR\033[0m \033[31m( presione 0)\033[0m")
    

    while True:


     opciones = int(input("\n\t\033[35mseleccione una opcion :\033[0m"))

    

     if opciones == 1:
        print("REGISTRAR ESTUDIANTE:")
        cant = int(input("ingrese la cantidad de estudiantes que desea registrar :"))
        for a in range(cant):
         nombre = input("ingrese nombre :")
         apellido = input("ingrese apellido :")
         carrera = input("ingrese su carrera :")

         while True:
              try:
                numero_matricula = int(input("ingrese el numero de matricula :"))
                existe = any(alumno.numero_matricula == numero_matricula for alumno in alumnos_registrados)
                if existe:
                    print("la matricula ya esta registrada, ingrese otra.")    

                else:
                   break  
              except ValueError:
                print("el numero de matricula debe ser numerico")
              
         estudiante = Estudiantes(nombre, apellido, numero_matricula, carrera)
         estudiante.registrar_estudiantes()
         alumnos_registrados.append(estudiante)
        


         

     if opciones == 2:
        print("selecciono opcion 2")
        print("REGISTRAR CURSO:")
        cant = int(input("ingrese la cantidad de cursos que desea agregar :"))
        for a in range(cant):
         nombre_curso = input("ingrese nombre del curso:")
         cantidad_alumnos = int(input("cantidad de alumno permitidos :"))
         profesor = input("ingrese el nombre del profesor encargado :")

         while True:
              try:
                codigo_curso = int(input("ingrese el codigo del curso :"))
                repetido = any(curso.codigo_curso == codigo_curso for curso in cursos_registrados)
                if repetido:
                    print("el codigo ya esta registradao, ingrese otro.")    

                else:
                   break  
              except ValueError:
                print("el numero de codigo debe ser numerico")
              
         curso = Cursos(nombre_curso, codigo_curso, profesor, cantidad_alumnos)
         curso.registro_cursos()
         cursos_registrados.append(curso)


     if opciones == 3:
      print("REGISTRAR CURSO:")

      if opciones == 3:
       matricula = int(input("Ingrese la matrícula del alumno: "))
       codigo = int(input("Ingrese el código del curso: "))

       alumno_encontrado = next((a for a in alumnos_registrados if a.numero_matricula == matricula), None)
       curso_encontrado = next((c for c in cursos_registrados if c.codigo_curso == codigo), None)

       if alumno_encontrado is None:
        print("no se encontro al alumno")
       elif curso_encontrado is None:
        print("no se encontro el curso")
       else:
        curso_encontrado.inscribirse_cursos(alumno_encontrado)
 



     if opciones == 4:
      print("\n DARSE DE BAJA EN CURSO")
      matricula = int(input("Ingrese la matrícula del alumno: "))
      codigo = int(input("Ingrese el código del curso: "))

      alumno = next((a for a in alumnos_registrados if a.numero_matricula == matricula), None)
      curso = next((c for c in cursos_registrados if c.codigo_curso == codigo), None)

      if alumno is None:
        print("alumno no encontrado")
      elif curso is None:
        print("curso no encontrado")
           
      else:
         alumno.baja_curso(curso)

     if opciones == 5:
        print("\nEstado de Cursos:")
        for curso in cursos_registrados:
         curso.estado_curso()

        print("\nEstado de Estudiantes:")
        for alumno in alumnos_registrados:
         alumno.estado_estudiante()
 
     if  opciones == 0:
        print("\033[93m saliendo del programa....\033[0m")
        break




menu()