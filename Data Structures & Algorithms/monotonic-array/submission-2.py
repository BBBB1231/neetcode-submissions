class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ascd = None
        desc = None

        for i in range(1,len(nums)):
            #lst = []

            # increasing
            if nums[i] > nums[i-1]:
                ascd = True
    
            # decreasing
            elif nums[i] < nums[i-1]:
                desc = True

            else:
                pass

        if ascd and desc:
            return False
        else:
            return True