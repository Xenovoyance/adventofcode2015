#!/usr/local/bin/python3

import hashlib

secret_key = "yzbqklnj"
found_hash = False
iteration = 0

while found_hash == False:
    new_key = secret_key + str(iteration)
    temp_hash = hashlib.md5(new_key.encode()).hexdigest()

    if temp_hash[0] == "0":
        if temp_hash[1] == "0":
            if temp_hash[2] == "0":
                if temp_hash[3] == "0":
                    if temp_hash[4] == "0":
                        print(temp_hash +
                              " found after " + str(iteration) + " tries.")
                        if temp_hash[5] == "0":
                            print(temp_hash +
                                  " found after " + str(iteration) + " tries.")
                            break
    iteration += 1

    # Just in case killer
    if iteration > 10000000:
        break
