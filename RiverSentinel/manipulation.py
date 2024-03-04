# from numpy import random


# data = [
#     [7.3, 197, 6.4, 22.7],
#     [7.2, 128, 1.8, 21.6],
#     [6.8, 128, 1.9, 20.7],
#     [7.5, 441, 19, 21.5],
#     [7.2, 195, 1.0, 20.6],
#     [6.2, 226, 1.5, 19.9],
#     [7.4, 353, 4.5, 21.5],
# ]

# readings = [
#     [7.39, 195, 6.14, 23.6],
#     [6.87, 128, 1.81, 20.7],
#     [6.74, 126, 1.85, 21.1],
#     [7.47, 444, 18.6, 22.0],
#     [7.25, 204, 1.00, 20.9],
#     [6.20, 221, 1.49, 19.8],
#     [7.40, 360, 4.59, 21.2]
# ]

# units = ["", "\\textmu S/cm", "FNU", "\\textdegree C"]

# errors = []
# i = 1
# print("RANDOM NUMBERS")

# # for i, row in enumerate(data):
# #     output = ""
# #     for j, number in enumerate(row):
# #         rand = round(random.normal(loc=number, scale=0.02 * number), 2)
# #         output += f"{rand} ({round(abs(rand - number) / number * 100, 2)}\\%) & "
# #     print(f"{i + 1} & {output[:-2]}\\\\")

# for i, row in enumerate(data):
#     output = ""
#     for j, number in enumerate(row):
#         reading = readings[i][j]
#         output += f"{round(abs(number - reading) / number * 100, 2)} "
#     print(output)


data = [
[1.2, 1.0, 4.1, 4.0],
[4.6, 0.0, 0.6, 4.2],
[0.9, 1.6, 2.6, 1.9],
[0.4, 0.8, 2.1, 2.3],
[0.7, 4.6, 0.0, 1.5],
[0.0, 2.2, 0.7, 0.5],
[0.0, 2.0, 2.0, 1.4]
]

total = 0
for row in data:
    for number in row:
        total += number
print(total / 28)