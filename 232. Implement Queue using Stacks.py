class MyQueue:

    def __init__(self):
        self.array=[]
        

    def push(self, x: int) -> None:
        return self.array.append(x)
        

    def pop(self) -> int:
        return self.array.pop(0)
        

    def peek(self) -> int:
        return self.array[0]
        

    def empty(self) -> bool:
        try:
            self.array[0]
            return False
        except:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()