class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, collection):
        self.head = None
        for item in collection:
            if not self.head:
                self.head = Element(item)
                current = self.head 
            else:
                current.next = Element(item)
                current = current.next

    def append(self, value):
        current = self.head
        # don't forget about if there's no elements in the list
        if self.head:
            while current.next:
                current = current.next
            current.next = Element(value)
        else:
            self.head = Element(value)

    def iterate(self):
        elements = []
        current = self.head
        if self.head:
            while current:
                elements.append(current.value)
                current = current.next
        return elements

    def get_position(self, position):
        # 1 is the beginning
        if position < 1:
            return None
        elif position == 1:
            return self.head.value
        else:
            current = self.head
            for i in range(position - 1):
                if current.next:
                    current = current.next
                else:
                    return None
            return current.value

    def insert(self, value, position):
        # between nodes position and position + 1  
        # find the positionth element
        if position < 1:
            return
        current = self.head
        for i in range(position - 1):
            if current.next:
                current = current.next
            else:
                return
        new_element = Element(value)
        new_element.next = current.next
        current.next = new_element            
            
collection = [1, 2, 6, 7, 4, 5]
a = LinkedList(collection)
a.append(1)
print(a.iterate())
print(a.get_position(3))
print(a.get_position(0))
print(a.get_position(6))
print(a.iterate())
a.insert(5, 1)
a.insert(11, 3)
print(a.iterate())

