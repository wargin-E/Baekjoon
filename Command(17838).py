number_of_testcases=int(input())
test_cases=[]

for k in range(0,number_of_testcases):
    test_case=input()
    test_cases.append(test_case)
for k in test_cases:
    if len(k)!=7:
        print(0)
    elif k[0]==k[1]==k[4]:
        if k[2]==k[3]==k[5]==k[6]:
            if k[1]!=k[2]:
                print(1)
            else:
                print(0)
    else:
        print(0)


