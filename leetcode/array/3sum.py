'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
'''

import time


class MySolution:
    def threesum(self, nums):

        start = time.perf_counter()
        lengthArray = len(nums)
        finalSet = set()
        nums = sorted(nums)

        for i in range(lengthArray):
            for j in range(lengthArray):

                if i == j:
                    continue

                for k in range(lengthArray):

                    if i == k or j == k:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = (nums[i], nums[j], nums[k])
                        finalSet.add((nums[i], nums[j], nums[k]))
        result = list()
        for element in finalSet:
            result.append(list(element))
        end = time.perf_counter()
        print("Time required is {:0.2f} seconds".format(end-start))
        return result


if __name__ == "__main__":
    mySolution = MySolution()
    nums = [2, 13, -2, -5, -1, 10, 6, -8, 5, -5, 7, -5, -14, -4, -5, 10, -15, -2, -14, -6, 10, 6, -14, -14, -9, -11,
            8, -3, -2, 12, -9, -14, 3, 5, -12, -13, -8, 1, -14, 12, 12, 0, 14, 5, 4, -14, -8, 4, -9, -7, 14, -13, 6,
            7, -12, 5, 12, 11, -13, -5, 0, -6, -12, -12, 6, 13, 12, 13, 0, 5, 2, -11, 13, 1, 9, 2, 2, -14, 13, 8, -14,
            4, 2, 8, -3, -3, -10, -14, -15, 14, -12, 1, -15, 14, -4, 6, 12, -6, -4, -3, 6, 5]
    print(mySolution.threesum(nums))
