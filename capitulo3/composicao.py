import math
# compondo funções - o argumento de uma função pode ser qualquer tipo de expressão, inclusive operadores aritméticos
degrees = 90
x = math.sin(degrees / 360 * 2 * math.pi)
print(x)
# E até chamadas de função:
x = math.exp(math.log(x+1))
print(x)
# também podemos criar as nossas funções
# Logo abaixo temos um cabeçalho que precisa terminar em dois pontos


def print_lyrics():  # criando uma função que não recebe parâmetros
    print("I,m a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    # a indentação (padrão de 4 espaços) que vai definir
    #  o corpo da função ou de um sub-bloco


''' REGRAS PARA NOMEAR FUNÇÕES
são as mesmas que as das variáveis:
letras, números e sublinhado são legais, 
 mas o primeiro caractere não pode ser um número.
 Não podemos usar uma palavra-chave como nome de
 uma função e devemos evitar ter uma variável e 
 uma função com o mesmo nome.
 '''

# ao criar uma função no interpretador, ... será exibido até
# uma linha em branco sinalizar o fim do corpo da função

# a definição da função cria um objeto do tipo function
print(type(print_lyrics))

# chamando a nova função
print_lyrics()

# podemos chamar nossa função dentro de outra


def repeat_lirics():
    print_lyrics()
    print_lyrics()
    print_lyrics()


repeat_lirics()
