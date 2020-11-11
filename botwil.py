def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n == 1:
        print(n1)
    else:
       while count < n:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
        

mtuple=('sds','dfsg','dgdg')

def function(a, *args):
    x = "-".join(args)
    print(x)
    
def factorial(n):
    fact=1
    if fact>=1:
        for i in range(1,n+1):
            fact=fact*i
    print(fact)
factorial(5)

teams=['A','B','C','D']
matches={}

for i in range(3) :
   matches[i]=str(teams[i] +'Vs' + teams[i+1])

print(matches)