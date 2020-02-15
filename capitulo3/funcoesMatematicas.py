import math  # importa o módulo de funções matemáticas
math  # chamando o nome do modulo para ver informações dele
# agora chamaremos as funções e variáveis do módulo
signal_power = 110
noise_power = 2
ratio = signal_power / noise_power
print(ratio)
'''
Para acessar uma das funções, 
é preciso especificar o 
nome do módulo e o nome da função, 
separados por um ponto
'''
decibels = 10 * math.log10(ratio)
print(decibels)
radians = 0.7
print(radians)
# Este formato é chamado de notação de ponto.
height = math.sin(radians)  # temos também cos, tan...
print(height)

# convertendo graus em radianos
degrees = 45
radians = degrees / 180 * math.pi
print(radians)
print(math.sin(radians))

# comparando os resultados
print(math.sqrt(2)/2)

# mostrando o valor de pi do modulo matemático
print(math.pi)
