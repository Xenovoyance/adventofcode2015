#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "input-test.txt"
else:
    input = "input.txt"

vowelcnt = 0
previouschar = ""
nicestrings = 0

twoinrow = False
vowels = False
cleanstring = False


with open(input) as blockstream:
    for row in blockstream:
        twoinrow = False
        vowels = False
        cleanstring = False
        # First remove the bad ones
        if (row.find('ab') == -1):
            if (row.find('cd') == -1):
                if (row.find('pq') == -1):
                    if (row.find('xy') == -1):
                        cleanstring = True
                        vowelcnt = 0
                        # Then validate the individual characters
                        for character in row:
                            # Vowels
                            if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
                                vowelcnt += 1
                            ## Two in row
                            if character == previouschar:
                                twoinrow = True
                            previouschar = character
                        if vowelcnt > 2:
                            vowels = True
        if twoinrow and vowels and cleanstring:
            nicestrings += 1

print(str(nicestrings))
