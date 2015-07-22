#!/usr/bin/python

import sys

results = {}

def partitions(n, max_num_used):
    if (n, max_num_used) in results:
        return results[(n, max_num_used)]
    
    if n == 0:
        return 1

    if n < 0:
        return 0

    if max_num_used <= 0:
        return 0

    res =  partitions(n, max_num_used - 1) + partitions(n - max_num_used, max_num_used)
    results[(n, max_num_used)] = res
    return res

def partitions_from_set(n, nums):
    if (n, nums) in results:
        return results[(n, nums)]

    if n == 0:
        return 1

    if n < 0:
        return 0

    if len(nums) <= 0:
        return 0

    res = partitions_from_set(n, nums[:-1]) + partitions_from_set(n - nums[-1], nums)
    results[(n, nums)] = res
    return res

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    
    n = int(sys.argv[1])
    print partitions(n, n)
    
    # count = 1
    # while True:
    #     print "processing %d. Partitions = " %count,
    #     res = partitions(count, count)
    #     print res
    #     if res % 1000000 == 0:
    #         break;
    #     count += 1

    # exit(0)
