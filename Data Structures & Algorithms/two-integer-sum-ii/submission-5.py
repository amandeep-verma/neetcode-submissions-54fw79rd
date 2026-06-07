class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(0, len(numbers)):
            comp = target - numbers[i]
            for j in range(i+1, len(numbers)):
               
                if comp == numbers[j]:
                    return [i+1, j+1]
                if comp < numbers[j]:
                    break

        return []