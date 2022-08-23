from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]):
        n = gas.__len__()
        final_list = []
        for g, c in zip(gas, cost):
            final_list.append(g - c)

        if sum(final_list) < 0:
            return -1
        
        final_list *= 2

        i = 0
        while i < n:
            while i < n and final_list[i] < 0:
                i += 1
            
            sum_ = final_list[i]
            j = 1
            while j < n:
                sum_ += final_list[i + j]
                if sum_ < 0:
                    i += 1
                    break
                j += 1
            else:
                return i


        
        
