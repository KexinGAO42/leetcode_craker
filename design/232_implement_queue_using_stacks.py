"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""


class MyQueue:

    """
    Intuition:
    1. Use two stacks to implement a queue => can help us to get the first-in element by using stack_push[-1] or stack_push[-1]
        a. stack_push
        b. stack_pop
    2. One of the stacks will always be empty
    3. We keep a bool state to indicate which stack currently stores the numbers
    """

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
        self.in_pop_stack = 0 # if not state => numbers are stored in stack_push

    def push(self, x: int) -> None:
        if not self.in_pop_stack: # if numbers in push_stack
            self.stack_push.append(x)
        else:
            while self.stack_pop:
                self.stack_push.append(self.stack_pop.pop())
            self.stack_push.append(x)
            self.in_pop_stack = 0

    def pop(self) -> int:
        if self.in_pop_stack: # if numbers in pop_stack
            return self.stack_pop.pop()
        else: # values are stored in self.stack_push
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
            val = self.stack_pop.pop()
            self.in_pop_stack = 1
            return val

    def peek(self) -> int:
        if self.in_pop_stack:
            return self.stack_pop[-1]
        else:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
            self.in_pop_stack = 1
            return self.stack_pop[-1]

    def empty(self) -> bool:
        if self.stack_pop or self.stack_push:
            return False
        if not self.stack_pop and not self.stack_push:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()