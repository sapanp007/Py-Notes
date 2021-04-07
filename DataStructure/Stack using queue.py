from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def size(self):
        return len(self.container)

    def enque(self, data):
        self.container.appendleft(data)

    def deque(self):
        if self.size() > 0:
            return self.container.pop()
        else:
            raise Exception("No data in container")


class Stack(Queue):
    def push(self, data):
        self.enque(data)
        for _ in range(1, self.size()):
            x = self.deque()
            self.enque(x)

    def pop(self):
        return self.deque()


if __name__ == "__main__":
    s1 = Stack()
    s1.push(9)
    s1.push(8)
    s1.push(7)
    s1.push(6)
    s1.pop()
    print(s1.container)