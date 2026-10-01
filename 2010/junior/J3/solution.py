import sys


values = {"A": 0, "B": 0}

for line in sys.stdin:
    parts = line.split()
    instruction = int(parts[0])

    if instruction == 7:
        break

    x = parts[1]
    if instruction == 1:
        values[x] = int(parts[2])
    elif instruction == 2:
        print(values[x])
    else:
        y = parts[2]
        left, right = values[x], values[y]

        if instruction == 3:
            result = left + right
        elif instruction == 4:
            result = left * right
        elif instruction == 5:
            result = left - right
        else:
            result = abs(left) // abs(right)
            if (left < 0) != (right < 0):
                result = -result

        values[x] = result
