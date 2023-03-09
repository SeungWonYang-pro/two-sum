from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    ans = [0,0]
    st = 0
    ed = 0
    cursum = nums[0]
    while 1:
        if(cursum==target):
            break
        if(st==ed):
            ed=ed+1
            cursum = cursum + nums[ed]
        else:
            if(cursum < target):
                ed=ed+1
                cursum = cursum + nums[ed]
            if(cursum > target):
                cursum = cursum - nums[st]
                st = st+1
        
        
    ans[0]= st
    ans[1] = ed
    return ans
