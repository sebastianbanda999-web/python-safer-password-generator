import random
import string

longitud = int(input("Longitud de la contraseña: "))

usar_mayus = input("¿Incluir mayusculas? (Si/No): ")
usar_numeros = input("¿Incluir numeros? (Si/No): ")
usar_simbolos = input("¿Incluir simbolos? (Si/No): ")

caracteres = string.ascii_lowercase

if usar_mayus == "Si":
    caracteres += string.ascii_uppercase

if usar_numeros == "Si":
    caracteres += string.digits

if usar_simbolos == "Si":
    caracteres += string.punctuation

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Contraseña generada:", contraseña)