class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_At_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insert_At_End(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_particular_index(self,index,data):
        
        if self.head is None:
            print("LinkedList is empty")
        elif index == 0:
            self.insert_At_begining(data)
        else:
            current = self.head
            ind = 1
            new_node = Node(data)
            while ind<index:
                current = current.next
                ind +=1
            new_node.next = current.next
            current.next = new_node
            
    def delete_node(self,data):
        if self.head is None:
            return
        elif self.head.data==data:
            self.head =self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return 
                current = current.next
                
    def printlist(self):
         if self.head is None:
             return 
         else:
             current = self.head 
             while current:
                 print(current.data,end = ' ')
                 current = current.next
             print()
    def reverse_list(self):
        current =self.head
        prev = None
        while current:
            new_node =current.next
            current.next = prev
            prev = current
            current=new_node
        self.head = prev
    
            
            
            
li = LinkedList()
li.insert_At_begining(1)
li.insert_At_begining(2)
li.insert_At_begining(3)
li.insert_At_begining(4)
li.insert_At_End(9)
li.insert_particular_index(2,11)
li.printlist()
li.delete_node(9)
li.printlist()
li.delete_node(11)
li.printlist()
li.reverse_list()
li.printlist()
                