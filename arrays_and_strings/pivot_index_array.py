#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def pivotIndex(nums):

        s = sum(nums)

        left_sum = 0

        for i, x in enumerate(nums):

            if left_sum == (s - left_sum - x):
                return i
            
            left_sum += x
        
        return -1