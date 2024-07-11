class circularStack:
    def __init__(self,capacity):
        self.stack = [None]*capacity
        self.top = -1
        self.capacity = capacity
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return (self.top + 1 ) % self.capacity == 0 and self.top !=-1
        
    def push(self,data):
        if self.is_full():
            print("Stack is full")
        else:
            self.top = (self.top +1)%self.capacity
            self.stack[self.top] = data
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            item = self.stack[self.top]
            self.top = (self.top -1 + self.capacity)%self.capacity
            return item
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            current = self.top
            count =0
            while count<self.capacity:
                print(self.stack[current],end = " ")
                current = (current - 1 + self.capacity) % self.capacity
                count +=1
            print()
                
                
                
st = circularStack(6)
st.push(1)
st.push(2)
st.display()  # Output: Elements in the circularStack are: 2 1
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.display()  # Output: Elements in the circularStack are: 6 5 4 3 2 1
st.push(7)  