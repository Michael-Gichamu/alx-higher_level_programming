#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            no_printed += 1
    except IndexError:
        pass
    print()
    return no_printed
