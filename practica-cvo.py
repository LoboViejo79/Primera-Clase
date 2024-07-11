# enteros
entero = 543
print(entero)

# float - decimal
decimal = 0.43
print(decimal)

# string
cadena = "Info 2024-07-11"
cadena1 = 'Info 2024-07-11'
cadena2 = """DOCSTRING"""
cadena3 = '''DOCSTRING'''
print(cadena)

# boolean
verdadero = True
falso = False
print(verdadero)
print(falso)

#vacio, null , nulo, None, nil
vacio = None
print(vacio)

#funcion type(), que tipo de dato tiene dentro
print(type(vacio))

## Tipo de datos estructurados /complejos
#list "tiene la caracteristica de poder creecer es variable  mutables"

lista = [1,2,3,4,5,6,7,8, "algo"] # 9 elemento. Indice empieza en 0.
print(lista)
print(lista[3])
lista_lista = [[3,2,1,], [7,6,5],[10,11,13]]
print(lista_lista[2][1]) #cuenta desde 0 en este caso estariamos imprimiendo  la lista 2 el numero 11



#tuplas "no puden crecer y no son variable son inmutables"
tuplas = (3,2,1,2,2,2)

#set "la caracteristica mas importante que tiene es un conjunto de datos no repetido"
conjuntos = {1,2,3,4,5,6,7,8,9,'123','123','123',5,5,5,5,5 } #la idea es buscar todo y agrupar y ordena
print(conjuntos)


#diccionarios, map " se manejan por  un tipod de estructura clave valor, key-value  mutables"
#Ejemplo 1:
#diccionarios = {'llave':'valor',1:'uno'}
#print(diccionarios[1])

#Ejemplo 2
Provincias = {'Chaco':'resistencia','Corrientes':'corrientes'}
print(Provincias['Chaco'])

#Ejemplo 3 # en este ejmplo estamos listando las ciudades del chaco
Ciudades = {'Chaco':['San Martin','Fontana','Barranqueras'], 'Corrientes':['Empedrado','Goya','Bella Vista']}
print(Ciudades['Chaco'])


#definidos por el progrador, librerias, dataframe(df)