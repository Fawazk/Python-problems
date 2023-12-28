class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "----->", end=" ")
                n = n.ref
            print("\n")

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("linkedlist is empty!!")
            return
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in linkedlist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("linkedlist is empty!!")
            return
        if self.head.data == x:
            self.add_begin(data)
            return
        n = self.head
        while n.ref is not None:
            if n.ref == x:
                break
            n = n.ref
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("linkedlist is empty!!")
            return
        self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("linkedlist is empty!!")
            return
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, data):
        if self.head is None:
            print("linkedlist is empty!!")
            return
        elif self.head.data == data:
            self.delete_begin()
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == data:
                    n.ref = n.ref.ref
                    break
                n = n.ref
            if n.ref is None:
                print("node is not pressent!")


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(20)
LL1.add_end(30)
LL1.print_LL()
LL1.delete_by_value(100)
LL1.print_LL()
