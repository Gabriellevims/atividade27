# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 
palavra= str(input("Digite a palavra:"))
palavra = palavra.lower().replace(" ","")

palavra2= palavra.lower()[::-1]
palavra2= palavra.replace(" ", "")

if palavra == palavra2:
    print(" A palavra é palíndromo")
else:
    print(" A palavra não é palíndromo")