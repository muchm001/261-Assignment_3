# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


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
        TODO: Write this implementation
        """
        return

    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        """
        return 0

    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0




# BASIC TESTING
if __name__ == "__main__":

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


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


    print('\n# is_empty example 1')
    q = Queue()
    print(q.is_empty())
    q.enqueue(10)
    print(q.is_empty())
    q.dequeue()
    print(q.is_empty())


    print('\n# size example 1')
    q = Queue()
    print(q.size())
    for value in [1, 2, 3, 4, 5, 6]:
        q.enqueue(value)
    print(q.size())



