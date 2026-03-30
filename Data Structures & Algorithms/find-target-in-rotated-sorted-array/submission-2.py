class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r, = 0, len(nums)-1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] < nums[0]:
                r = m -1
            else:
                l = m+1
        
        inflection =  l if l < len(nums) else 0

        if target <= nums[-1]:
            nL, nR = inflection, len(nums)-1
        else:
            nL, nR = 0, inflection

        while nL <= nR:
            nM = nL + (nR- nL)//2

            if nums[nM]== target:
                return nM
            elif nums[nM]< target:
                nL = nM+1
            else:
                nR = nM -1

        return -1