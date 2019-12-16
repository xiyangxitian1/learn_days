# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
class MinStack:
    """
    这样效率太低了
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = list()
        self.helper = list()

    def push(self, x: int) -> None:
        if not self.helper or self.helper[-1] >= x:
            self.helper.append(x)
        self.list.append(x)

    def pop(self) -> None:
        pop_num = self.list.pop()
        if self.helper[-1] == pop_num:
            self.helper.pop()

    def top(self) -> int:
        return self.list[-1] if self.list else None

    def getMin(self) -> int:
        return self.helper[-1] if self.helper else None
