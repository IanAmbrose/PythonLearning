import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr = [7, 69, 2, 221, 8974]


def miniMaxSum(arr):

    for i in range(0, len(arr)):
        arr[i] = int(arr[i])

    s = sum(arr)
    print(str(s - max(arr)) + " " + str(s - min(arr)))


if __name__ == "__main__":

    arr = [7, 69, 2, 221, 8974]

    miniMaxSum(arr)
