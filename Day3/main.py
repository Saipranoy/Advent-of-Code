import re

# Logic 1: Match the pattern (mul(2,3)) and then extract the digits to sum
# up the multiplication of the numbers.

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

# Logic 2: Same as above but we first extract pattern do() and don't()
# and then get the result.

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