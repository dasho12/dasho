class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

    def find_min(self):
        return self._find_min_rec(self.root)

    def _find_min_rec(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self):
        return self._find_max_rec(self.root)

    def _find_max_rec(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.val

# Жишээгээр модонд утгуудыг нэмэх, хайх, хамгийн бага, хамгийн их утгыг олох:
bst = BinarySearchTree()
input_values = [20, 9, 25, 5, 12, 15,30]

for value in input_values:
    bst.insert(value)

# Утгуудыг хайх
print("Minimum value:", bst.find_min())  # Minimum value: 5
print("Maximum value:", bst.find_max())  # Maximum value: 25

# Хайлт хийх
search_value = 21
result = bst.search(search_value)
if result:
    print("Search:", search_value, "Found")
else:
    print("Search:", search_value, "Not found")

search_value = 18
result = bst.search(search_value)
if result:
    print("Search:", search_value, "Found")
else:
    print("Search:", search_value, "Not found")