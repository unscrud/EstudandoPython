# exemplo de função que precisa de um argumento
def print_2x(nome):
    print(nome)
    print(nome)


x = "Cicrano"
print_2x("UnsCrud")  # parâmetro simples
print_2x('Fulano '*4)  # expressões podem ser usadas em parâmetros
print_2x(x)  # também podemos utilizar variáveis

# a variável criada na função fica na função


def cat_twice(part1, part2):  # parâmetros só existem no corpo da função, ou seja, também são locais
    cat = part1 + part2
    print_2x(cat)


line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)
# se tentássemos chamar cat aqui teríamos um erro
