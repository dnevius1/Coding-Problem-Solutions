from linked_list import LinkedList

def detect_cycle(head):

   if head is None:
      return False
   # Set both pointers equal to the head
   # of the linked list. 
   fast, slow = head, head

   # 'Fast' moves twice as fast as 'slow'. If
   # 'fast' is ever equal to 'slow', returns
   # true because a cycle exists. Otherwise,
   # returns false when 'fast' = NULL.
   while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
         return True

   return False