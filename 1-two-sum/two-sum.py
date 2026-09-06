class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #seen={}
        #for i in range (len(nums)):
         #   num= nums[i]
          #  difference = target-num
           # if difference in seen:
            #    return [seen[difference], i]
            #seen[num]= i
        #return []

        n= len(nums)
        for i in range (n):
            for j in range(i+1, n):
                if (nums[i]+nums[j]== target):
                    return [i,j]
        return []
