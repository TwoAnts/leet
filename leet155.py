#!/usr/bin/env python3
#-*- coding : utf-8-*-

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_num_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        min_num = x
        if self.min_num_stack:
            min_num = min(self.min_num_stack[-1], min_num)
        self.min_num_stack.append(min_num)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return
        self.min_num_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.min_num_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()