def valid (rules, update):
    for first,second in rules:
        if first not in update or second not in update:
            continue 

        if update.index(first) > update.index(second):
            return False
    return True




def part1() :
    
    rules = []
    updates = []
    with open("input.txt") as f:
        files = f.readlines() 
    
    for file in files:
        if '|' in file:
            rules.append(tuple(map(int,file.split("|"))))
        
        if ',' in file:
            updates.append(tuple(map(int,file.split(","))))
    
    valid_updates = []

    for update in updates:
        if valid(rules,update):
            valid_updates.append(update)
    
    middles_sum = 0

    for valid_update in valid_updates:
        middles_sum += valid_update[len(valid_update)//2]

    print (middles_sum)

part1()