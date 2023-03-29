class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def AtBeginning(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode
    def AtEnd(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=NewNode
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentined node is absent")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3 
list.AtBeginning("sun")
list.AtEnd("Sat")
list.Inbetween(list.headval.nextval.nextval.nextval,"Thu")
list.Inbetween(list.headval.nextval.nextval.nextval.nextval,"Fri")
list.listprint()