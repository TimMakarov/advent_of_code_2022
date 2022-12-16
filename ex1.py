
inventory_db = [0]

# Open the file in read-only mode
with open('input1.txt', 'r') as file:
    # Read each line of the file
    line = file.readline()

    while line:
        # Print the linels
        # print(repr(line), len(line))
        if line.strip().isnumeric():
            # print(f'last before: {inventory_db[-1]} adding {int(line)}')
            inventory_db[-1] += int(line)
            # print(f'last after: {inventory_db[-1]}')
        else:
            inventory_db.append(0)

        # Read the next line
        line = file.readline()

print(inventory_db[0])
inventory_db.sort(reverse=True)
print(inventory_db[0])
print(inventory_db[:3])
print(sum(inventory_db[:3]))
