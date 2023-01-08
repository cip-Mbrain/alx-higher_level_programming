#!/usr/bin/python3
def no_c(my_string):
    arr = []
    for i in my_string:
        if i == "c" or i == "C":
            arr.append('')
        else:
            arr.append(1)
    return "".join(arr)
