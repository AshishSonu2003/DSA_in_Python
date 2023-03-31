class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    def replace_max(self, new_num):
        if self.headval is None:
            return
        max_node = self.headval
        current_node = self.headval
        while current_node is not None:
            if current_node.dataval > max_node.dataval:
                max_node = current_node
            current_node = current_node.nextval
        max_node.dataval = new_num
list = SLinkedList()
list.headval = Node(12)
list.AtEnd(95)
list.AtEnd(140)
list.AtEnd(110)
list.AtEnd(40)
print("Original list")
list.listprint()
list.replace_max(100)
print("New List")
list.listprint()