class circularQueue:
    def __init__(self,capacity):
        self.queue = [None]*capacity
        self.capacity = capacity
        self.front = self.rear = -1
    
    def is_full(self):
        return (self.rear+1)%self.capacity==self.front
        
    def is_empty(self):
        return (self.front ==-1 and self.rear ==-1)
    
    def enqueue(self,data):
        if self.is_full():
            print("queue is full")
        elif self.is_empty():
            self.front = self.rear =0
            self.queue[self.rear]=data
        else:
            self.rear = (self.rear+1)%self.capacity
            self.queue[self.rear]=data
    
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        elif self.front==self.rear:
            item = self.queue[self.rear]
            self.front=self.rear =-1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front+1)%self.capacity
            return item
            
    def printqueue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            current = self.front
            
            while True:
                print(self.queue[current],end = ' ')
                if current==self.rear:
                    break
                current = (current +1)%self.capacity
               
            print()
            


q = circularQueue(6)
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.printqueue()
q.enqueue(7)
q.printqueue()
        