
import math
def F(x):
    return x**4-4*x-1

def dih(f,a,b,eps):
        while (abs((b - a) / 2) > eps):
            c = (a + b) / 2
            if f(a) * f(c) > 0:
                a = c
            else:
                b = c
        return c
        
def hord(f,a,b,eps):
    z = 100
    while(abs(f(b)-f(a))>eps and z !=0):
        c = (f(b)*a-f(a)*b)/(f(b)-f(a))
        z=z-1
        if((f(a)*f(c))>0):
            a=c
        else:
            b=c
    return c

print("Введите начало отрезка:")
a=float(input())
print("Введите конец отрезка:")
b=float(input())
print("Введите точность:")
eps=float(input())
kordih=dih(F,a,b,eps)
print("Корень уравнения найденный методом дихотомии:")
print(kordih)
if (F(a)*F(b) > 0 and F(a) != F(b)):
    print("Корней находимых методом хорд нет на данном отрезке")
else:
    korhor=hord(F,a,b,eps)
    print("Корень уравнения найденный методом хорд:")
    print(korhor)

