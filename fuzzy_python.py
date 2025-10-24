import random

# ------------------------------
# 1. INCERTIDUMBRE Y PROBABILIDAD
# ------------------------------
print("=== INCERTIDUMBRE Y PROBABILIDAD ===")
# Simular 10 tiradas de un dado
tiradas = [random.randint(1, 6) for _ in range(10)]
print("Tiradas:", tiradas)

# Calcular probabilidad de obtener un numero mayor a 4
exitos = sum(1 for t in tiradas if t > 4)
probabilidad = exitos / len(tiradas)
print(f"Veces que salio >4: {exitos}")
print(f"Probabilidad estimada: {probabilidad:.2f}\n")

# ------------------------------
# 2. FUNCIONES DE PERTENENCIA
# ------------------------------
print("=== FUNCIONES DE PERTENENCIA ===")
def triangular(x, a, b, c):
    """
    Funcion de pertenencia triangular.
    a: inicio de la base
    b: punto maximo (grado 1)
    c: fin de la base
    """
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    else:
        return 0

# Ejemplo: temperatura calida en [15, 25, 35]
temperatura = 25
grado = triangular(temperatura, 15, 25, 35)
print(f"Grado de pertenencia de {temperatura}C a 'calida': {grado:.2f}\n")

# ------------------------------
# 3. DEFUZIFICACION POR CENTROIDE
# ------------------------------
print("=== DEFUZIFICACION (CENTROIDE) ===")
# Valores y sus grados de pertenencia
valores = [10, 20, 30]
grados = [0.2, 0.5, 0.8]

# Formula del centroide: (sum(mu*x) / sum(mu))
numerador = sum(mu * x for mu, x in zip(grados, valores))
denominador = sum(grados)
centroide = numerador / denominador

print("Valores:", valores)
print("Grados de pertenencia:", grados)
print(f"Valor defuzificado (centroide): {centroide:.2f}")
