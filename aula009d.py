# Divisão em strings
frase = 'Curso em Vídeo Python'
# Cada palavra da lista inicial que foi quebrada vira uma nova lista
fraseDividida = frase.split()
print(fraseDividida)
print(fraseDividida[0])
print(fraseDividida[0][1])
# Unindo as palavras cortadas adicionando '-' entre elas
print('-'.join(fraseDividida))