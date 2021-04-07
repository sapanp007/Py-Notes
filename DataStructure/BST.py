"""
Utility:
    create a set type of class as it doesn't have duplicates
    returns elements in ascending or descending order
"""


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        # elements = self.in_order_traversal()
        # return sum(elements)
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def delete(self, val):
        if self.data == val:
            if self.left:
                max_value = self.left.find_max()
                self.data = max_value
                self.left.delete(max_value)
            elif self.right:
                min_value = self.right.find_min()
                self.data = min_value
                self.right.delete(min_value)
            else:
                self.data = None
        elif val < self.data:
            self.left.delete(val)
        else:
            self.right.delete(val)


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for idx in range(1, len(elements)):
        root.add_child(elements[idx])
    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print((numbers_tree.search(34)))
    print((numbers_tree.find_min()))
    print((numbers_tree.find_max()))
    print((numbers_tree.calculate_sum()))
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())


