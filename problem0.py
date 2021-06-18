import os
import sys


def main():
    count = 0
    dt = dict()
    word = input("Enter 10 character word: ")
    for i in word:
        if i not in dt:
            dt[i] = 1
        else:
            dt[i] = dt[i] + 1
    print(dt)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
