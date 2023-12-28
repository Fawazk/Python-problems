class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def forward_traversel(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "----->", end=" ")
                n = n.nref

    def backward_traversel(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "----->", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty!!")

    def add_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after_value(self, data, x):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given value is not in doubly linkedlist")
            else:
                new_node.pref = n
                new_node.nref = n.nref
                n.nref = new_node

    def add_before_value(self, data, x):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given value is not in doubly linkedlist")
            else:
                new_node.pref = n.pref
                n.pref = new_node
                new_node.nref = n
                if self.head == n:
                    # print('***',new_node.data,'****')
                    self.head = new_node
                else:
                    new_node.pref.nref = new_node

    def delete_begin(self):
        if self.head is None:
            print("linkedlist is empty!,can't delete")
            return
        else:
            if self.head.nref is None:
                self.head = None
                print("DLL is empty after deleting available node")
            else:
                self.head = self.head.nref
                self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("linkedlist is empty!,can't delete")
            return
        else:
            if self.head.nref is None:
                self.head = None
                print("DLL is empty after deleting available node")
            else:
                n = self.head
                while n is not None:
                    if n.nref is None:
                        break
                    n = n.nref
                n.pref.nref = None

    def delete_value(self, data):
        if self.head is None:
            print("linkedlist is empty!,can't delete")
            return
        else:
            if self.head.data == data:
                if self.head.nref is not None:
                    self.head.nref.pref = None
                    self.head = self.head.nref
                else:
                    self.head = None
                if self.head is None:
                    print("DLL is empty after deleting available node")
            else:
                n = self.head
                while n is not None:
                    if n.data == data:
                        break
                    n = n.nref
                if n is not None:
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref
                else:
                    print("Given value is not in DL")


DL1 = DoublyLinkedList()
DL1.add_at_begin(20)
DL1.add_at_begin(10)
DL1.add_at_end(100)
DL1.add_after_value(200, 100)
DL1.add_before_value(201, 200)
DL1.forward_traversel()
print("\n")
DL1.delete_value(190)
DL1.forward_traversel()
print("\n")
DL1.backward_traversel()
