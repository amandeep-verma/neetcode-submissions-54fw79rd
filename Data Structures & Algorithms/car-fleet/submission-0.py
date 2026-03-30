class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        [(7, 1), (4, 2), (1, 2), (0, 1)]


        """

        posSpeed = [(pos,speed) for pos, speed in zip(position, speed)]
        posSpeed.sort(reverse = True)

        stack = []

        for p, s in posSpeed:
            if stack and stack[-1] >= (target- p)/s:
                continue
            stack.append((target- p)/s)

        
        return len(stack)

