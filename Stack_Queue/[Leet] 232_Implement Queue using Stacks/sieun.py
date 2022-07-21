class MyQueue(object):
    def __init__(self):
        self.stack1 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        stack2 = []

        while len(self.stack1) > 1:
            value = self.stack1.pop()
            stack2.append(value)

        result = self.stack1.pop()

        while stack2:
            value = stack2.pop()
            self.stack1.append(value)

        return result

    def peek(self):
        stack2 = []

        while self.stack1:
            value = self.stack1.pop()
            stack2.append(value)

        result = value

        while stack2:
            value = stack2.pop()
            self.stack1.append(value)

        return result

    def empty(self):
        return not self.stack1