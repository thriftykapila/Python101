###
# Problem: (https://leetcode.com/problems/add-two-numbers but using lists instead of Linked Lists
# You are given two non-empty lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
###


class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        carry = 0        
        result = []
        size = max(len(l1), len(l2))
        i = 0
        while i<size or carry != 0:
            sum = self.get_list_item_or_zero(l1, i) + self.get_list_item_or_zero(l2, i) + carry
            result.append(sum%10)
            i += 1
            carry = int(sum/10)
        
        return result
    
    def get_list_item_or_zero(self, l: list, i: int):
        try:
            return l[i]
        except IndexError:
            return 0


# Test
# print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))