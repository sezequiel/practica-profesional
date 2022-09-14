# ejercicio 1
# Lo primero que haremos sera definir una variable,que contenga
# la edad ingresada por el usuario definir edadUsuario como entero
# Luego ásaremos a imprimir por consola la pregunta escribir "¿cuantos añostiene?
import random


def uno():
    #Se inicializa la variable edadUsuario y se pide por consola
    edadUsuario = int(input('¿cuantos años tiene?: '))
    #se comprueba si es menor
    if edadUsuario < 18:
    #se imprime por consola
        print('!Sos menor de edad!')
    #se comprueba que es mayor
    else:
    #se imprime por consola
        print('!Sos mayor de edad!')


def dos():
    #se incializa la variable sueldo y se pide por consola
    sueldo = int(input('De cuanto es su sueldo? '))
    #se incializa la variable sueldoMinimo y se pide por consola
    sueldoMinimo = int(input('De cuanto es el sueldo minimo actual? '))
    #se hace la comprobación del sueldo es menor
    if sueldo < sueldoMinimo:
    #se imprime por consola
        print('Su sueldo es menor al minimo actual')
    #es mayor al minimo actual
    else:
    #se imprime por consola
        print('Su sueldo es mayor al minimo actual')


# Ejercicio 3
def tres():
    #se incializa la variable numeroIngresado y se pide por consola
    numeroIngresado = int(input('Ingrese el numero a evaluar '))
    #se comprueba si es menor a 100
    if numeroIngresado < 100:
    #se imprime por consola
        print('El numero ingresado es menor a 100 ')
    # sino es mayor a 100
    else:
        #se imprime por consola
        print('El numero ingresado es mayor a 100 ')


# Ejercicio 4
def cuatro():
    #se incializa la variable letraIngresada y se pide por consola
    letraIngresada = input('Ingrese una letra ').strip()
    #se incializa un arreglo letras y se pide por consola
    letras = ['s', 'n']

    #se recorre el arreglo letras
    for letra in letras:
    #se comprueba lo ingresado por consola con cada letra del arreglo
        if letraIngresada == letra:
            #se imprime por consola
            print('Correcto ', letra, ' = ', letraIngresada)
        else:
            #se imprime por consola
            print('Incorrecto')


# Ejercicio 5

def cinco():
    #se incializa la variable numero y se pide por consola
    numero = int(input('Ingrese un numero a evaluar '))
    #se comprueba si el resultado es 0
    if numero % 2 == 0:
        #se imprime por consola
        print('El numero es par')
    else:
        #se imprime por consola
        print('El numero es impar')


# Ejercicio 6
def seis():
    #se inicializa una lista notas
    notas = list()
    #se agrega y se pide al lista notas
    notas.append(int(input('Ingrese su primer nota')))
    notas.append(int(input('Ingrese su segunda nota')))
    notas.append(int(input('Ingrese su tercer nota')))

    #se incializa la variable acu
    acu = int()

    #se recorre la lista notas
    for nota in notas:
        #se utiliza acu para la suma de las notas
        acu = acu + nota
    #se comprueba acu
    if acu / 3 >= 7:
    #se imprime por consola
        print("Alumno Aprobado")
    else:
        #se imprime por consola
        print("Alumno desaprobado")

    #se imprime por consola
    print('Su promedio es ', acu)


# Ejercicio 7
def siete():
    #se incializa la variable cadena de tipo str y se pide por consola
    cadena = str(input('Ingrese la palabra se contaran sus letras '))
    # se imprime por consola
    print('La cadena ingresa tiene ', len(cadena))
    # se comprueba  el tamaño de la cadena con la funcion len()
    if len(cadena) == 6:
    #se imprime por consola
        print("Correcto")
    else:
    #se imprime por consola
        print("Incorrecto")


# Ejercicio 8
def ocho():
    #se incializa la variable cadena y se pide por consola
    cadena = input('Ingrese la palabra a convertir ')
    # se comprueba el tamaño de cadena
    if len(cadena) == 4:
    # se imprime por consola
        print(cadena + cadena.join('!'))
    else:
        # se imprime por consola
        print(cadena + cadena.join('?'))


# Ejercicio 9
def nueve():
    #se incializa la variable descuento y se asigna el valor de 500
    descuento = 500
    #se incializa la variable mes y se pide por consola
    mes = str(input('Ingrese un mes'))
    #se incializa la variable importe y se pide por consola
    importe = int(input('Ingrese el importe de la compra'))
    #se convierte el valor de mes a minuscula
    enMinuscula = mes.lower()
    # se comprueba con condicionales  compuestos or (O)
    if (enMinuscula == 'septiembre' or enMinuscula == 'octubre' or enMinuscula == 'noviembre'):
        total = importe - descuento
        print('Se aplico $500 de descuento ', total)
    else:
        total = importe
        print('No se aplicaron descuentos ', total)
    print('Importe a pagar es de $', total)


# Ejercicio 10
def diez():
    #se incializa la variable numeroUno y se pide por consola
    numeroUno = int(input('ingrese el primer numero'))
    #se incializa la variable numeroDos y se pide por consola
    numeroDos = int(input('ingrese el segundo numero'))

    #se comprueba los numeros ingresados y se usa el operador concional and(Y)
    if (numeroUno % 2 == 0 and numeroDos % 2 == 0):
        print('Los 2 numeros son pares')
    else:
        print('Los 2 numeros no son pares o uno de ellos no lo es')


# Ejercicio 11
def once():
    #se incializa la variable notaUno y se pide por consola
    notaUno = int(input('Ingrese nota 1 '))
    #se incializa la variable notaDos y se pide por consola
    notaDos = int(input('Ingrese nota 2 '))
    #se incializa la variable notaTres y se pide por consola
    notaTres = int(input('Ingrese nota 3 '))

    # se comprueba las notas con el operador condicial (Y)
    if (notaUno >= 1 and notaUno <= 10) and (notaDos >= 1 and notaDos <= 10) and (notaTres >= 1 and notaTres <= 10):
        print('Son notas validas')

    else:
        print('Una o mas notas no son validas')


# Ejercicio 12
def doce():
    #se incializa la variable cadena y se pide por consola
    cadena = str(input('Ingrese la frase a validar ')).strip()
    # se convierte a miniscula la variable cadena lower()
    # se usa la funcion startswith() para saber con que letra empieza la cadena
    if cadena.lower().startswith('a') == True:
        print('La frase comienza con a')
    else:
        print('La frase no comienza con a')


# Ejercicio 13
def trece():
    #se incializa la variable cadena y se pide por consola
    cadena = str(input('Ingrese la frase a validar')).strip()
    # se incialiaza la variable primerCaracter y se asigna el valor la primera letra de cadena
    primerCaracter = cadena[0]

    # se convierte a miniscula la variable cadena lower()
    # se usa la funcion startswith() para saber con que letra empieza la cadena
    if cadena.lower().startswith(primerCaracter) == True and cadena.lower().endswith(primerCaracter) == True:
        print('La frase empieza y termina con ', primerCaracter)
    else:
        print('La frase no empieza y termina con la misma letra')


def catorce():
    # se inicializa la variable minutos
    minutos = int()
    # se inicializa la variable total
    total = float()
    # se inicializa la variable hora
    hora = int(input('ingrese las horas de alquiler'))
    # se comprueba si hora es menor o igual a 2
    if (hora <= 2):
        total = 400
        print('total ', total)
    else:
        litrosNafta = int(input('ingrese los litros de nafta gastados'))
        # se multiplica por 60 para saber la cantidad de minutos
        minutos = hora * 60
        total = (litrosNafta * 40) + (minutos * 5.20)
        print('total ', total)


def quince():
    # se inicializa la variable total y se pide por consola
    numero = int(input('ingrese un numero del 1-7'))
    # No hay swicht en python lo resolvi con diccionarios
    seleccion = {1: 'lunes',
                 2: 'martes',
                 3: 'miercoles',
                 4: 'jueves',
                 5: 'viernes',
                 6: 'sabado',
                 7: 'domingo'}
    # se obtiene el valor de el diccionario por el numero asignado
    print(seleccion.get(numero))


def dieciseis():
    # se inicializa la variable opcion y se pide por consola
    opcion = str(input('ingrese una opcion '))
    # se inicializa la variable numeroUno y se pide por consola
    numeroUno = int(input('ingrese el primer numero'))
    # se inicializa la variable numeroDos y se pide por consola
    numeroDos = int(input('ingrese el segundo numero'))

    # funcion que va asignada a su clave en el diccionario
    def suma(numeroUno, numeroDos):
        return numeroUno + numeroDos
    # funcion que va asignada a su clave en el diccionario
    def resta(numeroUno, numeroDos):
        return numeroUno - numeroDos
    # funcion que va asignada a su clave en el diccionario
    def division(numeroUno, numeroDos):
        return numeroUno / numeroDos
    # funcion que va asignada a su clave en el diccionario
    def multiplicacion(numeroUno, numeroDos):
        return numeroUno * numeroDos

    # No hay swicht en python lo resolvi con diccionario es mas rapido de hacer if seguidos
    # los diccionarios pueden contener objetos asi que use funciones
    case = {'s': suma(numeroUno, numeroDos),
            'r': resta(numeroUno, numeroDos),
            'm': multiplicacion(numeroUno, numeroDos),
            'd': division(numeroUno, numeroDos)}
    print(case.get(opcion))


def diecisiete():
    # se inicializa la variable dia y se pide por consola
    dia = int(input('ingrese un dia'))
    # se inicializa la variable mes y se pide por consola
    mes = int(input('ingrese un mes'))
    # se inicializa la variable anio y se pide por consola
    anio = int(input('ingrese año'))
    # se asigna a la variable valida un boolean
    valida = False
    # se inicializa el diccionario case y se asigna clave y valor
    case = {1: 'enero',
            2: 'febrero',
            3: 'marzo',
            4: 'abril',
            5: 'mayo',
            6: 'junio',
            7: 'julio',
            8: 'agosto',
            9: 'septiembre',
            10: 'octubre',
            11: 'noviembre',
            12: 'diciembre'}
    # se comprueba con condiconales logicos or (O) and(Y)
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 10 or mes == 12) and (dia > 0 and dia <= 31):
        valida = True
    elif mes == 2:
        valida = True
    elif (mes == 4 or mes == 6 or mes == 8 or mes == 9 or mes == 11) and (dia > 0 and dia < 31):
        valida = True
    print('la fecha es: ', dia, ' de ', case.get(mes), ' del ', anio)


# Ejercicio 18
def dieciocho():
    # se asigna a la variable numero y se pide por consola
    numero = int(input('Ingrese un numero a evaluar '))
    # se comprueba numero
    if (numero == 0):
        print('El numero no es par e impar')
    elif numero % 2 == 0:
        print('El numero es par')
    else:
        print('El numero es impar')

# Ejercicio 19
def diecinueve():

    anio = int(input('ingrese un año'))
    esBisiesto = bool()
    esBisiesto = False
    if (anio % 4 == 0 and anio % 100 != 0):
        esBisiesto = True
    if (anio % 100 == 0 and anio % 400 == 0):
        esBisiesto = True
    if (esBisiesto == True):
        print('El año ingresado es bisiesto')
    else:
        print('El año ingresado es no bisiesto')


# Ejercicio 20
def veinte():
    tornillosConDefectos = int(input('ingrese la cantidad de tornillos defectuosos'))
    tornillosSinDefectos = int(input('ingrese la cantidad de tornillos sin defectos'))
    eficiencia = int()
    if (tornillosConDefectos < 200 and tornillosSinDefectos > 1000):
        eficiencia = 8
    if (tornillosConDefectos < 200 and tornillosSinDefectos <= 1000):
        eficiencia = 7
    if (tornillosConDefectos >= 200 and tornillosSinDefectos > 1000):
        eficiencia = 6
    if (tornillosConDefectos <= 200 and tornillosSinDefectos <= 1000):
        eficiencia = 5
    print('EL grado de eficiencia del operario es: ', eficiencia)


# Ejercicio 21
def veintiuno():
    salario = float()
    horasTrabajadas = int()
    montoPorHora = float()
    horasExtra = int()
    montoPorHoraExtra = float()
    totalVentas = float()
    comision = float()
    totalSalario = float()
    opcion = input('Ingrese [A] para calcular el salario por comision de venta \n'
                   'ingrese [B] para calcular salario mas comision \n'
                   'Ingrese [C] para calcular el salario \n:')

    def salarioPorComision():
        comision = totalVentas * 0.4
        salario = comision
        print('el salario por Comision es :', salario)

    def salarioMasComision():
        if (horasTrabajadas <= 40):
            comision = totalVentas * 0.25
            salario = horasTrabajadas * montoPorHora
            totalSalario = salario + comision
            print('El salario mas comision es: ', totalSalario)
        else:
            comision = totalVentas * 0.25
            salario = 40 * montoPorHora
            totalSalario = salario + comision
            print('El salario mas comision es: ', totalSalario)

    def salario():

        print('El salario es: ')

    case = {'a': salarioPorComision(),
            'b': salarioMasComision(),
            'c': salario()}


# Ejercicio 22
def veintidos():
    # Simulamos un bucle do while por que en python no hay con un boolean
    condicion = True
    while condicion == True:
        numero = int(input('ingrese un numero'))
        if numero < 10:
            print('numero menor a 10')
            condicion == False


# Ejercicio 23
def veintitres():
    condicion = True
    while condicion == True:
        numero = int(input('ingrese una nota'))
        if numero < 0 and numero > 10:
            print('numero mayor a 10')
            condicion == False


# Ejercicio 24
def veinticuatro():
    maximo = int()
    minimo = int()
    contador = 0
    maximo = int(input("Ingrese un numero maximo"))
    minimo = int(input("Ingrese un numero minimo"))
    condicion = True
    numero = int()
    # do
    while condicion == True:
        numero = int(input('Ingrese un numero'))

        # while
        if not ((numero > minimo) and (numero < maximo)):
            condicion = False

        # Suma la cantidad de numero ingresados
        if (numero > minimo) and (numero < maximo):
            contador += 1

    print("La cantidad de numeros ingresados entre minimo y maximo es: ", contador)


# Ejercicio 25
def veinticinco():
    condicion = True
    acumulador = 0
    maximo = int(input('ingresa el limite maximo'))
    while condicion == True:
        numero = int(input('ingresa un numero'))
        acumulador = numero + acumulador
        if acumulador >= maximo:
            condicion = False
    print('supero el limite', acumulador)


# Ejercicio 26
def veintiseis():
    condicion = True
    acumulador = 0
    promedio = float()
    cantidad = 0
    # do
    while condicion == True:
        numero = int(input('ingresa un numero'))

        if not (numero <= -1):
            acumulador = numero + acumulador
            cantidad += 1
        # while
        if numero == -1:
            condicion = False
    promedio = acumulador / cantidad
    print('el promedio es ', promedio)


def veintisiete():
    condicion = True
    nombreAlumno = ""
    notaPractica = 0
    notaTeoria = 0
    notaProblemas = 0
    notaFinal = float()
    # do
    while condicion == True:
        nombreAlumno = str(input("ingresa el nombre del alumno "))
        # while
        if len(nombreAlumno) == 0:
            print(len(nombreAlumno))
            condicion = False

        notaTeoria = int(input('nota teoria '))
        if (notaTeoria > 0) and (notaTeoria <= 10):
            notaPractica = int(input('nota practica '))
            if (notaPractica > 0) and (notaPractica <= 10):
                notaProblemas = int(input('nota resolucion de problemas '))
                if (notaProblemas > 0) and (notaProblemas <= 10):
                    notaFinal = (notaPractica * 0.10) + (notaProblemas * 0.50) + (notaTeoria * 0.40)
                    print("la nota final es ", notaFinal)
                else:
                    print("nota resolucion de problemas invalida")
            else:
                print("nota practica invalida")
        else:
            print("nota teoria invalida... Recuerde que deben ser valores entre 1 al 10 ")


# Ejercicio 28
def veintiocho():
    contador = 0
    numero = 0
    mostrador = float()
    condicion = True

    while condicion == True:
        numero = int(input('ingrese un numero para contar la cantidad de digitos'))
        if numero <= 0:
            print('Este programa solo funciona con numeros positivos, intente de nuevo')

        if numero >= 1:
            condicion = False

    mostrador = numero

    while numero >= 1:
        numero = numero / 10
        contador = contador + 1
    print('la cantidad de digitos de ', mostrador, ' es ', contador)


# Ejercicio 29
def veintinueve():
    clave = 'eureka'
    intento = 3

    # usamos la funcion range para limitar los intentos
    for i in range(4):
        claveIngresada = str(input('ingrese la contraseña')).strip()
        print('Tiene ', intento, ' intentos')
        if claveIngresada == clave:
            print('clave correcta. Bienvenido arquimedes de sicarusa')
            break
        else:
            # Si es incorrecta intento se decrementa en uno
            intento -= 1
            print('Clave incorrecta,prube otra vez')


# Ejercicio 30
def treinta():
    condicion = True
    acumulador = 0
    print('Ingresar un numero. En caso de querer terminar , escriba n/N')
    while condicion == True:
        ingreso = str(input('ingrese un numero: ')).strip()
        # creamos una condicion para saber si es numero o no con la funcion isDigit

        if ingreso.isdigit() and int(ingreso) > 0:

            acumulador = int(ingreso) + acumulador
        else:
            print('Ingrese un numero entero y positivo')

        if ingreso == 'N' or ingreso == 'n':
            condicion = False
            print('La suma de los numeros ingreasados es: ', acumulador)


# Ejercicio 31
def treintaYUno():
    numero = 0
    acumulador = 0

    numero = int(input('Ingrese la cantidad de numeros pares a sumar '))
    for i in range(numero + 1):
        acumulador = acumulador + (i * 2)

    print('La suma de los ', numero, ' primeros numeros pares es: ', acumulador)


# Ejercicio 32
def treintaYDos():
    acumulador = 0
    contador = 0
    condicion = 1
    maximo = 0
    minimo = 0
    aux = -1
    auxMinimo = 0
    print('Ingrese un numero. Para cancelar oprima 0')

    while condicion == 1:

        numero = int(input('Ingrese un numero: '))
        if numero > 0:

            if numero > maximo:
                maximo = numero

            else:
                auxMinimo = numero

                if auxMinimo >= aux:
                    aux = auxMinimo
                else:
                    minimo = auxMinimo

            acumulador = numero + acumulador

            contador += 1
        else:
            print('Finalizo el programa')
        if numero == 0:
            condicion = 0
            print('El promedio es: ', (acumulador / contador))
            print('El numero maximo es ', maximo)
            print('El numero minimo es ', minimo)


# Ejercicio 33
def treintaYTres():
    numeroAleatorio = random.randint(1, 10)
    numero = 0
    condicion = True
    print('adivine el numero aleatorio entre 1 - 10')
    while condicion == True:
        numero = int(input('Ingrese un numero'))
        if numero < numeroAleatorio:
            print('El numero es menor al aleatorio')
        else:
            print('El numero es mayor al aleatorio')
        if numero == numeroAleatorio:
            condicion = False
            print('Felicitacion a adivinado el numero ', numeroAleatorio)


# Ejercicio 34
def treintaYCcuatro():
    i = 1
    for i in range(10):
        print('El numero ', i, ' al cuadrado es ', i * i)


# Ejercicio 35
def treintaYCinco():
    contadorDos = 0
    contadorTres = 0
    # le agrego uno  al range porque sino iria del 0 - 99
    for i in range(101):
        if (i % 2) == 0:
            contadorDos += 1
        if (i % 3) == 0:
            contadorTres += 1

    print('La cantidad de numeros que son divisibles  por 2 entre 1 - 100 es: ', contadorDos)
    print('La cantidad de numeros que son divisibles  por 3 entre 1 - 100 es: ', contadorTres)


# Ejercicio 36
def treintaYSeis():
    cadena = list()
    cadenaSeparada = ''
    cadena = input('ingrese una frase: ')
    for i in range(len(cadena)):
        cadenaSeparada += cadena[i] + ' '
    #  print(cadena[i],end=" ")

    print(cadenaSeparada)


# Ejercicio 37
def treintaYSiete():
    cadena = list()
    cadena = input('ingrese una frase: ')
    cadenaSeparada = ''
    longitud = len(cadena)
    for i in range(longitud):
        cadenaSeparada += cadena[(longitud - 1) - i] + ' '
        # print(cadena[(longitud-1)-i],end=' ')

    print(cadenaSeparada)
# Ejercicio de recursion en python
# Ejercicio 1
# Calcular el valor del numero ingresado de la serie fribonacci
def ejercicioUno(numero):
    # Si se ingresa 0 y 1 son los valores iniciales
    if numero == 0:
        return 0
    # Como la serie fribonacci son la suma de los 2 numeros anteriores al numero ingresado
    if numero == 1 or numero == 2:
        return 1
    else:
        return ejercicioUno(numero - 1) + ejercicioUno(numero - 2)


# Ejercicio 2
# Sumar digitos de un numero
def sumaDeDigitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumaDeDigitos(numero // 10)


# Ejercicio 3
# Factorial de un numero
def factorial(numero):
    # caso base
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


# Ejercicio 4
# Calcular el MCD
def mcd(a, b):
    # utilizamos funcion min
    minimo = min(a, b)
    # utilizamos funcion max
    maximo = max(a, b)
    if minimo == 0:
        return maximo
    elif minimo == 1:
        return 1
    else:
        return mcd(minimo, maximo % minimo)


# Ejercicio 5
# Suma de numeros positivos hasta el numero ingresado
def sumaHastaIngresado(numero):
    # caso base
    if numero == 1:
        return 1
    # llamada recursiva
    # ejemplo: numero = 5 5+4+3+2+1=15
    else:
        return numero + sumaHastaIngresado(numero - 1)


# Ejercicio 6
# Mostrar numeros en forma decreciente desde el ingresado hasta 1
def numerosDecreciente(numero):
    # caso base
    if numero == 1:
        return 1
    else:
        # Disminuimos en 1 hasta llegar a uno
        return numerosDecreciente(numero - 1)



# Ejercicio 7
# Tabla de multiplicar
def tabla(numero, multiplicador):
    if multiplicador <= 10:
        print(numero,' * ', multiplicador,' = ', numero*multiplicador)
        return tabla(numero, multiplicador + 1)

tabla(5, 0)


# Ejercicio 8
# Recorrer lista
def recorrerlista(lista: list, indice):
    tamanio = len(lista)
    if indice == tamanio:
        return -1
    else:
        print('indice ', indice, ' valor ', lista[indice])
        return recorrerlista(lista, indice + 1)


lista = list()
lista = [1, 2, 3, 4, 5]
recorrerlista(lista, 0)


# Ejercicio 9
# Devolver la posicion en una lista
def posicionEnLista(lista: list, buscado, indice):
    if indice == len(lista) - 1:
        return -1
    elif lista[indice] == buscado:
        print(buscado,' encontrado en posicion ',indice)
        return indice
    else:
        return posicionEnLista(lista, buscado, indice + 1)


posicionEnLista(lista, 2, 0)


# Ejercicio 10
# Potencia de un numero
def potencia(base,exponente):
    if exponente == 0:
        print(base,' * ',exponente,' = ',base*exponente)
        return 1
    elif exponente == 1:
        print(base,' * ',exponente,' = ',base*exponente)
        return base
    else:
        print(base,' * ',exponente,' = ',base*exponente)
        return base * potencia(base,exponente-1)


potencia(5,3)


