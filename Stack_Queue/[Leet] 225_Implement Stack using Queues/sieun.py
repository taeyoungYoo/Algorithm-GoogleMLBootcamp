class MyStack(object):
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            value = self.q.popleft()
            self.q.append(value)

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q
