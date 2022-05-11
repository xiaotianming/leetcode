"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有push to top,peek/pop from top,size, 和is empty操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return None
        elif len(self.stack2) == 0 and len(self.stack1) >= 0:
            for i in range(0, len(self.stack1)):
                self.stack2.append(self.stack1.pop(-1))
            return self.stack2.pop(-1)
        else:
            return self.stack2.pop(-1)

    def peek(self) -> int:
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return None
        elif len(self.stack2) == 0 and len(self.stack1) >= 0:
            for i in range(0, len(self.stack1)):
                self.stack2.append(self.stack1.pop(-1))
            tmp = self.stack2.pop(-1)
            self.stack2.append(tmp)
            return tmp
        else:
            tmp = self.stack2.pop(-1)
            self.stack2.append(tmp)
            return tmp
        """
        Get the front element.
        """

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())