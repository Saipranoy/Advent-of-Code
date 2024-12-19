def is_safe(num):

    for i in range(len(num)-1):
        a,b = num[i],num[i+1] 
        if not 0 < abs(b-a) <4:
            print("condition 1")
            return False 
        
        if i == len(num)-2:
            print("condition 2")
            continue

        c = num[i+2]

        if not a<b<c and not a>b>c :
            print("condition 3")
            return False 
        
    return True

        

def part1():
    reports = []

    with open("input.txt") as f:
        reports = f.readlines()
    
    safe = 0 

    for report in reports:
        num = list(map(int,report.split (' ')))


        if is_safe(num):
           safe += 1 
        else:
            for i in range(len(num)):
                if is_safe(num[:i]+num[i+1:]):
                    safe+=1
                    break
    
    print(safe)

part1()