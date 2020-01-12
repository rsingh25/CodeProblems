# Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.
# For example, 
# suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. 
# In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
#####
# Solution: interate through the list and maintain a list by summing with all previous number. 
#   if any sum reduces to zero, mark the related numbers to zero is source list. 
# finally filter out zero.

import functools
import logging
logging.basicConfig(level=logging.DEBUG)

def exec(input_list):
    sum_list = []
    for idx, num in enumerate(input_list):
        for idx2 in range(len(sum_list)):
            sum_list[idx2] = sum_list[idx2] + num
            if sum_list[idx2] == 0:
                for i in range(idx2, idx + 1):
                    input_list[i] = 0 # These are zeroed out
        sum_list.append(num)
        logging.debug(f"list {input_list} \t sum {sum_list} " )

    return list(filter(lambda x : x != 0, input_list))  # remove zeros

# Test
# To execute python -m unittest {filename}

import unittest
class Test(unittest.TestCase):        
    def test_exec(self):
        self.assertEqual(exec([3, 4 , 5, -6, 6, -12, 1]), [1])
        self.assertEqual(exec([]), [])
        self.assertEqual(exec([0,0,0]), [])
        self.assertEqual(exec([2, 5, -5 , 4]), [2, 4])
        self.assertEqual(exec([-5, 2, 7, 5]), [-5, 2, 7, 5])