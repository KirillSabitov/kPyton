n=int(input('Введите колво детей'))
m=int(input('Введите колво взрослых'))
k=int(input('Введите колво мест'))
v=int(2)
d=int(k-v)
ad=int(n/(k-2))
if n%(k-2)!=0:
    n//(k-2)+1
if k<3:
    print('0')
elif m/2<ad:
    print('0')
else:
    print(ad)