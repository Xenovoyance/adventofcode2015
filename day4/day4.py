#!/usr/local/bin/python3

import hashlib

secret_key = "yzbqklnj"
found_hash = False
iteration = 0

while found_hash == False:
    new_key = secret_key + str(iteration)
    # print(".")
    if hashlib.md5(new_key.encode()).hexdigest()[0] == "0":
        if hashlib.md5(new_key.encode()).hexdigest()[1] == "0":
            if hashlib.md5(new_key.encode()).hexdigest()[2] == "0":
                if hashlib.md5(new_key.encode()).hexdigest()[3] == "0":
                    if hashlib.md5(new_key.encode()).hexdigest()[4] == "0":
                        print(hashlib.md5(new_key.encode()).hexdigest() +
                              " found after " + str(iteration) + " tries.")
                        if hashlib.md5(new_key.encode()).hexdigest()[5] == "0":
                            print(hashlib.md5(new_key.encode()).hexdigest() +
                                  " found after " + str(iteration) + " tries.")
                            break
    iteration += 1

    # Just in case killer
    if iteration > 10000000:
        break
