

def play_round(hand_1, target):

    match hand_1:
        case 'A':
            hand_1_int = 1
        case 'B':
            hand_1_int = 2
        case 'C':
            hand_1_int = 3
    if target == 'Y':
        return (hand_1_int + 3)
    else:
        to_win = {'A': 2, 'B': 3, 'C': 1}
        to_lose = {'A': 3, 'B': 1, 'C': 2}
        if target == 'Z':
            return (6 + to_win[hand_1])
        else:
            return to_lose[hand_1]


def main():

    total_score = 0
    F_NAME = 'input2.txt'
    # Open the file in read-only mode
    with open(F_NAME, 'r') as file:
        # Read each line of the file
        line = file.readline()

        while line:
            # Print the linels
            # print(repr(line), len(line))
            total_score += play_round(line[0], line[2])
            print(
                f'hand_1: {line[0]},  need: {line[2]}, points: {play_round(line[0],line[2])}, total: {total_score}')
            # Read the next line
            line = file.readline()

    print(total_score)


if __name__ == '__main__':
    main()
