import random
import string

tamanho =int(input("Tamanho da Senha: "))

Caracteres = string.ascii_letters + string.digits + string.punctuation

senha =""

for i in range(tamanho):
    senha += random.choice(Caracteres)

print("Senha gerada: ", senha)