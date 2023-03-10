#!/usr/bin/env python3

"""
atds.py
Describes data structures used in class
"""

__author__ = "Sabrina Zhang"
__version__ = "2023-2-10"

class Stack(object):
    """
    Descrubes a stack with the peek, pop, and push methods as well as size() and isEmpty()
    """

    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        adds item to the end of the list, top of the stack
        """
        # you get to decide what's the top or bottom of the stack: 
        # stack = ["A," "B," "C,"] if using append, C -> top 
        self.stack.append(item)

    def pop(self):
        """
        Returns the last item in the list, aka the top of the stack 
        """
        #if len(self.stack) > 0:
        return self.stack.pop()


    def peek(self):
        # python going negative --> back to the bottom of stack
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        # T returned if True, F if not
        """
        if len(self.stack) == 0:
            return True
        else:
            return False
        """
        return len(self.stack) == 0 

    def __repr__(self):
        return super().__repr() + self.stack

class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)
        
    def dequeue(self):
        if (len(self.queue) > 0 ):
            self.queue.pop(0)
            
    def peek(self):
        if len(self.queue)>0: 
            return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __repr__(self):
        return "Queue" + str(self.queue)


class Deque(object):
    """
    Implements a double-ended queue where the front of the line is at index 0 and the tail end is -1. 
    """
    def __init__(self):
        self.deque = []
    
    # allows the 
    def add_front(self, item):
        self.deque.insert(0, item)

    def remove_front(self):
        if (len(self.deque) > 0):
            return self.deque.pop()

    def remove_rear(self):
        return self.deque.pop()

    #adds to the tailend/rearend
    def add_rear(self, item):
        self.deque.append(item)

    
    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0
    
    def __repr__(self):
        return "Deque" + str(self.deque)

class Node(object):
    # initalize 
    def __init__(self, data): 
        self.data = data
        self.next = None
        # want to set to none because you want to check if the next thing that we are poitning to is none or not (that way we know if we're at the end pf the unordered list or not)
        #unordered in the sense that it's not sorted!
        # this doesn't necessarily differ from a list, but it's unique in that it's our list with data values that "we" established... our specific datatypes, that is
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"


    



def main():
   # optional tester instructons here
   pass


if __name__ == "__main__":
    main()

