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

#part1()

def part2() :
   
    with open ("input.txt") as f:
        files = f.readlines()

    rules = []
    updates = []

    for file in files :
        if '|' in file:
            rules.append(tuple(map(int,file.split("|"))))
        
        if ',' in file:
            updates.append(list(map(int,file.split(','))))

    not_updates = []

    for update in updates:
        if not valid(rules,update):
            not_updates.append(update) 
    
    middle_sum = 0

    for not_update in not_updates:
        while not valid(rules,not_update):
            
            for first,second in rules:
                if first not in not_update or second not in not_update:
                    continue 

                first_index = not_update.index(first)
                second_index = not_update.index(second)

                if first_index > second_index:
                    not_update[first_index] = second
                    not_update[second_index] = first
            
        middle_sum += not_update[len(not_update)//2]

    print (middle_sum)

part2()
