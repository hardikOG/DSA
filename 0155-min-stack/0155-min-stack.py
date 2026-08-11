class MinStack(object):

    def __init__(self):
        self.st = []
        self.st2 = [float('inf')]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.st.append(value)
        self.st2.append(min(value, self.st2[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()
        self.st2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.st2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()