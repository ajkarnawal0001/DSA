# initialize_LL.py

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def take_input():
    head = None
    tail = None

    while True:
        value = int(input("Enter value (-1 to stop): "))
        if value == -1:
            break

        newNode = Node(value)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")  # Indicate end of linked list
