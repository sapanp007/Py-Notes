class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        level = self.get_level()
        prefix = " " * level * 2
        if level > 0:
            prefix = prefix + "|__"
        print(f"{prefix}{self.data}")
        for child in self.children:
            child.print_tree()

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


if __name__ == "__main__":
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptops")
    cell = TreeNode("Cell")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("windows"))
    laptop.add_child(TreeNode("linux"))
    cell.add_child(TreeNode("iphone"))
    cell.add_child(TreeNode("android"))
    cell .add_child(TreeNode("google pixel"))
    root.add_child(laptop)
    root.add_child(cell)
    root.print_tree()
