class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self, top=None):
        """Creates a singly linked list with no elements in it"""
        self.top = top

    def push(self, value):
        """Puts a new node with the value at the front of the linked list (top
        of stack"""
        #never forget edge cases!
        if not self.top:
            self.top = Element(value)
        else:
            new_top = Element(value)
            new_top.next = self.top
            self.top = new_top

    def pop(self):
        """Deletes the element at the top of the stack and returns the value"""
        #same here, never forget edge cases!
        value = self.top.value
        if not self.top.next:
            self.top = None
        else:
            self.top = self.top.next
        return value

    def __str__(self):
        """List of values in the linked list from top to bottom"""
        a = "["
        current = self.top
        while current:
            if current.next:
                a += "{}, ".format(current.value)
            else:
                a += "{}]".format(current.value)
            current = current.next
        return a

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s)
    print(s.pop())
