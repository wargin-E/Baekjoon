
def did_X_win(test_case):
    for y in range(0,3):
        if test_case[y*3+0]=="X" and test_case[y*3+1]=="X" and test_case[y*3+2]=="X":
            return 1
    for x in range(0,3):
        if test_case[x]=="X" and test_case[3+x]=="X" and test_case[6+x]=="X":
            return 1
    if test_case[0]=="X" and test_case[4]=="X" and test_case[8]=="X":
        return 1
    if test_case[2]=="X" and test_case[4]=="X" and test_case[6]=="X":
        return 1
    return 0
def did_O_win(test_case):
    for y in range(0,3):
        if test_case[y*3+0]=="O" and test_case[y*3+1]=="O" and test_case[y*3+2]=="O":
            return 1
    for x in range(0,3):
        if test_case[x]=="O" and test_case[3+x]=="O" and test_case[6+x]=="O":
            return 1
    if test_case[0]=="O" and test_case[4]=="O" and test_case[8]=="O":
        return 1
    if test_case[2]=="O" and test_case[4]=="O" and test_case[6]=="O":
        return 1
    return 0
def answer(test_case):
    X_count=0
    O_count=0
    for k in test_case:
        if k=="X":
            X_count=X_count+1
        elif k=="O":
            O_count=O_count+1
    if O_count>X_count:
        print("no")
    elif X_count-1>O_count:
        print("no")
    elif did_O_win(test_case)==1 and did_X_win(test_case)==1:
        print("no")
    elif did_O_win(test_case)==1 and did_X_win(test_case)==0:
        if O_count!=X_count:
            print("no")
        else:
            print("yes")
    elif did_O_win(test_case)==0 and did_X_win(test_case)==1:
        if O_count+1!=X_count:
            print("no")
        else:
            print("yes")
    elif did_X_win(test_case)==0 and did_O_win(test_case)==0:
        print("yes")

n=int(input())
test_cases=[]
for k in range(0,4*n-1):
    if (k+1)%4==0:
        blank=input()
        pass
    else:
        test_case_row=input()
        for s in range(0,3):
            test_cases.append(test_case_row[s])
for k in range(0,n):
    test_case=[]
    for s in range(0,9):
        test_case.append(test_cases[9*k+s])
    answer(test_case)


