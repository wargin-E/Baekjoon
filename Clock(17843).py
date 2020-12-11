n=int(input())
test_cases=[]
def minimum_angle(test_case):
    seconds_angle=6*int(test_case[2])
    minutes_angle=6*(int(test_case[1])+int(test_case[2])/60)
    hours_angle=30*(int(test_case[0])+int(test_case[1])/60+int(test_case[2])/3600)
    if seconds_angle-minutes_angle>0 or seconds_angle-minutes_angle==0:
        sec_min=seconds_angle-minutes_angle
    elif seconds_angle-minutes_angle<0:
        sec_min=minutes_angle-seconds_angle
    if seconds_angle-hours_angle>0 or seconds_angle-hours_angle==0:
        hour_sec=seconds_angle-hours_angle
    elif seconds_angle-hours_angle<0:
        hour_sec=hours_angle-seconds_angle
    if hours_angle-minutes_angle>0 or hours_angle-minutes_angle==0:
        hour_min=hours_angle-minutes_angle
    elif hours_angle-minutes_angle<0:
        hour_min=minutes_angle-hours_angle
    if sec_min>180:
        sec_min=360-sec_min
    if hour_sec>180:
        hour_sec=360-hour_sec
    if hour_min>180:
        hour_min=360-hour_min
    three_angles=[sec_min,hour_sec,hour_min]
    min=sec_min
    for k in range(1,3):
        if three_angles[k]<min:
            min=three_angles[k]
    print(min)


for k in range(0,n):
    a=input()
    test_cases.append(a.split(" "))
for k in test_cases:
    minimum_angle(k)

