print('O exercício 2.1 tem como objetivo a realização de pequenos testes ')
print('Por exemplo, n = 42 funciona e 42 = n não.')
print('É mostrado também que o ; pode ser usado no fim das instruções, mas um ponto . não pode')
print('')
print('Também é mostrado que se colocarmos duas variáveis juntas no intúito de multiplicá-las teremos uma exception.')
print('Exemplo:')
print('a = 2')
print('b = 3')
print('a * b terá 6 como resultado e ab seria uma nova variável que ainda não foi definida, logo causará uma exception.')
print('')

print('Agora no exercício 2.2 serão executadas algumas operações matemáticas:')
print('')
print('1º volume de uma esfera de raio 5:')
pi = 3.14
r = 5
numerador = 4*pi*r**3
print(numerador/3)
print('')

print('2º Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?')
livro = 24.95
livro_com_desconto = livro * 0.6
valor_primeiro = livro_com_desconto + 3
valor_demais = (livro_com_desconto + 0.75)*59
valor_total = valor_primeiro + valor_demais
print('Valor atacado de 60 cópias:')
print(valor_total)
print('')
print('3º Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?')
tempo_oito = 2*(8*60+15)
tempo_sete = 3*(7*60+12)
tempo_total_segundos = tempo_oito + tempo_sete
tempo_minutos = tempo_total_segundos / 60
resto = tempo_total_segundos % 60
print(tempo_minutos)
print('Saindo 6:52 + 38 minutos = chegará as 7:30')
