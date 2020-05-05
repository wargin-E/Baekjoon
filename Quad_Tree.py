
from math import sqrt
n=int(input())
def distinguish(a):
    if len(a)==1:
        return int(a[0])
    elif "0" not in a:
        return 1
    elif "1" not in a:
        return 0
    else:
        return -1
def simplify(a,answer):
    if distinguish(a)!=-1:
        if distinguish(a)==0:
            answer[0]=answer[0]+1
        elif distinguish(a)==1:
            answer[1]=answer[1]+1
        return answer
    elif distinguish(a)==-1:
        quarter_one=[]
        quarter_two=[]
        quarter_three=[]
        quarter_four=[]
        n=int(sqrt(len(a)))
        for y in range(0,int(n/2)):
            for x in range(0,int(n/2)):
                quarter_one.append(a[int(y*n+x)])
        for y in range(0,int(n/2)):
            for x in range(int(n/2),n):
                quarter_two.append(a[int(y*n+x)])
        for y in range(int(n/2),n):
            for x in range(0,int(n/2)):
                quarter_three.append(a[int(y*n)+x])
        for y in range(int(n/2),n):
            for x in range(int(n/2),n):
                quarter_four.append(a[int(y*n)+x])
        answer=simplify(quarter_one,answer)
        answer=simplify(quarter_two,answer)
        answer=simplify(quarter_three,answer)
        answer=simplify(quarter_four,answer)
        return answer
total=[]
two_dimention=[]
answer=[0,0]
for k in range(0,n):
    a=input().split(" ")
    two_dimention.append(a)
for k in two_dimention:
    for s in k:
        total.append(s)
answer=simplify(total,answer)
print(answer[0])
print(answer[1])


