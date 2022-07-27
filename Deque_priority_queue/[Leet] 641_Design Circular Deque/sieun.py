class MyCircularDeque(object):

    def __init__(self, k):
        # 원형 데크
        self.deque = [None] * k
        # 원형 데크 사이즈
        self.size = 0
        # 원형 데크 최대 사이즈
        self.maxSize = k
        # 원형 데크 front 현재 위치
        self.front = 0
        # 원형 데크 rear 현재 위치
        self.rear = -1

    def insertFront(self, value):
        # 꽉 찬 경우
        if self.isFull():
            return False
        else:
            self.front = (self.front - 1) % self.maxSize
            self.deque[self.front] = value
            self.size += 1
            return True

    def insertLast(self, value):
        # 꽉 찬 경우
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.deque[self.rear] = value
            self.size += 1
            return True

    def deleteFront(self):
        # 빈 경우
        if self.isEmpty():
            return False
        else:
            self.deque[self.front] = None
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return True

    def deleteLast(self):
        # 빈 경우
        if self.isEmpty():
            return False
        else:
            self.deque[self.rear] = None
            self.rear = (self.rear - 1) % self.maxSize
            self.size -= 1
            return True

    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize