import numpy as np

# Crear una matriz de 2x4
matriz = np.array([[10, 5, 8, 12],
                   [3, 15, 6, 9]])

# Modificar el elemento de la fila 1 columna 0 a 10
matriz[1, 0] = 10

# Sustituir la fila 0 con los valores (10, 20, 30, 40)
matriz[0, :] = [10, 20, 30, 40]

# Obtener el tamaño de la matriz
tamano = matriz.size

# Obtener la forma de la matriz (filas, columnas)
forma = matriz.shape

# Obtener el valor máximo, mínimo y la media de la matriz
maximo = np.max(matriz)
minimo = np.min(matriz)
media = np.mean(matriz)

# Mostrar toda la información en pantalla
print("Matriz modificada:")
print(matriz)

print("\nTamaño de la matriz:", tamano)
print("Forma de la matriz:", forma)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
print("Media:", media)

# --------------------------------------------------------------------------------------------------


# Crear una nueva matriz de 2x2
matriz_original = np.array([[2, 4],
                            [6, 8]])

# Convertir la matriz en un vector utilizando flatten()
vector = matriz_original.flatten()

# Mostrar el vector resultante en pantalla
print("Matriz original:")
print(matriz_original)

print("\nVector resultante:")
print(vector)

# Crear dos matrices para multiplicación y suma
matriz_a = np.array([[1, 2],
                     [3, 4]])

matriz_b = np.array([[2, 0],
                     [1, 3]])

# Realizar la multiplicación entre las matrices
producto = np.dot(matriz_a, matriz_b)

# Realizar la suma entre las matrices
suma = matriz_a + matriz_b

# Mostrar los resultados de multiplicación y suma en pantalla
print("\nMatriz A:")
print(matriz_a)

print("\nMatriz B:")
print(matriz_b)

print("\nResultado de la multiplicación:")
print(producto)

print("\nResultado de la suma:")
print(suma)
