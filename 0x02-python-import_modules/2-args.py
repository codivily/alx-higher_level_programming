#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    print("{:d} arguments{}".format(argc - 1, ("." if argc == 1 else ":")))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
