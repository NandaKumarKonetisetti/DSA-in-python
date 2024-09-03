class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None
        

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            
    def prrintList(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node:
                print(current_node.data,end = ' ')
                current_node = current_node.next
            print()
    def insertAtParticularIndex(self,index,data):
        if self.head is None:
            return 
        else:
            new_node = Node(data)
            current = self.head
            ind = 1
            while ind<index and current:
                current = current.next
                ind +=1
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
    def delete_node(self,data):
        if self.head is None:
            return 
        current_node = self.head
        while current_node.data !=data:
            current_node = current_node.next
        if current_node is None:
            print(f"No node is there")
            return 
        if current_node == self.head: # Case 1: Node to be deleted is the head node
            self.head= self.head.next
            if self.head is not None:
                self.head.prev = None
        elif current_node.next is None:# Case 2: Node to be deleted is the tail node
            current_node.prev.next = None
        else:# Case 3: Node to be deleted is in the middle
            current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next

            
            
    def printReverseList(self):
        if self.head is None:
            return 
        else:
            current_node = self.head
            while current_node.next:
                current_node =current_node.next
            while current_node:
                print(current_node.data,end = ' ')
                current_node = current_node.prev
            print()


li = DoubleLinkedList()
li.prepend(0)
li.prepend(1)
li.append(2)
li.prepend(3)
li.append(9)
li.insertAtParticularIndex(2,11)
li.prrintList()
li.printReverseList()
li.deleteNode(1)
li.deleteNode(3)
li.deleteNode(9)
li.prrintList()
            