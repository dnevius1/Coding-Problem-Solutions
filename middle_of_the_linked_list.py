from linked_list import LinkedList

# The code in "linked_list.py" can be used to create a linked list out of a list. 
# The code in "linked_list_traversal.py" can be used to traverse the linked list.
# The code in "linked_list_reversal.py" can be used to reverse the linked list.

def get_middle_node(head):
    if head is None:
        return None
    
    # Create slow and fast pointers at head.
    slow, fast = head, head

    # Iterate through linked list until 'fast'
    # pointer reaches the end. 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # When fast pointer reachest the end of the 
        # linked list, slow pointer is in the middle. 
        # Slow pointer is returned.
        if fast == None or fast.next == None:
            return slow
    
    
    return head
