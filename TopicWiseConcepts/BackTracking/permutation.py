## https://leetcode.com/problems/permutations/ ##

class Solution(object):   

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def rec(nums, temp=[], ans=[]):
            if len(temp) == len(nums):
                # print(nums, temp)
                ans.append(temp[:])
                return
            
            for n in nums:
                if n not in temp:
                    temp.append(n)
                    rec(nums, temp, ans)
                    temp.pop()
            return ans

        return rec(nums)

        