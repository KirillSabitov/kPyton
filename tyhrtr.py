#pr1 = 42
#pr2 =pr1
#pr1 =100
#print(pr1)
#print(pr2)

#pr3 =[1,2,3,4,5,6,7,8,9]
#pr4 = pr3
#pr3[1] = 'привет'
#print(pr3)
#print(pr4)
def primer(p1,p2,p3,p4,p5,p6):
    return(p1 and p2 and p3) or (p4 and p5 and p6)

print(primer(True,True,True,True,False,True))

