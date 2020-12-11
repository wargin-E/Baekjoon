k=int(input())
num_list=[]
for s in range(0,k):
    i=int(input())
    num_list.append(i)
    if i==0:
        num_list.pop()
        num_list.pop()
sum=0
for k in num_list:
    sum=sum+k
print(sum)
