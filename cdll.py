# Course: CS261 - Data Structures
# Student Name: Michael Uchmanowicz
# Assignment: A3 P3
# Description: Deque and Bag ADT interfaces with a circular doubly linked list data
# structure


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'Node [' + str(self.value) + ']'
        return out


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel)
        """
        next_node = self.sentinel.next
        new_node = DLNode(value)
        next_node.prev = new_node
        self.sentinel.next = new_node
        new_node.next = next_node
        new_node.prev = self.sentinel
        if next_node.prev == self.sentinel:
            self.sentinel.prev = new_node

        return

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (right before the back sentinel).
        """
        prev_node = self.sentinel.prev
        new_node = DLNode(value)
        self.sentinel.prev = new_node
        prev_node.next = self.sentinel.prev
        self.sentinel.prev.prev = prev_node
        new_node.next = self.sentinel
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, the method raises a custom “SLLException”
        """
        if index < 0:
            raise CDLLException
        else:
            cur = self.sentinel.next
            pre = None
            cur_index = 0
            while cur_index < index:
                pre = cur
                cur = cur.next
                cur_index += 1
                if pre == self.sentinel:
                    raise CDLLException
            else:
                w = cur.prev
                x = DLNode(value)
                y = cur

                x.next = y
                w.next = x
                x.prev = w
                y.prev = x
        return

    def remove_front(self) -> None:
        """
        Removes the first node from the list. If the list is empty, the method raises a
        custom “SLLException”
        """

        if self.sentinel.next == self.sentinel:
            raise CDLLException
        else:
            new_front = self.sentinel.next.next
            new_front.prev = self.sentinel
            self.sentinel.next = new_front

        return

    def remove_back(self) -> None:
        """
        Removes the last node from the list. If the list is empty, the method raises a
        custom “SLLException”
        """
        new_back = self.sentinel.prev.prev

        if self.sentinel.next == self.sentinel:
            raise CDLLException
        else:
            new_back.next = self.sentinel
            self.sentinel.prev = new_back

        return

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index. Index 0 refers to the beginning
        of the list.
        If the provided index is invalid, the method raises a custom “SLLException”
        """
        if self.sentinel.next == self.sentinel or index < 0:
            raise CDLLException
        else:
            cur = self.sentinel.next
            pre = None
            cur_index = 0

            while cur_index < index:
                pre = cur
                cur = cur.next
                cur_index += 1
                if pre == self.sentinel:
                    raise CDLLException
            else:
                if cur == self.sentinel:
                    raise CDLLException
                else:
                    w = cur.prev
                    y = cur.next

                    y.prev = w
                    w.next = y

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without removing it. If the list is
        empty, the method raises a custom “SLLException”
        """
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Returns value from the last node in the list without removing it. If the list is
        empty, the method raises a custom “SLLException”
        """
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end and removes the first node in
        the list that matches the provided “value” object. Method returns True if some node was
        actually removed from the list. Otherwise it returns False
        """
        if self.sentinel.next == self.sentinel:
            return False
        else:
            cur = self.sentinel.next
            cur_index = 0

            while cur.value != value:
                cur = cur.next
                cur_index += 1
                if cur == self.sentinel:
                    return False
            else:
                self.remove_at_index(cur_index)
                return True

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value”
        object
        """
        cur = self.sentinel.next
        value_count = 0

        while cur != self.sentinel:
            if cur.value == value:
                value_count += 1
            cur = cur.next
        else:
            return value_count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new CircularlyLinkedList object that contains the requested number of nodes
        from the original list starting with the node located at the requested start index. If the
        original list contains N nodes, valid start_index is in range [0, N - 1] inclusive.
        If the provided start index is invalid, or if there are not enough nodes between start index
        and end of the list to make the slice of requested size, this method raises a custom
        “CDLLException”
        """
        if start_index > self.length() - 1 or start_index + size - 1 > self.length() - 1:
            raise CDLLException
        else:
            new = CircularList()
            slice_end = start_index + size
            cur_index = start_index
            while cur_index < slice_end:
                new.add_back(self.get_at_index(cur_index))
                cur_index += 1
            else:
                return new

    def get_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index. Index 0 refers to the beginning
         of the list.
        If the provided index is invalid, the method raises a custom “SLLException”
        """
        if self.sentinel.next == self.sentinel or index < 0:
            raise CDLLException
        else:
            cur = self.sentinel.next
            pre = None
            cur_index = 0

            while cur_index < index:
                pre = cur
                cur = cur.next
                cur_index += 1
                if pre == self.sentinel:
                    raise CDLLException
            else:
                if cur == self.sentinel:
                    raise CDLLException
                else:
                    return cur.value

    def is_sorted(self) -> int:
        """
        Returns an integer that describes whether the linked list is sorted. Method
        should return 1 if the list is sorted in strictly ascending order. It should return 2 if the list is
        sorted in strictly descending order. Otherwise the method should return 0.
        Empty list and list consisting of a single node is considered sorted in strictly ascending
        order
        """
        if self.sentinel.next == self.sentinel or self.sentinel.next.next == self.sentinel:
            return 1
        else:
            cur = self.sentinel.next
            if cur.value > cur.next.value:
                sort = 2
                cur = cur.next
            elif cur.value < cur.next.value:
                sort = 1
                cur = cur.next
            while sort > 0:
                if sort == 2:
                    if cur.next == self.sentinel:
                        return sort
                    if cur.value < cur.next.value:
                        return 0
                    else:
                        cur = cur.next
                if sort == 1:
                    if cur.next == self.sentinel:
                        return sort
                    if cur.value > cur.next.value or cur.value == cur.next.value:
                        return 0
                    else:
                        cur = cur.next

            else:
                return 0

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps pairs of two nodes located at different indices
        """

        if index1 < 0 or index2 < 0:
            raise CDLLException
        elif index1 > self.length() - 1 or index2 > self.length() - 1:
            raise CDLLException
        elif index1 == index2:
            return
        else:

            # index 1 node
            prev_node = self.sentinel
            curr_node = self.sentinel.next

            one_index = 0
            while one_index != index1:
                prev_node = curr_node
                curr_node = curr_node.next
                one_index += 1

            # index 2 node
            prev_node2 = self.sentinel
            curr_node2 = self.sentinel.next

            two_index = 0
            while two_index != index2:
                prev_node2 = curr_node2
                curr_node2 = curr_node2.next
                two_index += 1

            w1 = prev_node
            x1 = curr_node
            y1 = curr_node.next

            w2 = prev_node2
            x2 = curr_node2
            y2 = curr_node2.next

            if index2 == index1 + 1:
                pass
                x2.prev = w1
                x1.next = y2
                x2.next = x1
                x1.prev = x2
                w1.next = x2
                y2.prev = x1

            else:

                x1.next = y2
                x2.next = y1
                w1.next = x2
                w2.next = x1

                x1.prev = w2
                x2.prev = w1
                y2.prev = x1
                y1.prev = x2

    def reverse(self) -> None:
        """
        Reverses the order of the nodes in the list.
        """
        length = self.length()
        if length % 2 == 0:
            mid = length / 2
        else:
            mid = (length - 1) / 2
        for i in range(0, int(mid)):
            pair1 = 0 + i
            pair2 = length - i - 1
            self.swap_pairs(pair1, pair2)

        return

    def sort(self) -> None:
        """
        Sorts the content of the list in non-descending order.
        """

        last_sort = None
        length = self.length()
        while last_sort != 0:
            if last_sort is not None:
                length = last_sort
            if length <= 1:
                return
            else:
                for i in range(length - 1):
                    if self.get_at_index(i) > self.get_at_index(i + 1) and i != length:
                        self.swap_pairs(i, i + 1)
                        last_sort = i + 1
                    else:
                        last_sort = i + 1

    def length(self) -> int:
        """
        Returns the number of nodes in the list
        """
        if self.sentinel.next == self.sentinel:
            return 0
        else:
            cur = self.sentinel.next
            cur_index = 0

            while cur.next != self.sentinel:
                cur = cur.next
                cur_index += 1
            else:
                cur_index += 1
                return cur_index

    def is_empty(self) -> bool:
        """
        Returns True if the list has no data nodes. Otherwise, it returns False. T
        """
        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False


if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = CircularList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    # print('\n# add_back example 1')
    # list = CircularList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)
    #
    #
    # print('\n# insert_at_index example 1')
    # list = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # #
    # #
    # print('\n# remove_front example 1')
    # list = CircularList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = CircularList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
    # #
    # #
    # print('\n# remove_at_index example 1')
    # list = CircularList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)
    # #
    # #
    # print('\n# get_front example 1')
    # list = CircularList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))
    # #
    # #
    # print('\n# get_front example 1')
    # list = CircularList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
    # #
    # #
    # print('\n# remove example 1')
    # list = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)
    # #
    # #
    # print('\n# count example 1')
    # list = CircularList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    # #
    # #
    # print('\n# slice example 1')
    # list = CircularList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    # #
    # #
    # print('\n# slice example 2')
    # list = CircularList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")
    # #
    # #
    # print('\n# is_sorted example 1')
    # test_cases = (
    #     [-100, -8, 0, 2, 3, 10, 20, 100],
    #     ['A', 'B', 'Z', 'a', 'z'],
    #     ['Z', 'T', 'K', 'A', '1'],
    #     [1, 3, -10, 20, -30, 0],
    #     [-10, 0, 0, 10, 20, 30],
    #     [100, 90, 0, -90, -200]
    # )
    # for case in test_cases:
    #     list = CircularList(case)
    #     print('Result:', list.is_sorted(), list)
    # #
    # #
    # print('\n# is_empty example 1')
    # list = CircularList()
    # print(list.is_empty(), list)
    # list.add_back(100)
    # print(list.is_empty(), list)
    # list.remove_at_index(0)
    # print(list.is_empty(), list)
    # #
    # #
    # print('\n# length example 1')
    # list = CircularList()
    # print(list.length())
    # for i in range(800):
    #     list.add_front(i)
    # print(list.length())
    # for i in range(799, 300, -1):
    #     list.remove_at_index(i)
    # print(list.length())
    #
    print('\n# swap pairs example 1')
    list = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5), (4, 2), (3, 3))
    for i, j in test_cases:
        print('\nSwap nodes ', i, j, ' ', end='')
        try:
            list.swap_pairs(i, j)
            print(list)
        except Exception as e:
            print(type(e))

    # print('\n# reverse example 1')
    # test_cases = (
    #     [1, 2, 3, 3, 4, 5],
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     list = CircularList(case)
    #     list.reverse()
    #     print(list)
    #
    # print('\n# reverse example 2')
    # list = CircularList()
    # print(list)
    # list.reverse()
    # print(list)
    # list.add_back(2)
    # list.add_back(3)
    # list.add_front(1)
    # list.reverse()
    # print(list)
    #
    # print('\n# Sort Example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     list = CircularList(case)
    #     print(list)
    #     list.sort()
    #     print(list)
