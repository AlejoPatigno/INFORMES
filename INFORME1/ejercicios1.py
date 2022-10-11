#----------- EJERCICIO 1----------

"""
Cree los siguientes rangos (tipo range()): 
   rango1 => 334, 331, 328, 325, ... 4, 1
   rango2 => 1, 3, 5, 7, 9, 11, ... 999, 1001
   rango3 => -50, -55, -60, -65, -70, ... -195, -200
Después de obtener los rangos, almacenelos de la siguiente manera:
listaDeRangos = [rango1, rango2, rango3]
"""

rango1= list(range(334,0,-3))
rango2=list(range(1,1003,2))
rango3=list(range(-50,-205,-5))

listaDeRangos = [rango1, rango2, rango3]


#------------EJERCICIO 2----------

""" 
    Seis diferentes autos realizan una carrera. 
    Cada uno de ellos empieza su recorrido en intervalos de 2 segundos
El primero de ellos inicia su recorrido y acelera a razón constante de 1.5m/s²
El segundo inicia su recorrido 2 segundos después a razón de 2 m/s². 
El tercero inicia su recorrido 4 segundos después a razón de 3 m/s². 
El cuarto inicia su recorrido 6 segundos después a razón de 3.5 m/s². 
El quinto inicia su recorrido 8 segundos después a razón de 4 m/s². 
El sexto inicia su recorrido 10 segundos después a razón de 4.5 m/s².
¿qué auto realiza el primer rebase sobre otro auto?
Almacene su respuesta en un string llamado primerRebase. Ejemplo: 
primerRebase = "Auto6-Auto3"  (auto que rebasa - auto rebasado)
"""

t=0
r=False

while r==False:
    x1=0.5*1.5*t**2
    if t>2:
        x2=0.5*2*(t-2)**2
    else: x2=0
    if t>4:
        x3=0.5*3*(t-4)**2
    else: x3=0
    if t>6:
        x4=0.5*3.5*(t-6)**2
    else: x4=0
    if t>8:
        x5=0.5*4*(t-8)**2
    else: x5=0
    if t>10:
        x6=0.5*4.5*(t-10)**2
    else: x6=0

    if x2>x1:
        primerRebase= "Auto2-Auto1"
        r= True
    elif x3>x2:
        primerRebase= "Auto3-Auto2"
        r= True
    elif x4>x3:
        primerRebase= "Auto4-Auto3"
        r= True
    elif x5>x4:
        primerRebase= "Auto5-Auto4"
        r= True
    elif x6>x5:
        primerRebase= "Auto6-Auto5"
        r= True
    else: t=t+1




#------------EJERCICIO 3 ----------

"""Los estudiantes del curso de matematicas obtuvieron las siguientes 
calificaciones definitivas (cada una de las notas equivale al 25%):
         Examen1  Examen2  Examen3  Examen4
Camila    1.0      2.3       5.0      5.0
Maria     5.0      3.5       2.5      3.2
José      2.2      4.0       3.2      4.1
Daniela   5.0      0.5       1.0      0.2
Esteban   4.0      5.0       0.0      0.0
El director del grupo preparará una salida académica, en caso de 
que se hayan cumplido las siguientes condiciones:
   * El 60% del grupo debe aprobar la materia. (se aprueba en 3.0)
   * Por lo menos dos examenes del grupo, deben tener un promedio mayor a 3.0
   * Todos los que perdieron la materia deben tenerla por encima de 2.0
¿habrá salida académica?
Almacene la respuesta en una variable denominada => salidaAcademica, cuyo valor sea un booleano
si salen => True, si no salen => False
"""
listaCamila=[1.0, 2.3, 5.0, 5.0]
listaMaria=[5.0,  3.5, 2.5, 3.2]
listaJose=[2.2, 4.0, 3.2, 4.1]
listaDaniela=[5.0, 0.5, 1.0, 0.2]
listaEsteban=[4.0, 5.0, 0.0, 0.0]

promCamila=sum(listaCamila)/4
promMaria=sum(listaMaria)/4
promJose=sum(listaJose)/4
promDaniela=sum(listaDaniela)/4
promEsteban=sum(listaEsteban)/4

i=0
k=0

if promCamila>=3.0:i=i+1   
elif promCamila>2.0: k=k+1

if promMaria>=3.0:i=i+1    
elif promMaria>2.0: k=k+1

if promJose>=3.0:i=i+1     
elif promJose>2.0: k=k+1

if promDaniela>=3.0:i=i+1  
elif promDaniela>2.0: k=k+1

if promEsteban>=3.0:i=i+1  
elif promEsteban>2.0: k=k+1

if i>=3: condicion1=True
else: condicion1=False
if k==5-i: condicion3=True
else: condicion3=False

j=0
cont=0
while cont<=3:
    promExamenes=(listaCamila[cont]+listaMaria[cont]+listaJose[cont]+listaDaniela[cont]+listaEsteban[cont])/4
    if promExamenes>3.0:
        j=j+1

    cont=cont+1
if j>=3: condicion2=True
else: condicion2=False

salidaAcademica=condicion1 and condicion2 and condicion3

print(salidaAcademica)



#------------EJERCICIO 4 ----------

""" El salario mensual de un empleado se calcula solo teniendo en cuenta el numero de seguros vendidos,
    (el precio de cada seguro es de $120000)
    Para los primeros 20 seguros vendidos, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
   El salario de 4 empleados es el siguiente:
    Empleado   Empleado1   Empleado2    Empleado3   Empleado4
    Salario   $ 7860000    $ 5520000   $ 3720000    $ 2280000
   Determine el numero de seguros vendidos por cada empleado.
   Almacene su respuesta en una lista llamada cantidadSegurosVendidos como muestra el ejemplo:
   cantidadSegurosVendidos = [10, 50, 80, 32]
"""
lista= [7860000, 5520000, 3720000, 2280000]
cantidadSegurosVendidos=[]
cont=0

while cont<=3:
    salario= lista[cont]

    algo=salario/120000

    if (algo-34)>0:
        n=((algo-34)*10)+120
    elif (algo-4)>0:
        n=((algo-4)/0.3)+ 20
    else:
        n=algo/0.2
    cont=cont+1
    cantidadSegurosVendidos.append()

print(cantidadSegurosVendidos)


#------------EJERCICIO 5 ----------

""" La calificación de una materia se encuentra en el intervalo [0.0 ,5.0] 
y se calcula tomando 4 notas, con porcentajes de 15%, 25%, 20% y 40%.
Si los estudiantes tienen las primeras 3 calificaciones definidas.
Calcule la nota4 necesaria  para aprobar la materia. (se aprueba en 3.0)
   Nombre          Nota1   Nota2  Nota3  Nota4  
Maria Gonzalez       3.1    3.1    1.2      ?
Camilo Suarez        3.2    4.0    1.1      ?
Esteban Rodriguez    3.2    4.1    2.2      ?
Mariana Rosero       5.0    5.0    5.0      ?
Jose Nuñez           5.0    4.0    2.5      ?
Esteban Quesada      3.4    4.0    2.6      ?
Mauricio Velazquez   5.0    4.2    2.1      ?
Julia Quintero       2.0    2.2    2.1      ?
Mauricio Lizcano     3.7    4.1    4.7      ?
Miguel Pineda        1.0    1.1    3.3      ?
Angie Gomez          4.1    4.7    4.4      ?
Angelica Lozano      3.1    1.0    2.6      ?
Camilo Restrepo      5.0    5.0    1.0      ?
Almacene los resultados en un diccionario llamado notasNecesarias,
cuya clave sea el nombre completo del alumno (string) y el valor
sea la nota necesaria del respectivo alumno (flotante con 2 decimales)
Ejemplo:  notasNecesarias = {"Maria Gonzalez": 3.87, "Mauricio Velazquez": 2.31, ...}
"""

lista1=["Maria Gonzalez"    ,   3.1  ,  3.1  ,  1.2]
lista2=["Camilo Suarez"     ,  3.2  ,  4.0  ,  1.1]
lista3=["Esteban Rodriguez"  , 3.2  ,  4.1  ,  2.2]
lista4=["Mariana Rosero"      , 5.0  ,  5.0  ,  5.0]
lista5=["Jose Nuñez"         ,  5.0  ,  4.0  ,  2.5]
lista6=["Esteban Quesada"     , 3.4  ,  4.0  ,  2.6]
lista7=["Mauricio Velazquez"  , 5.0  ,  4.2  ,  2.1]
lista8=["Julia Quintero"      , 2.0   , 2.2  ,  2.1]
lista9=["Mauricio Lizcano"   ,  3.7 ,   4.1  ,  4.7]
lista10=["Miguel Pineda"      ,  1.0 ,   1.1 ,   3.3]
lista11=["Angie Gomez"        ,  4.1 ,   4.7   , 4.4]
lista12=["Angelica Lozano"    ,  3.1 ,   1.0   , 2.6]
lista13=["Camilo Restrepo"    ,  5.0 ,   5.0  ,  1.0]

nota4MG=(3-(lista1[1]*0.15)-(lista1[2]*0.25)-(lista1[3]*0.2))/0.4
nota4CS=(3-(lista2[1]*0.15)-(lista2[2]*0.25)-(lista2[3]*0.2))/0.4
nota4ER=(3-(lista3[1]*0.15)-(lista3[2]*0.25)-(lista3[3]*0.2))/0.4
nota4MR=(3-(lista4[1]*0.15)-(lista4[2]*0.25)-(lista4[3]*0.2))/0.4
nota4JN=(3-(lista5[1]*0.15)-(lista5[2]*0.25)-(lista5[3]*0.2))/0.4
nota4EQ=(3-(lista6[1]*0.15)-(lista6[2]*0.25)-(lista6[3]*0.2))/0.4
nota4MV=(3-(lista7[1]*0.15)-(lista7[2]*0.25)-(lista7[3]*0.2))/0.4
nota4JQ=(3-(lista8[1]*0.15)-(lista8[2]*0.25)-(lista8[3]*0.2))/0.4
nota4ML=(3-(lista9[1]*0.15)-(lista9[2]*0.25)-(lista9[3]*0.2))/0.4
nota4MP=(3-(lista10[1]*0.15)-(lista10[2]*0.25)-(lista10[3]*0.2))/0.4
nota4AG=(3-(lista11[1]*0.15)-(lista11[2]*0.25)-(lista11[3]*0.2))/0.4
nota4AL=(3-(lista12[1]*0.15)-(lista12[2]*0.25)-(lista12[3]*0.2))/0.4
nota4CR=(3-(lista13[1]*0.15)-(lista13[2]*0.25)-(lista13[3]*0.2))/0.4

notasNecesarias={lista1[0]:round(nota4MG,ndigits=2), lista2[0]:round(nota4CS,ndigits=2), lista3[0]:round(nota4ER,ndigits=2), lista4[0]:round(nota4MR,ndigits=2), lista5[0]:round(nota4JN,ndigits=2), lista6[0]:round(nota4EQ,ndigits=2), lista7[0]:round(nota4MV,ndigits=2), lista8[0]:round(nota4JQ,ndigits=2), lista9[0]:round(nota4ML,ndigits=2), lista10[0]:round(nota4MP,ndigits=2), lista11[0]:round(nota4AG,ndigits=2), lista12[0]:round(nota4AL,ndigits=2), lista13[0]:round(nota4CR,ndigits=2)}
