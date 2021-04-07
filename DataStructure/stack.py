"""
Stack is a LIFO
Use case:
1.when browsing multiple pages browser keeps track of the previous page and when we hit previous
it goes to the last visited page(LIFO).
2. When multiple functions are called python keep track of a stack, can be seen in debuger section
3. undo task

collection.deque can be used to faster append and pop

"""
from collections import deque


class Stack:
    def __init__(self):
        self.stack_list = deque()

    def size(self):
        return len(self.stack_list)

    def empty(self):
        if self.size() > 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        try:
            return self.stack_list.pop()
        except:
            return "stack empty"

    def top(self):
        if self.size() > 0:
            return self.stack_list[-1]
        else:
            return None


if __name__ == "__main__":
    s1 = Stack()
    s1.push(5)
    print(s1.top())
    print(s1.size())

    """Problem1 -  Reverse a string"""
    str1 = "we will conquere COVID-19"
    str2 = ""
    str_obj = Stack()
    for i in str1:
        str_obj.push(i)
    for _ in range(len(str1)):
        str2 += str_obj.pop()
    print(str2)

    """Problem2 -  valid paranthesis"""
    val1 = "({})"
    paren_obj = Stack()
    d1 = {'{': '}', '(': ')'}
    for i in val1:
        if i in d1.keys():
            paren_obj.push(i)
        elif i == d1[paren_obj.top()]:
            pop_val = paren_obj.pop()
    print(True if paren_obj.size() == 0 else False)
