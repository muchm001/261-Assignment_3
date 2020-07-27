# Course: CS261 - Data Structures
# Student Name: Michael Uchmanowicz
# Assignment: A3 P4
# Description: a Queue ADT


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()        # use as main storage
        self.s2 = MaxStack()        # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        Removes and returns the value from the beginning of the queue. It must be
        implemented with the runtime complexity of not worse than O(n).
        If the queue is empty, the method raises a custom “QueueException”.
        """
        if self.s1.is_empty():
            raise QueueException
        else:
            i = self.s1.size()
            while i >= 1:
                if i > 1:
                    self.s2.push(self.s1.pop())
                    i -= 1
                else:
                    val = self.s1.pop()
                    t = 0
                    org_size = self.s2.size()
                    while t < org_size:
                        self.s1.push(self.s2.pop())
                        t += 1
                    return val

    def is_empty(self) -> bool:
        """
        Returns True if there are no elements in the queue. Otherwise it returns False
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Returns the number of elements currently in the queue
        """
        return self.s1.size()




# BASIC TESTING
if __name__ == "__main__":

    # print('\n# enqueue example 1')
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)


    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    #
    #
    # print('\n# is_empty example 1')
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(10)
    # print(q.is_empty())
    # q.dequeue()
    # print(q.is_empty())
    #
    #
    # print('\n# size example 1')
    # q = Queue()
    # print(q.size())
    # for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    # print(q.size())



