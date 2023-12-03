# return raw text from input
def read_raw_text(day):
    with open(f"{day}/{day}.txt") as f:
        return f.read()

# return list of lines from input
def read_lines_list(day):
    with open(f"{day}/{day}.txt") as f:
        return list(map(str.strip,f.readlines()))

# return groups of lines from input
def read_groups(day):
    with open(f"{day}/{day}.txt") as f:
        return [group.split("\n") for group in f.read().split("\n\n")]
    
# return list of list of chars from 2d grid input
def read_grid_2d(day):
    with open(f"{day}/{day}.txt") as f:
        return [list(line.strip()) for line in f.readlines()]   
