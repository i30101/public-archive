# import external libraries
import re

# open file
f = open("input.txt", "r")
lines = f.read().split("\n")

# numbers in string form
numbers = list("0123456789")

# part one
def problem_1():
    p1 = list(lines)
    
    # go through rows
    sum = 0
    for r, row in enumerate(p1):
        # obtain numbers in row
        row_string = "".join([char if char.isdigit() else "." for char in row])
        nums = [num for num in row_string.split(".") if num.isdigit()]
        print(nums)
        # print(row)

        # index of next number
        start_index = 0

        # cycle through numbers
        for num in nums:
            # get indeces of number in row
            start_index = row_string.index(num)
            end_index = start_index + len(num)

            adjacent_start = abs(start_index - 1)
            adjacent_end = end_index + 1 if end_index < len(row) - 1 else end_index
            adjacents = row[adjacent_start : adjacent_end]
            if r > 0:
                adjacents += p1[r - 1][adjacent_start : adjacent_end]
            if r < len(p1) - 1:
                adjacents += p1[r + 1][adjacent_start : adjacent_end]
            
            for number in numbers:
                adjacents = adjacents.replace(number, "")

            for char in adjacents:
                if char != ".":
                    print(num)
                    sum += int(num)
                    break
            
            row_string = row_string[: start_index] + "".join(["." for n in num]) + row_string[end_index :]
    print(sum)



# part two
def problem_2():
    p2 = list(lines)

    gear_locations = {}
    for r, row in enumerate(p2):
        row_string = "".join([char if char.isdigit() else "." for char in row])
        # print(row_string)
        nums = [num for num in row_string.split(".") if num.isdigit()]
        # print(nums)
        for num in nums:
            start_index = row_string.index(num)
            end_index = start_index + len(num)

            adjacent_start = abs(start_index - 1)
            adjacent_end = end_index + 1 if end_index < len(row) - 1 else end_index
            
            #check current row
            current = row[adjacent_start : adjacent_end]
            # print()
            # print(current)
            if "*" in current:
                # find all indeces of gears
                current_indeces = [i + adjacent_start for i in range(len(current)) if current.startswith("*", i)]
                # save to dictionary
                for i in current_indeces:
                    # print("added current")
                    if (r, i) not in gear_locations:
                        gear_locations[(r, i)] = [int(num)]
                    else:
                        gear_locations[(r, i)].append(int(num))
                    
            # check row above
            if r > 0:
                above = p2[r - 1][adjacent_start : adjacent_end]
                # print(above)
                if "*" in above:
                    # find all indeces of gears
                    above_indeces = [i + adjacent_start for i in range(len(above)) if above.startswith("*", i)]
                    # save to dictionary
                    for i in above_indeces:
                        # print("added above")
                        if (r - 1, i) not in gear_locations:
                            gear_locations[(r - 1, i)] = [int(num)]
                        else:
                            gear_locations[(r - 1, i)].append(int(num))


            # check row below
            if r < len(p2) - 1:
                below = p2[r + 1][adjacent_start : adjacent_end]
                # print(below)
                if "*" in below:
                    # find all incedes of gears
                    below_indeces = [i + adjacent_start for i in range(len(below)) if below.startswith("*", i)]
                    # print(below_indeces)
                    # save to dictionary
                    for i in below_indeces:
                        # print("added below")
                        if (r + 1, i) not in gear_locations:
                            gear_locations[(r + 1, i)] = [int(num)]
                        else:
                            gear_locations[(r + 1, i)].append(int(num))

    gear_sum = 0
    valids = 0
    print(gear_locations)
    for gear in gear_locations.values():
        if len(gear) == 2:
            # print(gear[0] * gear[1])
            print(gear[0], gear[1])
            gear_sum += (gear[0] * gear[1])
            valids += 1

    print(gear_sum)
    print(valids)



problem_2()