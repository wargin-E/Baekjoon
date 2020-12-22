N=int(input())
brute_force=[]
sdij=[]
difference_list=[]
for k in range(0,N):
    sdij.append(input().split(" "))
if N==4:
    brute_force=[[1,2],[1,3],[1,4]]
    for k in brute_force:
        all=[1,2,3,4]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==6:
    for a in range(2,6):
        for b in range(a+1,7):
            k=[1]
            k.append(a)
            k.append(b)
            brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==8:
    for a in range(2,7):
        for b in range(a+1,8):
            for c in range(b+1,9):
                k=[1]
                k.append(a)
                k.append(b)
                k.append(c)
                brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==10:
    for a in range(2,8):
        for b in range(a+1,9):
            for c in range(b+1,10):
                for d in range(c+1,11):
                    k=[1]
                    k.append(a)
                    k.append(b)
                    k.append(c)
                    k.append(d)
                    brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8,9,10]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==12:
    for a in range(2,9):
        for b in range(a+1,10):
            for c in range(b+1,11):
                for d in range(c+1,12):
                    for e in range(d+1,13):
                        k=[1]
                        k.append(a)
                        k.append(b)
                        k.append(c)
                        k.append(d)
                        k.append(e)
                        brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8,9,10,11,12]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==14:
    for a in range(2,10):
        for b in range(a+1,11):
            for c in range(b+1,12):
                for d in range(c+1,13):
                    for e in range(d+1,14):
                        for f in range(e+1,15):
                            k=[1]
                            k.append(a)
                            k.append(b)
                            k.append(c)
                            k.append(d)
                            k.append(e)
                            k.append(f)
                            brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==16:
    for a in range(2,11):
        for b in range(a+1,12):
            for c in range(b+1,13):
                for d in range(c+1,14):
                    for e in range(d+1,15):
                        for f in range(e+1,16):
                            for g in range(f+1,17):
                                k=[1]
                                k.append(a)
                                k.append(b)
                                k.append(c)
                                k.append(d)
                                k.append(e)
                                k.append(f)
                                k.append(g)
                                brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==18:
    for a in range(2,12):
        for b in range(a+1,13):
            for c in range(b+1,14):
                for d in range(c+1,15):
                    for e in range(d+1,16):
                        for f in range(e+1,17):
                            for g in range(f+1,18):
                                for h in range(g+1,19):
                                    k=[1]
                                    k.append(a)
                                    k.append(b)
                                    k.append(c)
                                    k.append(d)
                                    k.append(e)
                                    k.append(f)
                                    k.append(g)
                                    k.append(h)
                                    brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
if N==20:
    for a in range(2,13):
        for b in range(a+1,14):
            for c in range(b+1,15):
                for d in range(c+1,16):
                    for e in range(d+1,17):
                        for f in range(e+1,18):
                            for g in range(f+1,19):
                                for h in range(g+1,20):
                                    for i in range(h+1,21):
                                        k=[1]
                                        k.append(a)
                                        k.append(b)
                                        k.append(c)
                                        k.append(d)
                                        k.append(e)
                                        k.append(f)
                                        k.append(g)
                                        k.append(h)
                                        k.append(i)
                                        brute_force.append(k)
    for k in brute_force:
        all=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for s in k:
            all.remove(s)
        link_team=all
        start_team=k
        start_team_score=0
        link_team_score=0
        for j in start_team:
            for k in start_team:
                if j!=k:
                    start_team_score=start_team_score+int(sdij[j-1][k-1])
        for j in link_team:
            for k in link_team:
                if j!=k:
                    link_team_score=link_team_score+int(sdij[j-1][k-1])
        if start_team_score>=link_team_score:
            difference_list.append(start_team_score-link_team_score)
        elif start_team_score<link_team_score:
            difference_list.append(link_team_score-start_team_score)
print(min(difference_list))
