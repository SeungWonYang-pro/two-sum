from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        ans = [0,0]
        st = 0
        ed = 0
        cursum = nums[0]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if((nums[i]+nums[j]) == target):
                    ans[0]=i
                    ans[1]=j
                    break

        return ans
