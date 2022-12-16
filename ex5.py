
def readfile():
    F_NAME = 'input5.txt'
    with open(F_NAME, 'r') as file:
        arr = file.read().split('\n')

    ch = [i*4 for i in range(1, 9)]
    chars = list(map(lambda x: x+1, ch))
    chars.insert(0, 1)
    grid = []
    for i in range(9):
        grid.append([])
    for row in range(8):
        line = arr[row]
        for index in range(len(grid)):
            letter = line[chars[index]]
            if letter != ' ':
                grid[index].append(letter)
    return (arr, grid)


def move_letters(grid, amount, stack_from, stack_to):
    moved_arr = []
    for i in range(amount):
        moved_arr.insert(0, grid[stack_from].pop(0))
    for j in range(amount):
        grid[stack_to].insert(0, moved_arr[j])
    return (grid)


def main():
    arr, grid = readfile()
    for row in range(10, len(arr)):
        # list(map(int, xs))
        move = arr[row].split(' ')
        amount = int(move[1])
        stack_from = int(move[3])
        stack_to = int(move[5])
        print(f'move amount: {amount}, from: {stack_from}, to: {stack_to}')
        stack_from -= 1
        stack_to -= 1
        grid = move_letters(grid, amount, stack_from, stack_to)
    print(grid)
    result = []
    for i in grid:
        result.append(i[0])
    print(''.join(result))


if __name__ == '__main__':
    main()
