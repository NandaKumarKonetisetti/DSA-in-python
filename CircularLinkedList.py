class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node =  self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
            self.head = new_node
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
    def insert_at_Middle(self,index,data):
        ind = 1
        new_node = Node(data)
        current_node = self.head
        while current_node.next!= self.head and ind<index:
            current_node = current_node.next
            ind+=1
        temp = current_node.next
        current_node.next= new_node
        new_node.next = temp
        
    
    def printlist(self):
        if self.head is None:
            return 
        else:
            current_node = self.head
            while True:
                print(current_node.data,end = ' ')
                current_node = current_node.next
                if current_node ==self.head:
                    break
            print("Head")
    
    def delete_node(self,data):
        if self.head is None:
            return 
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current_node = self.head
                while current_node.next != self.head:
                    current_node = current_node.next
                current_node.next = self.head.next
                self.head = self.head.next
                return 
        else:
            current = self.head
            while current.next !=self.head:
                if current.next.data == data:
                    current.next = current.next.next
                    return 
                current = current.next
                
            
li = LinkedList()
li.prepend(1)
li.prepend(2)
li.prepend(3)
li.prepend(4)
li.append(5)
li.insert_at_Middle(1,0)
li.delete_node(4)
li.delete_node(5)
li.delete_node(2)
li.printlist()
        
        
            
            
        
        