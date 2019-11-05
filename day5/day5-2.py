#!/usr/local/bin/python3
import re

run_env = "prod"  # test or prod

if run_env == "test":
    input = "input-test.txt"
else:
    input = "input.txt"


def find_all(a_str, sub):
    start = 0
    occurances = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            break
        occurances += 1
        start += len(sub)  # use start += 1 to find overlapping matches
    return occurances


isnice = 0
rule1 = False
rule2 = False

with open(input) as blockstream:
    for row in blockstream:
        rule1 = False
        rule2 = False
        # Check rule 1 - It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
        for i in range(15):
            inputstr = row[i] + row[i+1]
            if (find_all(row, inputstr) > 1):
                rule1 = True
            if i < 14:
                if (row[i] == row[i+2]) and rule2 == False:
                    rule2 = True
        # Check rule 2 - It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
        # If both rule1 and rule2 are true, increase isnice counter
        if rule1 == True and rule2 == True:
            isnice += 1
print(isnice)
