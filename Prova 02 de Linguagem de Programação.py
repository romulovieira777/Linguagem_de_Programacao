#Prova 02 de Linguagem de Programação

#Operações aritméticas
'''
import math
n = float(input())
print('i)',n**2)
print('ii)',n**math.e)
print('iii)',math.sqrt(n))
print('iv)',n**(1/3))
print('v)',n**(1/n))
print('vi)',math.e*n)
print('vii)',math.pi/n)
print('viii)',math.log(n,7))
print('ix)',math.log(n,math.e))
print('x)',math.log(n,math.pi))
'''

#Expressões aritméticas
'''
import math
a = float(input())
b = float(input())
c = float(input())
d = float(input())
soma = (a+b+c+d)
mult = (a*b*c*d)
n1 = ((a**2)+3*b)/c+d
n2 = (math.log(a,10)+math.e**(-b/c))-(d**2/math.pi)
n3 = ((a**2)**(1/3)*b**(1/3)+(c*d))/(soma)
n4 = (a+b)*(c+d)/mult
n5 = ((a**2)+(b**2))/(c*d)-((c**2)+(d**2))/(a*b)
n6 = soma**2
n7 = (a**2)+(b**2)+(c**2)+(d**2)
n8 = mult**(1/3)

print('i)',round(float(n1),4))
print('ii)',round(float(n2),4))
print('iii)',round(float(n3),4))
print('iv)',round(float(n4),4))
print('v)',round(float(n5),4))
print('vi)',round(float(n6),4))
print('vii)',round(float(n7),4))
print('viii)',round(float(n8),4))
'''

#loja de tintas
'''
import math
a = float(input())
r = 7
lata = 24
ga = 5.4
p1 = float(91.00)
pg = float(23.00)
qt = a/r
t1 = math.ceil(qt/lata)
v1 = p1*t1
print('a) {} lata(s) de 24 litros: R$ {:.2f}'.format(t1,v1))

tg = math.ceil(qt/ga)
vg = pg*tg
print('b) {} lata(s) de 5.4 litros: R$ {:.2f}' .format(tg,vg))

ge1 = qt//lata
geg = math.ceil((qt%lata)/ga)
vge = ge1*p1+geg*pg
print('c)',int(ge1),'lata(s) de 24 litros e', int(geg),'lata(s) de 5.4 litros: R$ {:.2f}'.format(vge))
'''



























      
