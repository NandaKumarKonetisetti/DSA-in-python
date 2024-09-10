class Node:
    def __init__(self,value):
        self.value =value
        self.left = None
        self.right = None


def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def delete_node(root,key):
    if root is None:
        print(f"Value with node {key} is not present in tree")
        return 
    if key<root.value:
        root.left = delete_node(root.left,key)
    elif key>root.value:
        root.right = delete_node(root.right,key)
    else:
        #case 1 root with only one child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        #case 2 root with 2 child
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right,temp.value)
    return root
    
def find_min(root):
    if root :
        current = root
        while current.left is not None:
            current = current.left
        return current

def count_nodes(root):
    if root is not None:
        return 1+count_nodes(root.left)+count_nodes(root.right)

def pre_order(root):
    if root:
        print(root.value,end = ' ')
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.value,end = ' ')
        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value,end = ' ')

def search_element(root,key):
    if root is None:
        return False
    if root.value == key:
        return True
    if key>root.value:
        return search_element(root.right,key)
    else:
        return search_element(root.left,key)
root = Node(6)
insert(root,1)
insert(root,2)
insert(root,9)
insert(root,11)
insert(root,3)
pre_order(root)
print()
in_order(root)
print()
post_order(root)
print()
root = delete_node(root,6)
in_order(root)
print()

#Multiple searches in a tree
keys_to_search = [7, 10, 3, 8]
for key in keys_to_search:
    found = search_element(root, key)
    print(f"Key {key} found in BST: {found}")

