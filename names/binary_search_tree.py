import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, new_node):

        if new_node < self.value:
            # print(new_node, 'new node <', self.value)

            if self.left is None:
                self.left = BinarySearchTree(new_node)

            else:
                self.left.insert(new_node)

        else:
            # print(new_node, 'new node >', self.value)

            if self.right is None:
                self.right = BinarySearchTree(new_node)

            else:
                self.right.insert(new_node)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if target == self.value:
            return True
        
        elif target < self.value:

            if self.left is None:
                return False

            else:
                # print(target, 'less then', self.value, 'moving left')
                return self.left.contains(target)

        elif target > self.value:

            if self.right is None:
                return False

            else:
                # print(target, 'greater then', self.value, 'moving right')
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.right is None:
            return self.value
        else:
            # print(self.value, 'can move right')
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # # DAY 2 Project -----------------------


    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
            if node is None:
                return

            self.in_order_print(node.left) 
            print(node.value)
            self.in_order_print(node.right)


    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
        
    #     self.queue = Queue()
    #     self.queue.enqueue(node)

    #     while self.queue.size:
    #         node = self.queue.dequeue()
    #         print(node.value)
    #         if node.left:
    #             self.queue.enqueue(node.left)
    #         if node.right:
    #             self.queue.enqueue(node.right)


    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):

    #     self.stack = Stack()
    #     self.stack.push(node)

    #     while self.stack.size:
    #         node = self.stack.pop()
    #         print(node.value)
    #         if node.left:
    #             self.stack.push(node.left)
    #         if node.right:
    #             self.stack.push(node.right)


# test2 = BinarySearchTree(5)

# def test():
#     test2.insert(2)
#     test2.insert(3)
#     test2.insert(7)
#     test2.insert(1)
#     test2.insert(8)
#     test2.insert(9)
#     test2.bft_print(test2)

# print(test(), 'result')







    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
