#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "input-test.txt"
else:
    input = "input.txt"

theworld = {}
santapositionx = 0
santapositiony = 0

roboelfpositionx = 0
roboelfpositiony = 0

positioncounter = 0


def givepresent(x, y):
    global theworld
    theworld[x, y] = True


givepresent(santapositionx, santapositiony)

with open(input) as blockstream:
    for row in blockstream:
        for character in row:
            # count, if even move santa else move robo
            if positioncounter % 2:
                if character == "<":
                    santapositionx -= 1
                elif character == ">":
                    santapositionx += 1
                elif character == "^":
                    santapositiony += 1
                elif character == "v":
                    santapositiony -= 1
                givepresent(santapositionx, santapositiony)
            else:
                if character == "<":
                    roboelfpositionx -= 1
                elif character == ">":
                    roboelfpositionx += 1
                elif character == "^":
                    roboelfpositiony += 1
                elif character == "v":
                    roboelfpositiony -= 1
                givepresent(roboelfpositionx, roboelfpositiony)
            positioncounter += 1

print("Santa gave presents to " + str(len(theworld)) + " homes.")
