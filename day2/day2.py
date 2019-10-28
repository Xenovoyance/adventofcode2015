#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "day2-inputtest.txt"
else:
    input = "day2-input.txt"

totalBoxArea = 0
totalribbon = 0
currentExtra = 0


def breakApartString(box):
    return box.rstrip("\n\r").split('x')


def smallestinlist(smallist):
    smallist.sort()
    return int(smallist[0])


def messureribbon(first, second, third):
    # Messure both smallest distance around sides AND smallest perimeter of any one surface. Take smallest and pass on together with bow

    distance = [0, 0, 0, 0]

    distance[0] = 2 * first + 2 * second
    distance[1] = 2 * first + 2 * second
    distance[2] = 2 * second + 2 * third
    distance[3] = 2 * first + 2 * third

    distance.sort()

    bow = first * second * third

    return distance[0] + bow


def surfaceAreaOfBox(boxlist):
    global currentExtra
    global totalribbon

    boxlist.sort()
    addRibbonToTotal(messureribbon(int(boxlist[0]), int(boxlist[1]), int(boxlist[2])))

    firstside = int(boxlist[0]) * int(boxlist[1])
    secondside = int(boxlist[1]) * int(boxlist[2])
    thirdside = int(boxlist[0]) * int(boxlist[2])
    currentExtra = smallestinlist([firstside, secondside, thirdside])
    #print(firstside, secondside, thirdside, ">", currentExtra)
    sides = 2 * firstside + 2 * secondside + 2 * thirdside
    total = sides + currentExtra

    #print(sides, "(", currentExtra, ")", ">>", total, "(Ribbon:", totalribbon, ")")

    return total


def addAreaToTotal(boxarea):
    global totalBoxArea
    totalBoxArea += boxarea


def addRibbonToTotal(length):
    global totalribbon
    totalribbon += length


with open(input) as blockstream:
    for row in blockstream:
        addAreaToTotal(surfaceAreaOfBox(breakApartString(row)))

print("\nThe total box area is", totalBoxArea, "and ribbon length is", totalribbon)


'''
Right answers:
Wrapping paper: 1588178
Ribbon: 3783758
'''
