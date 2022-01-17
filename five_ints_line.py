#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 16, 2022
# This program uses a for loop and an
# if statement to print integers ranging
# from 1000 to 2000.

# initializes the counter
counter = 1000


# function determines the integer amount
def main():

    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print(" ")
        print(counter, end=" ")


if __name__ == "__main__":
    main()
