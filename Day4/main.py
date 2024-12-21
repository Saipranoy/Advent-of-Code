# The algorithm starts at every cell, lokking for the first letter "X"
# For every "X" found,  it tries all 8 directions.
# If all letters matched in any direction then they are counted as found.
def search_word_in_grid(grid, word) :

    rows , cols = len(grid), len(grid[0])
    word_len = len(word)
    result = 0

    directions = [
        (0, 1),
        (0, -1), 
        (1, 0), 
        (-1, 0), 
        (1, 1), 
        (-1, -1), 
        (1, -1), 
        (-1, 1)
    ]
    
    # Check if the they are within the grid
    def is_valid(x, y) :
        return 0 <= x < rows and 0 <= y < cols
    
    # Check if the word is found in the grid 

    def search_from_cell(r,c) :
        
        count = 0
        # Check if the first letter is found "X" 
        if grid[r][c] != word[0] :
            return 0
        
  

        for dr,dc in directions :

            found = 1 

            for k in range (word_len):

                nr,nc = r + k*dr, c + k*dc 

                if not is_valid(nr,nc) or grid[nr][nc] != word[k] :
                    found = 0
                    break

            if found == 1 :
                count += 1
                
            
        return count
    
    for r in range(rows) :
        for c in range(cols) :
            result += search_from_cell(r,c) 

    return result


def part1() :

    with open("input.txt") as f:
        grid = f.readlines() 
        
    grid = [list(line.strip()) for line in grid]

    word = "XMAS"
    
    result = search_word_in_grid(grid, word)

    print (result)

#part1()

def part2() :
    grid = []

    with open("input.txt") as f:
        grid = f.readlines() 
        

    
    count = 0

    for r in range (1,len(grid)-1):
        for c in range (1,len(grid[0].strip())-1):
            if grid[r][c] == "A":
                if ((grid[r-1][c-1] == "M" and grid[r+1][c+1] == "S") or \
                    (grid[r-1][c-1] == "S" and grid[r+1][c+1] == "M")) and \
                    ((grid[r-1][c+1] == "M" and grid[r+1][c-1] == "S") or \
                    (grid[r-1][c+1] == "S" and grid[r+1][c-1] == "M")):
                     count += 1
    print(count)
    return count 

part2() 
        



    
    
    

    

part2() 