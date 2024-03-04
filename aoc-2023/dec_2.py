# open file
f = open("input.txt", "r")
lines = f.read().split("\n")

# part one
def problem_1():
    p1 = list(lines)
    sum = 0
    for line in p1:
        # obtain singular draws
        draws = line[line.index(":") + 2 :].replace(";", ",").split(", ")
        valid = True
        for draw in draws:
            num = int(draw[: draw.index(" ")])
            if "red" in draw:
                valid = num < 13
            elif "green" in draw:
                valid = num < 14
            elif "blue" in draw:
                valid = num < 15
            else:
                print("unhappy")
        if valid:
            sum += int(line[line.index(' ') + 1 : line.index(':')])
    print(sum)
    


# part two
def problem_2():
    p2 = list(lines)
    power_sum = 0
    get_num = lambda d : int(d[: d.index(" ")])
    for line in p2:
        # obtain singular draws
        draws = line[line.index(":") + 2 :].replace(";", ",").split(", ")
        red_min = 0
        green_min = 0
        blue_min = 0
        for draw in draws:
            num = get_num(draw)
            if "red" in draw:
                red_min = num if num > red_min else red_min
            elif "green" in draw:
                green_min = num if num > green_min else green_min
            elif "blue" in draw:
                blue_min = num if num > blue_min else blue_min
            else:
                print("unhappy")
        power_sum += red_min * green_min * blue_min
    print(power_sum)


problem_2()