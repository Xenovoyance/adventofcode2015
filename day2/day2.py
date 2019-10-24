#!/usr/local/bin/python3

run_env = "test"  # test or prod

if run_env == "test":
    input = "day2-inputtest.txt"
else:
    input = "day2-input.txt"

totalBoxArea = 0
currentExtra = 0


def breakApartString(box):
    return box.rstrip("\n\r").split('x')


def smallestinlist(smallist):
    smallist.sort()
    return int(smallist[0])


def surfaceAreaOfBox(boxlist):
    global currentExtra

    firstside = int(boxlist[0]) * int(boxlist[1])
    secondside = int(boxlist[1]) * int(boxlist[2])
    thirdside = int(boxlist[0]) * int(boxlist[2])
    currentExtra = smallestinlist([firstside, secondside, thirdside])
    sides = 2 * firstside + 2 * secondside + 2 * thirdside
    total = sides + currentExtra

    print(sides, "(", currentExtra, ")", ">>", total)

    return total


def addAreaToTotal(boxarea):
    global totalBoxArea
    totalBoxArea += boxarea


with open(input) as blockstream:
    for row in blockstream:
        addAreaToTotal(surfaceAreaOfBox(breakApartString(row)))
print("\nThe total box area is:", totalBoxArea)
