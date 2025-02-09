# # initialize_LL.py

# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# def take_input():
#     head = None
#     tail = None

#     while True:
#         value = int(input("Enter value (-1 to stop): "))
#         if value == -1:
#             break

#         newNode = Node(value)

#         if head is None:
#             head = newNode
#             tail = newNode
#         else:
#             tail.next = newNode
#             tail = newNode

#     return head

# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")  # Indicate end of linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_from_list(self, values):
        """Create a linked list from a given Python list"""
        if not values:
            return
        
        self.head = Node(values[0])  # Initialize head
        temp = self.head

        for value in values[1:]:
            temp.next = Node(value)  # Create new node
            temp = temp.next  # Move temp forward

    def get_length(self):
        """Find the length of the linked list"""
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        """Print the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

