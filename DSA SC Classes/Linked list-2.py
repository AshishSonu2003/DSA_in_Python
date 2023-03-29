class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_node(self, value):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == value:
                if previous_node is None: 
                    self.head = current_node.next
                elif current_node.next is None: 
                    previous_node.next = None
                    self.tail = previous_node
                else:  
                    previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next
my_list = LinkedList()

my_list.insert_at_start(3)
my_list.insert_at_end(5)
my_list.insert_at_start(1)
my_list.insert_at_end(7)

my_list.traverse()

my_list.delete_node(3)

my_list.traverse()
