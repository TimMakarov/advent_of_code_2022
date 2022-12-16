

def play_round(hand_1, hand_2):
    match hand_2:
        case 'X':
            hand_2_int = 1
        case 'Y':
            hand_2_int = 2
        case 'Z':
            hand_2_int = 3
    match hand_1:
        case 'A':
            hand_1_int = 1
        case 'B':
            hand_1_int = 2
        case 'C':
            hand_1_int = 3

    to_win = [(1, 3), (2, 1), (3, 2)]
    if hand_2_int == hand_1_int:
        points_for_win = 3

    elif (hand_2_int, hand_1_int) in to_win:
        points_for_win = 6
    else:
        points_for_win = 0
    return (points_for_win+hand_2_int)


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
                f'hands: {line[0]} vs {line[2]}, {play_round(line[0],line[2])}, total: {total_score}')
            # Read the next line
            line = file.readline()

    print(total_score)


if __name__ == '__main__':
    main()
