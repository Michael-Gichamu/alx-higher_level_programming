#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv) - 1
    if argv_len == 0:
        print(0, "arguments.")
    else:
        print("{:d} arguments:".format(argv_len))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
