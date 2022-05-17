# For your reference:
#
class SinglyLinkedListNode:

    def __init__(self, dataval):
        self.data = dataval
        self.next = None
    
    def __init__(self, dataval, nextNode):
        self.data = dataval
        self.next = nextNode
#
#
def mergeLists(head1, head2):

    newHead = SinglyLinkedListNode(min(head1.data, head2.data))

    dummy = newHead

    if min(head1.data, head2.data) == head1.data:
        head1 = head1.next
    else:
        head2 = head2.next

    while head1 or head2:

        if not head1:
            dummy.next = SinglyLinkedListNode(head2.data)
            dummy = dummy.next
            head2 = head2.next
        elif not head2:
            dummy.next = SinglyLinkedListNode(head1.data)
            dummy = dummy.next
            head1 = head1.next

        elif head1.data >= head2.data:
            dummy.next = SinglyLinkedListNode(head2.data)
            dummy = dummy.next
            head2 = head2.next
        
        else:
            dummy.next = SinglyLinkedListNode(head1.data)
            dummy = dummy.next
            head1 = head1.next

    return newHead