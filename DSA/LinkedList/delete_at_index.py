# delete_at_index.py

from initialize_LL import print_linked_list, take_input


def delete_at_index(head,index):
    if(head is None):
        return None
    if(index == 0):
        return head.next
    temp = head
    count = 0
    while(temp is not None and count < index-1):
        temp=temp.next
        count+=1
    if(temp is None or temp.next is None):
        return head
    temp.next = temp.next.next
    return head

def delete_at_index_recursive(head,index):
    if(head is None):
        return None
    if(index is 0):
        return head.next

    head.next = delete_at_index_recursive(head.next, index-1)
    return head

head = take_input()
print_linked_list(head)
head = delete_at_index_recursive(head,2)
print_linked_list(head)
