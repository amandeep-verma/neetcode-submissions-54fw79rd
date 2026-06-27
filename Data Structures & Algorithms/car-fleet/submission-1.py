class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        Sol 1 - Monotonic decreasing order of stack
        zip postion and speed in list.
        Sort them in order of position. So now a car ahead in positon can only be joined by another car if
        its time time reach the target is before the car ahead. Use this logic to remove the car (add to fleet)
        else add it to stack. Now next car is checked against this car
        O(n logn) 
        """

        posSpeed = [(pos,speed) for pos, speed in zip(position, speed)]
        posSpeed.sort(reverse = True)

        stack = []

        for p, s in posSpeed:
            if stack and stack[-1] >= (target- p)/s:
                continue
            stack.append((target- p)/s)

        
        return len(stack)

