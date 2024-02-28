'''
Ejercicios de Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''

print('Ejercico 1: Dado un número, imprime si es positivo o negativo.')
print('ingresa un numero')
number= int(input())
if number>0:
  print('Valor positivo')
elif number==0:
  print('es Cero')
else:   
  print('valor negativo')

print('#2. Ejercicio: Dado un número, imprime si es par o impar.')
print('ingresa un numero')
numero= int(input())
if numero %2 ==0:
  print('es un numero par')
else:
  print('es numero impar')
  
print('#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.')
print('ingresa un numero')
a= int(input())
print('ingresa otro un numero')
b= int(input())
print('ingresa ultimo numero')
c= int(input())
if a>b and a>c:
  print(a,'es el valor más alto')
elif b>a and b>c:
  print(b, 'es el valor mas alto')
elif c>a and c>b:
  print(c, 'es el valor más alto')
  
