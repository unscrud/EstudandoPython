import math


def print_twice(val):
    print(val)
    print(val)


radians = 1
# exemplos de função com resultado
# o retorno deve ser usado ou atribuido para que não se perca
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
print(x)
print(golden)

# funções nulas não tem retorno
result = print_twice('oi')
print(result)  # retornará um tipo especial
print(type(result))  # um NoneType
