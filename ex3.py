
def check_item(group):

    for char in group[0]:
        if char in group[1] and char in group[2]:
            item = ord(char)
            if item > 96:
                return (char, item - 96)
            else:
                return (char, item - 64 + 26)
    return (0, 0)


def main():

    total_score = 0
    F_NAME = 'input3.txt'
    line_group = []
    # Open the file in read-only mode
    with open(F_NAME, 'r') as file:
        # Read each line of the file
        line = file.readline()

        while line:
            # Print the linels
            # print(repr(line), len(line))
            # total_score += play_round(line[0], line[2])
            line_group.append(line.strip())
            print(len(line_group), line)
            if len(line_group) == 3:
                c, n = check_item(line_group)
                total_score += n
                print(c, n, total_score)
                line_group = []

            line = file.readline()

    print(total_score)


if __name__ == '__main__':
    main()
