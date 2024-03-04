# part one
f = open("input.txt", "r")
lines = f.read().split("\n")
def problem_1():
    sum = 0
    i = 0
    for line in lines:
        line_numbers = [char for char in line if char.isdigit()]
        line_sum = 10 * int(line_numbers[0]) + int(line_numbers[-1])
        sum += line_sum
        print(line_sum)
    print(sum)


# part two
number_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = [str(i) for i in range(1, 10)] + number_names
sum = 0

# converts number string into int
def to_int(s: str) -> int:
    try:
        return int(s)
    except:
        return 1 + number_names.index(s)


# problem 2
def problem_2():
    sum = 0
    for line in lines:
        line_numbers = []
        for i in range(len(line)):
            for j in range(i + 1, i + 6):
                if line[i : j] in numbers:
                    line_numbers.append(line[i : j])
        line_sum = to_int(line_numbers[0]) * 10 + to_int(line_numbers[-1])
        sum += line_sum
    print(sum)


problem_2()