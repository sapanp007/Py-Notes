class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("list is empty")
        else:
            ll_data = ""
            itr = self.head
            while itr:
                ll_data += str(itr.data) + "-->"
                itr = itr.next
            print(ll_data)

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, values):
        if self.head is None:
            for value in values:
                self.insert_at_the_end(value)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            for value in values:
                node = Node(value, None)
                itr.next = node
                itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_count():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, value):
        if index not in range(self.get_count()):
            raise Exception("invalid index")
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    node = Node(value, itr.next)
                    itr.next = node
                    break
                count += 1
                itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("No data to search")
        else:
            itr = self.head
            while itr:
                if itr.data == data_after:
                    node = Node(data_to_insert, itr.next)
                    itr.next = node
                    return
                itr = itr.next
            raise Exception("didn't find any match for data given")

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("empty linklist")
        else:
            itr = self.head
            while itr.next:
                if itr.next.data == data:
                    if itr.next.next is not None:
                        itr.next = itr.next.next
                        return
                    else:
                        itr.next = None
                        return
                itr = itr.next
            raise Exception("didn't find any match for data given")

    def get_mid_value(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_the_begining(4)
    ll.insert_at_the_begining(2)
    ll.print()
    ll.insert_at_the_end(5)
    ll.print()
    print(ll.get_count())
    ll.remove_at(1)
    ll.print()
    ll.insert_values([1, 2, 3])
    ll.print()
    ll.insert_at(4, 98)
    ll.print()
    ll.insert_after_value(98, 99)
    ll.print()
    ll.remove_by_value(98)
    # ll.remove_by_value(3)
    ll.print()
    print(ll.get_mid_value())
