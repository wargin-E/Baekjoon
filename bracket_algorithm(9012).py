T=int(input())
b_list=[]
def elimination(a):
    while "(" in a and ")" in a:
        l=len(a)
        for s in range(0,len(a)-1):
            if a[s]=="(" and a[s+1]==")":
                a[s]=0
                a[s+1]=0
        while 0 in a:
            a.remove(0)
        if len(a)==l:
            break
yesorno=[]
for s in range(0,T):
    bracket=input()
    b_list.append(bracket)
for k in b_list:
    k=list(k)
    elimination(k)
    if len(k)==0:
        yesorno.append("YES")
    else:
        yesorno.append("NO")
for k in yesorno:
    print(k)


