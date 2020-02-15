def do_twice(funcao, valor):
    funcao(valor)  # executando o que for passado como parâmetro
    funcao(valor)


def print_algo(algo):
    print(algo)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


do_twice(print_algo, 'UnsCrud')

do_twice(print_twice, "Teste")

do_four(print_algo, "Quatro")
