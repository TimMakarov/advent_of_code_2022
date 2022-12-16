
def readfile():
    F_NAME = 'input6.txt'
    with open(F_NAME, 'r') as file:
        arr = file.read()
    return (arr)


def main():
    arr = readfile()
    if len(set(arr[:14])) == 14:
        print(arr[:14], 14)
    else:
        str = list(arr[:14])
        print(str, 2)
        for i in range(14, len(arr)):
            str.pop(0)
            str.append(arr[i])
            if len(set(str)) == 14:
                print(f'got it: {str} , {i+1}')
                break


if __name__ == '__main__':
    main()
