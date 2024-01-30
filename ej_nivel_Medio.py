
print("1: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.")
def fibb(n):
  a, b =0, 1
  for i in range(n):
    print (a)
    a, b =b, a+b

n=int(input("introduzca el N-esimop valor de la serie Fibb: "))
fibb(n)

print("Define una función que tome un número y retorne una lista de sus divisores")
def divisores (numero):
  num_divisores=[]
  for i in range (1, numero + 1):
    if numero % i == 0:
      #print(i)
      num_divisores.append(i)
  return num_divisores
  print(num_divisores)

numero=int(input("introduzca el número a conocer los divisores: "))
print(divisores(numero))

print("Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista origina")

def elem_unicos(listas):
  return list(set(listas))

listas=[1,2,"hola", 1, 2, 3,"hola", 1,2]
print(elem_unicos(listas))

print("define una función que tome una cadena y cuente el número de vocales en la cadena")
def vocales(cadena):
  vocal=["a","e","i","o","u"]
  k=0
  for i in range(len(cadena)):
    if cadena [i] in vocal:
      k=k+1
  return k

cadena="hipopotamo"
print(vocales(cadena))

print("Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista")
def truncar(lista,n):
  lista_temp=[]
  for i in range(len(lista)):
    if n>i:
      lista_temp.append(lista[i])
  return lista_temp

lista=[1,2,3,4,5,6,7,8,9,10]
n=4
print(truncar(lista,n))

print("Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena")
def may_min(cadena):
  mayusculas=[]
  minusculas=[]
  j=0
  k=0
  for i in range(len(cadena)):
    if cadena[i].islower() :
      minusculas.append(cadena[i])
      j=j+1
    elif cadena[i].isupper():
      mayusculas.append(cadena[i])
      k=k+1
  return j, k

cadena="CaRaDepErRo"
print(may_min(cadena))

print("Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario.")
def num_perfecto(numero):
  num_divisores=[]
  k=0
  for i in range (1, numero):
    if numero % i == 0:
      #print(i)
      num_divisores.append(i)
  for i in range(len(num_divisores)):
    k=k+num_divisores[i]
    #print(k)
  if k==numero:
    return True
  else:
    return False

numero=int(input("Introducir un numero para comprobar si es perfecto"))
print(num_perfecto(numero))

print("Define una función que reciba un número y retorne su representación en binario")
def conv_binario(num_decimal):
  binario = ""
  while num_decimal > 0:
    res = num_decimal % 2
    binario = str(res) + binario
    num_decimal //= 2
  return binario

num_decimal=int(input("introducir el número a pasar a binario: "))
print(conv_binario(num_decimal))

print("Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).")
def interseccion(lista1, lista2):
    return list(set(lista1) & set(lista2))

lista1 =[1,2,3,4,5]
lista2= [2,3,4,5,6]
print(interseccion(lista1, lista2))
''
print("Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)")
def es_palindromo(palabra):
  inversa=palabra[::-1]
  #return inversa
  if inversa==palabra:
    return True
  else:
    return False

palabra=str(input("introducir la palabra: "))
print(es_palindromo(palabra))

print("Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”")
a=0
for i in range(1, 50):
  if i %3==0 and i%5==0:
    print(i, "Fizzbuzz")
  elif i%3==0:
    print (i, "Fizz")
  elif i%5==0:
    print(i, "buzz")
  else:
    print(i)

print("Define una función que tome una lista y retorne la lista ordenada en orden ascendente")
def ordenar_lista(list):
  #return sorted(lista)
  n=len(lista)
  for i in range(n):
    for j in  range(0, n-i-1):
      if lista[j]>lista[j+1]:
        #print (i)
        #print(j)
        lista[j], lista[j+1]=lista[j+1], lista[j]
  return lista

lista=[4,3,6,2,6,9,2,7,2,7,9]
print(ordenar_lista(lista))

print("Define una función que reciba una lista de palabras y un entero n, retorne la lista de palabras que son más largas que n")
def palabras_largas(lista,n):
  lista_n=[]
  for palabra in lista:
    if len(palabra)>n:
      lista_n.append(palabra)
  return lista_n

lista=['hola','mundo','gato','hipopotamo','toro']
n=int(input("introduicir el numero: "))
print(palabras_largas(lista,n))

print("Define una función que tome un número y calcule su serie de Fibonacci")
def fib(n):
  a=0
  b=1
  for j in range(0, n):
    c=a+b
    a=b
    b=c
  return c+b

num=int(input("introducir numero: "))
print(fib(num))

print("Define una función que tome una lista de números y retorne el número más grande de la lista")
def mlista(liste):
  mayor=0
  #L=[]
  for i in range(len(liste)):
    if liste[i]>mayor:
      mayor=liste[i]
  return mayor

liste=[1,3,5,7,9,4,3]
print(mlista(liste))

print("Define una función que reciba un número y retorne la suma de sus dígitos al cubo")
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)**3
        #print(suma)
    return suma

n=87
print(suma_digitos(n))

print("Define una función que reciba una lista de números y retorne el segundo número más grande de la lista")
def segundo_mayor(lista):
  #return sorted(lista)
  n=len(lista)
  nlista=[]
  for i in range(n):
    for j in range(0, n-i-1):
      if lista[j]>lista[j+1]:
        #print (i)
        #print(j)
        lista[j], lista[j+1]=lista[j+1], lista[j]
  nlista=sorted(set(lista), reverse=True)
  return nlista[1]

lista=[1,3,6,2,6,9,2,7,2,7,9]
print(segundo_mayor(lista))

print("Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.")
def comparar_listas(lista1, lista2):
  lista1a=sorted(set(lista1))
  lista2a=sorted(set(lista2))
  n1=len(lista1a)
  n2=len(lista2a)
  n3=min(n1,n2)
  #print(n3)
  for i in range(n3):
    if lista1a[i]==lista2a[i]:
      print(lista1a[i])
    return True
  return False

lista1=[1,2,3,4,5,6,7,8,9]
lista2=[3,5,7,2,7,2,2,7,4]

print(comparar_listas(lista1,lista2))

print("Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.")
def orden_inverso(lista):
  lista1=sorted(lista, reverse=True)
  print(lista1)

lista1=[3,5,7,2,7,2,2,7,4]
#print(orden_inverso(lista1))
orden_inverso(lista1)

print("Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene")
def contar_digitos(cadena):
  r=0
  for digitos in cadena:
    r=r+1
    #print(digitos)
  return r

s="hola es una cadena"
print(contar_digitos(s))

print("Define una función que reciba una lista de números y retorne la suma acumulada de los números")
def suma_acum(lista):
  r=0
  for i in lista:
    r=int(i)+r
  return r

lista=[2,12,4,56,7]
print(suma_acum(lista))

print("Define una función que encuentre el elemento más común en una lista")
def mas_comun(lista):
  item_max=None
  max_count=0
  for i in lista:
    count=lista.count(i)
    #print(i)
    if count > max_count:
      max_count=count
      item_max= i
      #print(max_count)
      #print(i)
  return item_max

lista=[1,1,1,1,1,1,2,34,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9]
print(mas_comun(lista))

print("Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10")
def tabla_de_multiplicar(n):
  for i in range(1,11):
    print({i:n*i})
    #return {i: n * i for i in range(1, 11)}
    #es otra manera de hacerlo, pero creo que es mejor como digo yo
n=5
print(tabla_de_multiplicar(n))

print("Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena")
def contar_caracteres(cadena):
  cadena2=sorted(cadena)
  conteo={}
  for caracter in cadena2:
    conteo[caracter]= cadena2.count(caracter)
  return conteo

cadena="buenos dias gente de bien"
print(contar_caracteres(cadena))

print("Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas")
def no_esta(lista1, lista2):
  resultado=[]

  for elemento in lista1:
    if elemento not in lista2:
      resultado.append(elemento)
  for elemento in lista2:
    if elemento not in lista1:
      resultado.append(elemento)
  return resultado

lista1 = [7,1,3,4,5,6]
lista2 = [1,2,4,5,6]
print(no_esta(lista1, lista2))

print("Define una función que tome una lista y retorne la lista sin duplicados")
def sin_duplicaos(lista):
  lista2=list(set(lista))
  return lista2

lista=[1,2,2,2,2,3,3,3,3,4,4,4,4,4,4]
print(sin_duplicaos(lista))

print("Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número")
def operacion(num):
  op=0
  for i in range(num):
    if i%2 ==0:
     op += i**2
  return op

n=int(input("introducir numero: "))
print(operacion(n))

print("Define una función que reciba una lista de números y retorne el promedio de los números en la lista")
def promedio(lista):
  prom=0
  n=0
  suma=0
  for elemento in lista:
    suma=suma+elemento
    n=n+1
  return suma/n

lista=[2,4,6,8]
print(promedio(lista))

print("30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista")
def cadena_larga(lista):
  res=""
  for cadena in lista:
    if len(cadena)>len(res):
      res=cadena
  return res

lista=["hola", "tos", "hipopotamo","kiliki"] 
print(cadena_larga(lista))

print("31. Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.")
def primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primos.append(num)
        num += 1
    return primos

n=int(input("introducir un número: "))
print(primos(n))

print("32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso")
def reverse_cadena(cadena):
  inv=""
  for i in cadena:
    inv=i+inv
  return inv

cadena="hola mundo"
print(reverse_cadena(cadena))

print( "33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla" )
def sort_tuples(datos):
    return sorted(datos, key=lambda x: x[-1])

datos = [ (3, 1), (2, 3), (3, 2), (1, 2), (4, 1), (4,2), (3,3)]
print(sort_tuples(datos))
#este lo he tenido que buscar por que no era capaz de sacarlo. 

print("34: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena")
def num_vocales(cadena):
  vocales=("a","e","i","o","u")
  n=0
  for i in cadena:
    if i in vocales:
      n+=1
  return n

cadena=("hola me llamo pepito")
print(num_vocales(cadena))

print("35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne Fals")
def entero (nu):
  esprimo=True
  for i in range (2,nu):
    if nu%i==0:
      esprimo=False
      break
  return esprimo

nu=int(input("introducir numero: "))
print(entero(nu))