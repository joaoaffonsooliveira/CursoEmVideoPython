# Dissecando uma variável
n = input('Digite algo: ')
print(f'''O tipo primitivo da palavra "{n}" é: {type(n)}''')
print(f'''Há espaços em "{n}"? {n.isspace()}''')
print(f'''"{n}" é um número? {n.isnumeric()}''')
print(f'''"{n}" é alfabético? {n.isalpha()}''')
print(f'''"{n}" é alfanumérico? {n.isalnum()}''')
print(f'''"{n}" está em maiúscula? {n.isupper()}''')
print(f'''"{n}" está em minúsculas? {n.islower()}''')
print(f'''{n} está capitalizada? {n.istitle()}''')