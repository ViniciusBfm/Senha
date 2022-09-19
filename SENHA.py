# Há diferença entre letras maiusculas e minusculas

# Palavra de base: SECURITY
"""
SECURITY = Chave
5ECURITY = Senha

1 = 1 
2 = 2....
9 = 9
10 = A
11 = B...
"""
chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave: 
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "11"
    elif letra in "Cc": senha = senha + "3"
    elif letra in "Dd": senha = senha + "13"
    elif letra in "Ee": senha = senha + "7"
    elif letra in "Ff": senha = senha + "15"
    elif letra in "Ss": senha = senha + "@"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Nn": senha = senha + "$"
    elif letra in "Mm": senha = senha + "%"
    else: senha: senha + letra
print(senha)