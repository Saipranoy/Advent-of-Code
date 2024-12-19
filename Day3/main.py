import re

def part1() :

    with open("input.txt") as f:
        files = f.readlines()

    
    pattern = r"mul\(\d+,\d+\)"
    result = 0

    for line in files:
        matches = re.findall(pattern,line)

        for match in matches:
            num = list(map(int,re.findall(r"\d+",match)))
            result += num[0]*num[1]
        
    print(result)

part1()

def part2() :

    with open("input.txt") as f:
        files = f.readlines() 
    
    pattern  = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

    result = 0
    sum_next = True

    for line in files:
        matches = re.findall(pattern,line)

        for match in matches:
            if match == "do()":
                sum_next = True 
                continue 

            if match == "don't()":
                sum_next = False
                continue 

            if sum_next: 
                num = list(map(int,re.findall(r"\d+",match)))
                result += num[0]*num[1] 
    
    print(result)

part2() 