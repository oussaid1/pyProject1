
def ex1():
    file = open('books.txt', 'r')
    tous = file.readlines()
    for a in range(len(tous)):
        x = tous[a]
        l = len(x)-1
        if a+1 == len(tous):
             l=len(x)
        d=str(x[0])+str(l)
        print(d)

def grandMot(t):
    lalist=t.split()
    s=[]
    j={}
    for a in lalist:
        s.append(len(a))
        j[len(a)]=a
    print(j)
    return str(j.get(max(s)))

#print(grandMot('this ilöts my new day her t'))
for i in range(10):
    try:
        if 10/i==2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)