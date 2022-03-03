# Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name']='Bryant'
print(estudiantes[0]['last_name'])
# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0]="Andrés"
print(directorio_deportes)
# Cambia el valor 20 en z a 30.
z[0]['y']=30
print(z)
##################
# Iterar a través de una lista de diccionarios
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(estudiantes):
    for i in estudiantes:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

#para diccionarios
# for key,valor in diccionario.items():
    
# for key in diccionario:
#     diccionario.get(key,"mensaje si no hay")
    


iterateDictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(f"{i[key_name]}")

iterateDictionary2('first_name',estudiantes)
iterateDictionary2('last_name', estudiantes)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    
    for i in dojo:
        print("----------")
        print(len(dojo[i]),i.upper())
        for j in range(len(dojo[i])):
            print(dojo[i][j])
        print("----------")
printInfo(dojo)
'''
# salida:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''