print("escribe una frase porfavor:")

frase = []
frase = input()
print(frase.split())

for l in frase:
    print(l.upper())
else:
    print("se recorrio el arreglo")
print("Que palabra quieres contar en la frase?")
palabra = input()
print("la palabra", palabra, "se repite", frase.count(palabra), "veces")
print("Que palabra quieres remplazar en la frase?")
palabra = input()
print("por cual palabra la quieres remplazar?")
palabra2 = input()
print("la nueva frase es:", frase.replace(palabra, palabra2))