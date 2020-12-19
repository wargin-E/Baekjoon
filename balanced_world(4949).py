sentences=[]
simple_sentences=[]
answers=[]
brackets=["(",")","[","]"]
while True:
    k=input()
    if k==".":
        break
    else:
        sentences.append(k)
for k in sentences:
    k=list(k)
    for a in range(0,len(k)):
        if k[a] not in brackets:
            k[a]=0
    while 0 in k:
        k.remove(0)
    simple_sentences.append(k)
def terminate(k):
    for s in range(0,len(k)-1):
        if k[s]=="[" and k[s+1]=="]":
            k[s]=0
            k[s+1]=0
        elif k[s]=="(" and k[s+1]==")":
            k[s]=0
            k[s+1]=0
    while 0 in k:
        k.remove(0)
for k in simple_sentences:
    while True:
        if len(k)==0 or len(k)==1:
            break
        l=len(k)
        terminate(k)
        if l==len(k):
            break
for k in simple_sentences:
    if len(k)==0:
        print("yes")
    else:
        print("no")




