# Course: CS261 - Data Structures
# Student Name: Michael Uchmanowicz
# Assignment: A3 P1
# Description:

class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel).
        """
        new_node_next = self.head.next
        self.head.next = SLNode(value)
        self.head.next.next = new_node_next

        return

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (right before the back sentinel)
        """
        cur = self.head
        pre = None
        while cur.next is not None:
            pre = cur
            cur = cur.next
        else:
            pre.next = SLNode(value)
            pre.next.next = self.tail
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
         Adds a new value at the specified index position in the linked list. Index 0
            refers to the beginning of the list (right after the front sentinel).
            If the provided index is invalid, the method raises a custom “SLLException”.
        """
        if index < 0:
            raise SLLException
        else:
            cur = self.head.next
            pre = None
            cur_index = 0
            while cur_index < index:
                pre = cur
                cur = cur.next
                cur_index += 1
                if pre == self.tail:
                    raise SLLException
            else:
                if index == 0:
                    self.head.next = SLNode(value)
                    self.head.next.next = cur
                else:
                    pre.next = SLNode(value)
                    pre.next.next = cur
        return

    def remove_front(self) -> None:
        """
        Removes the first node from the list. If the list is empty, the method raises a
        custom “SLLException”
        """
        if self.head.next == self.tail:
            raise SLLException
        else:
            new_node_next = self.head.next.next
            self.head.next = new_node_next

        return

    def remove_back(self) -> None:
        """
        Removes the last node from the list. If the list is empty, the method raises a
        custom “SLLException”
        """
        if self.head.next == self.tail:
            raise SLLException
        else:
            cur = self.head
            pre = None
            while cur.next != self.tail:
                pre = cur
                cur = cur.next
            else:
                pre.next = pre.next.next
        return

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index. Index 0 refers to the beginning
        of the list.
        If the provided index is invalid, the method raises a custom “SLLException”
        """
        if self.head.next == self.tail or index < 0:
            raise SLLException
        else:
            cur = self.head.next
            pre = None
            cur_index = 0

            while cur_index < index:
                pre = cur
                cur = cur.next
                cur_index += 1
                if pre == self.tail:
                    raise SLLException
            else:
                if cur == self.tail:
                    raise SLLException
                if cur == self.head.next:
                    self.head.next = cur.next
                else:
                    pre.next = cur.next
        return

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without removing it. If the list is
        empty, the method raises a custom “SLLException”
        """
        if self.head.next == self.tail:
            raise SLLException
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        Returns value from the last node in the list without removing it. If the list is
        empty, the method raises a custom “SLLException”
        """
        if self.head.next == self.tail:
            raise SLLException
        else:
            cur = self.head
            pre = None
            while cur.next is not None:
                pre = cur
                cur = cur.next
            else:
                return pre.value

    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end and removes the first node in
        the list that matches the provided “value” object. Method returns True if some node was
        actually removed from the list. Otherwise it returns False
        """
        if self.head.next == self.tail:
            return False
        else:
            cur = self.head.next
            cur_index = 0

            while cur.value != value:
                cur = cur.next
                cur_index += 1
                if cur == self.tail:
                    return False
            else:
                self.remove_at_index(cur_index)
                return True

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value”
        object
        """
        cur = self.head.next
        value_count = 0

        while cur != self.tail:
            if cur.value == value:
                value_count += 1
            cur = cur.next
        else:
            return value_count

    def get_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index. Index 0 refers to the beginning
         of the list.
        If the provided index is invalid, the method raises a custom “SLLException”
        """
        if self.head.next == self.tail or index < 0:
            raise SLLException
        else:
            cur = self.head.next
            pre = None
            cur_index = 0

            while cur_index < index:
                pre = cur
                cur = cur.next
                cur_index += 1
                if pre == self.tail:
                    raise SLLException
            else:
                if cur == self.tail:
                    raise SLLException
                else:
                    return cur.value

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList object that contains the requested number of nodes
        from the original list starting with the node located at the requested start index. If the
        original list contains N nodes, valid start_index is in range [0, N - 1] inclusive.
        If the provided start index is invalid, or if there are not enough nodes between start index
        and end of the list to make the slice of requested size, this method raises a custom
        “SLLException”.
        """
        if start_index > self.length() - 1 or start_index + size - 1 > self.length() - 1:
            raise SLLException
        else:
            new = LinkedList()
            slice_end = start_index + size
            cur_index = start_index
            while cur_index < slice_end:
                new.add_back(self.get_at_index(cur_index))
                cur_index += 1
            else:
                return new

    def is_sorted(self) -> int:
        """
        Returns an integer that describes whether the linked list is sorted. Method
        should return 1 if the list is sorted in strictly ascending order. It should return 2 if the list is
        sorted in strictly descending order. Otherwise the method should return 0.
        Empty list and list consisting of a single node is considered sorted in strictly ascending
        order.
        """

        if self.head.next == self.tail or self.head.next.next == self.tail:
            return 1
        else:
            cur = self.head.next
            if cur.value > cur.next.value:
                sort = 2
                cur = cur.next
            elif cur.value < cur.next.value:
                sort = 1
                cur = cur.next
            while sort > 0:
                if sort == 2:
                    if cur.next == self.tail:
                        return sort
                    if cur.value < cur.next.value:
                        return 0
                    else:
                        cur = cur.next
                if sort == 1:
                    if cur.next == self.tail:
                        return sort
                    if cur.value > cur.next.value or cur.value == cur.next.value:
                        return 0
                    else:
                        cur = cur.next

            else:
                return 0

    def length(self) -> int:
        """
        Returns the number of nodes in the list.
        """
        if self.head.next == self.tail:
            return 0
        else:
            cur = self.head.next
            cur_index = 0

            while cur.next != self.tail:
                cur = cur.next
                cur_index += 1
            else:
                cur_index += 1
                return cur_index

    def is_empty(self) -> bool:
        """
        Returns True if the list has no data nodes. Otherwise, it returns False
        """
        if self.head.next == self.tail:
            return True
        else:
            return False


if __name__ == '__main__':
    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)

    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)

    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)

    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)

    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_front example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())

    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)

    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))

    print('\n# get at index example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.get_at_index(0), list.get_at_index(1), list.get_at_index(2), list.get_at_index(3),
          list.get_at_index(4), list.get_at_index(5))

    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")

    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200]
    )
    for case in test_cases:
        list = LinkedList(case)
        print('Result:', list.is_sorted(), list)

    print('\n# is_empty example 1')
    list = LinkedList()
    print(list.is_empty(), list)
    list.add_back(100)
    print(list.is_empty(), list)
    list.remove_at_index(0)
    print(list.is_empty(), list)

    print('\n# length example 1')
    list = LinkedList()
    print(list.length())
    for i in range(800):
        list.add_front(i)
    print(list.length())
    for i in range(799, 300, -1):
        list.remove_at_index(i)
    print(list.length())
