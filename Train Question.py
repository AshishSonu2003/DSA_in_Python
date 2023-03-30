class Compartment:
    def __init__(self, name, capacity, passengers):
        self.name = name
        self.capacity = capacity
        self.passengers = 0

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_passengers(self):
        return self.passengers

    def is_vacant(self):
        return self.passengers < self.capacity
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        elif index >= self.length:
            self.append(data)
        else:
            new_node = Node(data)
            leader = self.traverse_to_index(index - 1)
            holding_pointer = leader.next
            leader.next = new_node
            new_node.next = holding_pointer
            self.length += 1




class Train:
    def __init__(self, train_name, compartment_list=None):
        self.train_name = train_name
        self.compartment_list = LinkedList()

        if compartment_list is not None:
            for compartment in compartment_list:
                self.add_compartment(compartment)

    def add_compartment(self, compartment):
        if isinstance(compartment, Compartment):
            self.compartment_list.append(compartment)
        else:
            print("Invalid compartment object")

    def remove_compartment(self, name):
        current_node = self.compartment_list.head
        prev_node = None

        while current_node is not None:
            if current_node.data.get_name() == name:
                if prev_node is None:
                    self.compartment_list.head = current_node.next
                else:
                    prev_node.next = current_node.next
                return True
            else:
                prev_node = current_node
                current_node = current_node.next

        print(f"Compartment {name} not found")
        return False

    def insert_compartment_at_beginning(self, compartment):
        if isinstance(compartment, Compartment):
            self.compartment_list.prepend(compartment)
        else:
            print("Invalid compartment object")

    def insert_compartment_at_end(self, compartment):
        if isinstance(compartment, Compartment):
            self.compartment_list.append(compartment)
        else:
            print("Invalid compartment object")

    def insert_compartment_at_position(self, compartment, position):
        if isinstance(compartment, Compartment):
            self.compartment_list.insert(position, compartment)
        else:
            print("Invalid compartment object")


 

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        compartments = []
        current_node = self.compartment_list.head

        while current_node is not None:
            compartments.append(current_node.data)
            current_node = current_node.next

        return compartments


    def check_vacancy(self):
        count = 0
        current_node = self.compartment_list.head

        while current_node is not None:
            if current_node.data.is_vacant():
                count += 1
            current_node = current_node.next

        return count
train = Train("Express", [])
compartment1 = Compartment("A1", 50, 30)
compartment2 = Compartment("A2", 40, 20)
train.add_compartment(compartment1)
train.add_compartment(compartment2)
num_vacant_compartments = train.check_vacancy()
print("Compartments with more than 50% vacancy:", num_vacant_compartments)
train.remove_compartment("A2")
compartment3 = Compartment("B1", 30, 10)
train.insert_compartment_at_beginning(compartment3)
compartment4 = Compartment("C1", 60, 40)
train.insert_compartment_at_end(compartment4)
compartment_list = train.get_compartment_list()
for compartment in compartment_list:
    print(compartment.get_name(), compartment.get_capacity(), compartment.get_passengers())
