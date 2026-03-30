class MinStack:
    
    class Node:
         def __init__(self, val = None, Node = None, minE = None):
            self.val = val
            self.next = Node
            self.minE = minE

    first = None
    size = None
    def __init__(self):
        self.first = self.Node()
        self.size = 0

    def push(self, val: int) -> None:
        second = self.first
        minE = min(val, second.minE) if self.first.val != None else val
        
        self.first = self.Node(val, second, minE)
        self.size += 1


    def pop(self) -> None:
        if self.size:
            self.first = self.first.next
            self.size -= 1
        

    def top(self) -> int:
        if self.size:
            return self.first.val
            
    def getMin(self) -> int:
        
        return self.first.minE
        
