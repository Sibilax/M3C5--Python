#Cree un bucle For de Python.

rango = range(1,11)

for num in rango:
  print(f'Este es el número: {num}')

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(a,b,c):
  return a + b + c

print(suma(1,2,3))

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda a,b,c : a + b + c
resultado = suma (1,2,3)

print(resultado)

"""Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
*Sugerencia, si es necesario, utilice un bucle for in y el operador in."""


nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for element in lista_nombre:
  if element == nombre:
    print(f'{element}: coincide.')
  else:
    print(f'{element}: no coincide.')