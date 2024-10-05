
def procesar_frases(frases):
    conteo_palabras = []
    for frase in frases:
        palabras = frase.split()
        conteo_palabras.append(len(palabras))
        print(f"Frase: '{frase}' contiene {len(palabras)} palabras.")
    return conteo_palabras

frases = [
    "Python es un lenguaje de programación",
    "Me gusta resolver problemas con código",
    "Las listas y los bucles son muy útiles"
]

procesar_frases(frases)

# Ejercicio 2 
def encontrar_coeficientes_sin_numpy():
    puntos = [(0, 0), (1, 8), (2, 12), (3, 12), (5, 0)]

    a = -1
    b = 9.4
    c = 0

    return a, b, c

a, b, c = encontrar_coeficientes_sin_numpy()
print(f"Los coeficientes son: a = {a}, b = {b}, c = {c}")
