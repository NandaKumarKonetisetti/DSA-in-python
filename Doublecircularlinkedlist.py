class Node:
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None


class DoubleCircularLinkedlist:
    def __init__(self):
        self.head = None
    
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
           tail = self.head.prev
           new_node.next = self.head
           new_node.prev = tail
           self.head.prev = new_node
           tail.next = new_node
           self.head = new_node
            
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
           tail = self.head.prev
           tail.next = new_node
           new_node.prev = tail
           new_node.next = self.head
           self.head.prev = new_node
    
    def delete_node(self,data):
            if self.head is None:
                return 
            current_node = self.head
            while current_node.data !=data:
                current_node = current_node.next
                if current_node ==self.head:
                    print(f"Node with data {data} not found")
                    return 
                    
            if current_node.next == current_node:  # case 1 : only one node 
                self.head = None
            elif current_node == self.head:  # case 2 : deleting the head node
                last = self.head.prev 
                last.next = self.head.next
                self.head = self.head.next
                self.head.prev = last 
            else: #case 3 deleting other node
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
    
                    
                    
                
    def printList(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while True:
                print(current_node.data,end = ' ')
                if current_node.next == self.head:
                    break
                current_node = current_node.next
            print("Head")
    def printReverselist(self):
        if self.head is None:
            return
        else:
            tail = self.head.prev
            current_node = tail
            while True:
                print(current_node.data,end = ' ')
                if current_node.prev == tail:
                    break
                current_node = current_node.prev
            print("Head")
        
li = DoubleCircularLinkedlist()
li.prepend(0)
li.prepend(1)
li.prepend(2)
li.append(3)
li.append(4)
li.append(5)
li.printList()
li.printReverselist()
li.delete_node(5)
print("Node Deleted")
li.printList()
li.printReverselist()
            
            