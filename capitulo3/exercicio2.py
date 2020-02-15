def do_twice(funcao, valor):
    funcao(valor)  # executando o que for passado como parâmetro
    funcao(valor)


def print_algo(algo):
    print(algo)


do_twice(print_algo, 'UnsCrud')
