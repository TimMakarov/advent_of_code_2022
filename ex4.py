
def check_range(group):

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
    F_NAME = 'input4.txt'
    line_group = []
    # Open the file in read-only mode
    with open(F_NAME, 'r') as file:
        # Read each line of the file
        line = file.readline()

        while line:

            ranges = line.strip().split(sep=',')
            r1 = ranges[0].split(sep='-')
            r2 = ranges[1].split(sep='-')

            r1_1 = int(r1[0])
            r1_2 = int(r1[1])
            r2_1 = int(r2[0])
            r2_2 = int(r2[1])

            if r1_1 == r2_1 or r1_2 == r2_2:
                total_score += 1
            else:
                if r1_1 > r2_1:
                    r1_1, r2_1 = r2_1, r1_1
                    r1_2, r2_2 = r2_2, r1_2

                if r1_1 <= r2_1 and r1_2 >= r2_1:
                    total_score += 1

                elif r1_1 > r2_1 and r1_2 <= r2_2:
                    total_score += 1

                else:
                    print(r1, r2)

            line = file.readline()

    print(total_score)


if __name__ == '__main__':
    main()
