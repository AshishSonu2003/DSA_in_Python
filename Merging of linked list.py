class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(list1, list2, n):
    if n == 0:
        return list2
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1
    temp = LinkedList(0)
    temp.next = list1
    curr = temp
    for i in range(n):
        curr = curr.next
    p = curr.next
    curr.next = list2
    while list2.next != None:
        list2 = list2.next
    list2.next = p
    return temp.next
list1 = LinkedList(1)
list1.next = LinkedList(2)
list1.next.next = LinkedList(4)
list1.next.next.next = LinkedList(3)
list1.next.next.next.next = LinkedList(5)
list2 =LinkedList(9)
list2.next = LinkedList(8)
list2.next.next = LinkedList(11)
merged = merge_lists(list1, list2, 2)
while merged != None:
    print(merged.val, end='->')
    merged = merged.next