print('Придайте значение переменной А')
a=input()
print('Придайте значение переменной B')
b=input()
a=int(a)
b=int(b)

if(a==0 and b==0):
    print('INF')

if(a==0 and b!=0):
    print('no')

if(a!=0 and a%b!=0):
    print('no')
if (a!=0 and b==0):
    n = int(-b/a)
    print