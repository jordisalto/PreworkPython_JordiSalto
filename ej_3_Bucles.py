'''
Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''

print('Ejercicio1: Imprime los números del 1 al 10 usando un bucle for')
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
  print(num)
  num += 1
  
print('Ejercicio2: Imprime los números pares del 1 al 20 usando un bucle while')
num=1
while num<=20:
  if num%2==0:
    print(num)
  num +=1
  
print('Ejercicio3: Usa un bucle para calcular la suma de los números del 1 al 100')
i=1 
j=0
while i<=100:
  j=j+i
  i +=1
print(j)
  
  