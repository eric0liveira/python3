'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula: MaiorAB = (a + b + abs(a - b)) / 2

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior_ab = int((a + b + abs(a - b)) / 2)
maior_abc = int((maior_ab + c + abs(maior_ab - c)) / 2)

print(maior_abc, "eh o maior")