#!/usr/bin/python

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

import sys

SAY_NUMBER = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

SAY_UNIT = {
    0 : "",
    1 : "",
    2 : "hundred",
    3 : "thousand"
}

def say_number(n):
    digits = [int(d) for d in list(str(n))]

    num_digits = len(digits)

    unit = len(digits) - 1
    text = ""
    for digit in digits:

        if unit == 1:
            if num_digits > 2 and (digit != 0 or digits[-1] != 0):
                text += " and "
            if digit == 1:
                text += SAY_NUMBER[10*digit + digits[-1]]
            else:
                text += SAY_NUMBER[10 * digit] + " " + SAY_NUMBER[digits[-1]]

            break

        if digit != 0:
            text += ' '.join([SAY_NUMBER[digit], SAY_UNIT[unit]])
            
        unit -= 1

    return text


if __name__ == "__main__":
    n = int(sys.argv[1])
    letter_count = 0
    for i in range(n):
        letter_count +=  len(''.join(say_number(i+1).split()))

    print letter_count
