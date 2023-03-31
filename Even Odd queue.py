class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0
    
    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False
    
    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False
   
    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data
    
    def get_max_size(self):
        return self.__max_size
    
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
class QueueSeparator:
    def __init__(self, queue):
        self.queue = queue
        self.even_queue = Queue(queue.get_max_size())
        self.odd_queue = Queue(queue.get_max_size())

    def separate_even_odd(self):
        while not self.queue.is_empty():
            num = self.queue.dequeue()
            if num % 2 == 0:
                self.even_queue.enqueue(num)
            else:
                self.odd_queue.enqueue(num)
    def get_even_queue(self):
        return self.even_queue

    def get_odd_queue(self):
        return self.odd_queue



input_queue = Queue(8)
input_queue.enqueue(2)
input_queue.enqueue(7)
input_queue.enqueue(9)
input_queue.enqueue(4)
input_queue.enqueue(6)
input_queue.enqueue(5)
input_queue.enqueue(10)
separator = QueueSeparator(input_queue)
separator.separate_even_odd()

even_queue = separator.get_even_queue()
odd_queue = separator.get_odd_queue()
input_queue.display()

print("Odd Queue:")
odd_queue.display()

print("Even Queue:")
even_queue.display()