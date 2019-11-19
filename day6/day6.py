#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "input-test.txt"
else:
    input = "input.txt"

# initiate and set the whole matrix to 0
light_matrix = {}
for i in range(0, 1000):
    for j in range(0, 1000):
        light_matrix[i, j] = 0


def turn_on(start, end):
    start_ids = start.split(",")
    end_ids = end.split(",")
    for i in range(int(start_ids[0]), int(end_ids[0])+1):
        for j in range(int(start_ids[1]), int(end_ids[1])+1):
            light_matrix[i, j] = 1


def turn_off(start, end):
    start_ids = start.split(",")
    end_ids = end.split(",")
    for i in range(int(start_ids[0]), int(end_ids[0])+1):
        for j in range(int(start_ids[1]), int(end_ids[1])+1):
            light_matrix[i, j] = 0


def toggle(start, end):
    start_ids = start.split(",")
    end_ids = end.split(",")
    for i in range(int(start_ids[0]), int(end_ids[0])+1):
        for j in range(int(start_ids[1]), int(end_ids[1])+1):
            if light_matrix[i, j] == 0:
                light_matrix[i, j] = 1
            else:
                light_matrix[i, j] = 0


def check_operator(input_string):
    words = input_string.split()
    if (words[0] == "toggle"):
        return "toggle"
    elif (words[1] == "on"):
        return "on"
    elif (words[1] == "off"):
        return "off"


with open(input) as blockstream:
    for row in blockstream:
        row_words = row.split()
        # check operator
        operator = check_operator(row)

        if (operator == "toggle"):
            toggle(row_words[1], row_words[3])
        elif (operator == "on"):
            turn_on(row_words[2], row_words[4])
        elif (operator == "off"):
            turn_off(row_words[2], row_words[4])

lights_turned_on = 0

for i in range(0, 1000):
    for j in range(0, 1000):
        if (light_matrix[i, j] == 1):
            lights_turned_on += 1

print(lights_turned_on)
# print(len(light_matrix))

# 542387 too low
