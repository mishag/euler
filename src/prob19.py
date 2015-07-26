#!/usr/bin/python

import time

SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

JAN = 0
FEB = 1
MAR = 2
APR = 3
MAY = 4
JUN = 5
JUL = 6
AUG = 7
SEP = 8
OCT = 9
NOV = 10
DEC = 11

MONTH_TO_STRING = {
    JAN: "Jan",
    FEB: "Feb",
    MAR: "Mar",
    APR: "Apr",
    MAY: "May",
    JUN: "Jun",
    JUL: "Jul",
    AUG: "Aug",
    SEP: "Sep",
    OCT: "Oct",
    NOV: "Nov",
    DEC: "Dec"
}

DAY_TO_STRING = {
    MON: "Mon",
    TUE: "Tue",
    WED: "Wed",
    THU: "Thu",
    FRI: "Fri",
    SAT: "Sat",
    SUN: "Sun"
}

LAST_DATE = {
    JAN : 31,
    FEB : 28,
    MAR : 31,
    APR : 30,
    MAY : 31,
    JUN : 30,
    JUL : 31,
    AUG : 31,
    SEP : 30,
    OCT : 31,
    NOV : 30,
    DEC : 31
}

def next_month(month):
    return (month + 1) % 12

def is_leap_year(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0

class Day:
    def __init__(self):
        self._year  = 1900
        self._month = JAN
        self._date  = 1
        self._day   = MON

    def __str__(self):
        return "%d-%s-%d, %s" %(self._year, 
                                MONTH_TO_STRING[self._month],
                                self._date,
                                DAY_TO_STRING[self._day])

    def __repr__(self):
        return self.__str__()

    def is_last_date_of_the_month(self):
        if self._month == FEB:
            return self._date == 29 if is_leap_year(self._year) else self._date == 28

        return self._date == LAST_DATE[self._month]

    def day(self):
        return self._day

    def month(self):
        return self._month

    def year(self):
        return self._year

    def date(self):
        return self._date

    def next(self):
        self._day = (self._day + 1) % 7

        if self.is_last_date_of_the_month():
            self._date = 1
            if self._month == DEC:
                self._year += 1
                
            self._month = next_month(self._month)
        else:
            self._date += 1



if __name__ == "__main__":
    start = time.time()
    
    d = Day()
    count = 0
    while True:
        if d.date() == 31 and d.year() == 2000 and d.month() == DEC:
            break

        #print d
        if d.day() == SUN and d.date() == 1 and d.year() >= 1901:
            count += 1
        d.next()

    print count

    print time.time() - start
