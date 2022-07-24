class MyCircularQueue(object):

    def __init__(self, k):
        # 원형 큐
        self.q = [None] * k
        # 원형 큐 사이즈
        self.size = 0
        # 원형 큐 최대 사이즈
        self.maxSize = k
        # 원형 큐 front 현재 위치
        self.front = 0
        # 원형 큐 rear 현재 위치
        self.rear = -1

    def enQueue(self, value):
        # 꽉 찬 경우
        if self.isFull():
            return False
        # enqueue
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.q[self.rear] = value
            self.size += 1
            return True

    def deQueue(self):
        # 빈 경우
        if self.isEmpty():
            return False
        # dequeue
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return True

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.q[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.q[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize
