class MinStack:

    def __init__(self):
        self.stack = []
        self.minHolder = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minHolder.append(val if len(self.minHolder)==0 or val < self.minHolder[-1] else self.minHolder[-1]) 
        

    def pop(self) -> None:
        self.stack.pop()
        self.minHolder.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minHolder[-1]
        
