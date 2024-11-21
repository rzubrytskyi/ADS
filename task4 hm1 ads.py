class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.front is not None:
            return self.front.data
        else:
            print("Queue is empty")
            return None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                # Node found
                if current.prev:
                    current.prev.next = current.next
                else:
                    # Deleting the head node
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    # Deleting the tail node
                    self.tail = current.prev
                return
            current = current.next
        print(f"Data {data} not found in the list.")

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Forward:", elements)

    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        print("Backward:", elements)

### Tests for queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Is queue empty?", queue.is_empty())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Is queue empty?", queue.is_empty())

### Tests for DoublyLinkedList
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)
dll.prepend(1)

dll.display_forward()
dll.display_backward()

dll.delete(10)
dll.display_forward()
dll.display_backward()

dll.delete(100)