'''''N1 = input('digite seu nome:')
N2 = input('digite seu sobrenome:')

print('seu nome é', N1,'e seu sobrenome é', N2)

______________________________________________

n = int(input('Digite um Numero:'))

if n > 10:
    print("O numero é maior que 10.")
elif n == 10:
   print("O número é exatamente 10.")
else:
    print("O numero é menor que 10.")
    
____________________________________________

N = int(input('Digite sua idade:'))

if N <= 17:
    print('Você é Adolecente!!')
elif N < 13:
    print('Você é Criança!!')
else:
    print('Você é Adulto!!')

_______________________________________________

n = int(input('Digite um numero de 0 a 10:'))

if n == 10:
    print("O numero é 10")
elif n < 10:
    print("o numero e menor que 9")

___________________________________________


a = 5
b = 10

if a == b:
    print('A é igual a B')
elif a != b:
    print('A é diferente de B')

if a > b:
    print('A é maior que B')
elif a < b:
    print('A é menor que B')

if a <= b:
    print('A é menor ou igual a B')
elif a >= b:
    print('A é maior ou igual a B')

________________________________________________
'''''

nota = 10

if nota == 100:
    print("A+")
elif nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")