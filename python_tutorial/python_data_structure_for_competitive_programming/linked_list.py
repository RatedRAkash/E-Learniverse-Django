from typing import Optional


class ListNode:
    # Using quotes ('ListNode') is required because the class is not yet fully defined at the time the type hint is interpreted.
    def __init__(self, val: Optional[int]=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class MyLinkedList:
    root: Optional[ListNode]

    def __init__(self, val: Optional[int]):
        self.root = ListNode(val)

    def add_node(self, val: int):
        current = self.root

        while current.next is not None:
            current = current.next

        current.next = ListNode(val)

    def delete_node(self, val_to_be_deleted: int):
        dummy = ListNode()
        dummy.next = self.root

        prev = dummy
        current = self.root

        while current is not None:
            if current.val == val_to_be_deleted:
                prev.next = current.next
                break

            prev = current
            current = current.next

        self.root = dummy.next

    def reverse_linked_list(self):
        current = self.root
        prev = None

        while current is not None:
            temp_next_node = current.next
            current.next = prev
            prev = current
            current = temp_next_node

        # as "current" is pointing to "null"... that means, "prev" is Pointing to the Last Node, so "prev" will be our New Root
        self.root = prev

    def print_linked_list(self):
        print("Linked List is:   ", end="") # Printing in the Same Line
        current = self.root

        while current is not None:
            print(current.val, end="")
            current = current.next

            # for Last Element we are Not Printing the "->"
            if current is not None:
                print("->", end="")

        # For Next Iteration of Printing we are Printing a "Single Line"
        print("")

if __name__ == "__main__":
    my_list = MyLinkedList(2)
    my_list.add_node(1)
    my_list.add_node(55)
    my_list.add_node(58)
    my_list.add_node(6)
    my_list.add_node(51)
    my_list.print_linked_list()

    my_list.delete_node(58)
    my_list.print_linked_list()

    my_list.reverse_linked_list()
    my_list.print_linked_list()