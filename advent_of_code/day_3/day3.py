# Create a class for each and column + line number as attribute
DIGITS = "0123456789"

class Number:
    def __init__(self, value: int, start: tuple, end: tuple) -> None:
        self.start = start
        self.end = end

# For numbers add an attribute for all adjacent spaces (used to find if adj. symbols)
    def get_adjacent(self) -> list[tuple]:
        lign = self.start[0]
        all_adj = set()
        for num in range(self.start[1],self.end[1] + 1):
            adjacents = self.adjacents_of_digit((lign, num))
            all_adj.update(adjacents)
        return all_adj


    
    def adjacents_of_digit(self, digit: tuple) -> list[tuple]:
        adjacents = []
        # Loop through all the adjacent line (ours included)
        for i in range(digit[0] - 1, digit[0] + 2):
            # Loop through all adj. colums
            for j in range(digit[1] - 1, digit[1]+ 2):
                adjacents.append((i,j))
        return adjacents
    
def check_symbol(symbol: str) -> bool:
    if symbol not in DIGITS:
        

number = Number(256, (3,5), (3,7))
print(number.get_adjacent())

raw = [["467..114.."],
["...*......"],
["..35..633."],
["......#..."],
["617*......"],
[".....+.58."],
["..592....."],
["......755."],
["...$.*...."],
[".664.598.."]]



for i in range(len(raw)):
    for j in range(len(raw[i].split(""))):
        # Check if symbol
        if raw[i][j] not in
        # Check if number

# Go through each line to find numbers and symbols

# Add to number and symbol list
    
# Go through number list, check if symbol have matching coordinates, add to sum if yes