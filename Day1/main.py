
def part1():
    lines = []

    with open("input.txt") as f:
        lines = f.readlines()
    
    list1 = []
    list2 = []

    for i in range(len(lines)):
        list1.append(int(lines[i].split(' ')[0]))    # Split the line by space and get the first element and add it to the firt list
        list2.append(int(lines[i].split(' ')[-1]))    # Split the line by space and get the second element and add it to the second list

    list1.sort()
    list2.sort()   # Sort the lists

    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])  # Subtract the elements of the two lists and get the absolute value and add it to the total list
    
    print(total)

#part1()

def part2():
    lines = []

    with open("input.txt") as f:
        lines = f.readlines()
    
    list1 = []
    list2 = []

    for i in range(len(lines)):
        list1.append(int(lines[i].split(' ')[0]))    # Split the line by space and get the first element and add it to the firt list
        list2.append(int(lines[i].split(' ')[-1]))    # Split the line by space and get the second element and add it to the second list

    list1.sort()
    list2.sort()   # Sort the lists

    total = 0
 
    for i in range(len(list1)):
        n = 0
        for j in range(len(list2)):
           if list1[i] == list2[j]:
               n += 1 
        total += list1[i]*n

    print(total)

part2()
