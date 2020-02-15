def do_twice(f):
    f()  # executando o que for passado como parâmetro
    f()


def print_spam():
    print('spam')


do_twice(print_spam)
