T=int(input())
while T:
    a=int(input())
    c=(input().split()) # take input in 1 line
    d=(input().split()) # take input in 1 line
    c.sort()  
    d.sort(reverse=True)
    dot_product=0
    for i in range(0,a):
        dot_product+=(int(c[i])*int(d[i]))
    print(dot_product)
    T-=1