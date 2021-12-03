class Stack:
    def __init__(self):
        self.__element = []

    # Return True if the stack is empty
    def isEmpty(self):
        return len(self.__element) == 0

    # Return the element an the top of the stack
    # without removing it from the stack
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__element[len(self.__element) - 1]

    # Store an element at the top of the stack
    def push(self, element):
        self.__element.append(element)

    # Remove the element at the top of the stack and return it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__element.pop()

    # Return the size of the stack
    def getSize(self):
        return len(self.__element)
