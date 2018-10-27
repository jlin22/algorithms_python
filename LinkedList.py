class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, collection=None):
        """Accepts an optional parameter collection, which contains initial
        values for the linked list. If it is None, then the linked list starts
        out empty."""
        if collection:
            self.head = None
            for item in collection:
                if self.head:
                    # inserting the next element
                    current.next = Element(item)
                    current = current.next
                else:
                    # inserting the first element of the linked list
                    self.head = Element(item)
                    current = self.head
        else:
            self.head = None

    def append(self, value):
        """Adds the value to the end of the linked list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Element(value)
        else:
            self.head = Element(value)

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None if the position is not in the list."""
        if position < 1:
            return None
        if position == 1:
            return self.head
        current = self.head
        for i in range(position - 1):
            if current.next:
                current = current.next
            else:
                return None
        return current.value

    def insert(self, value, position):
        """Inserts a node between the node at the current position - 1 and
        the node at current position with that value. 1 is the first position"""
        if position < 1:
            pass
        if position == 1:
            new_head = Element(value)
            new_head.next = self.head
            self.head = new_head
        else:
            current = self.head
            for i in range(position - 2):
                if current.next:
                    current = current.next
                else:
                    pass
            new_element = Element(value)
            new_element.next = current.next
            current.next = new_element

    def delete(self, value):
        """Delete the first node with a given value"""
        current = self.head
        if current.value == value:
            self.head = self.head.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next

    def __str__(self):
        """Prints the elements of the linked list in a python list manner"""
        a = ""
        current = self.head
        a += "["
        while current:
            a += str(current.value)
            if current.next:
                a += ", "
                current = current.next
            else:
                a += "]"
                break
        return a

if __name__ == "__main__":
    """I need to test more for edge cases and think about edge cases as the first
    thing I consider"""
    elements = [3, 4, 15, 2, 26, 11]
    numbers = LinkedList(elements)
    numbers.insert(6, 2)
    print(numbers)
    print(numbers.get_position(3))
    numbers.delete(15)
    print(numbers)
