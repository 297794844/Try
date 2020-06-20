class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.__id = 430
class link():
    def __init__(self):
        self.lhead = None
    def travel(self):
        tra = self.lhead
        while tra is not None:
            print(tra.val)
            tra = tra.next
    def headinsert(self, newdata):
        node = Node(newdata)
        node.next = self.lhead
        self.lhead = node
    def tailinsert(self, newdata):
        node = Node(newdata)
        if self.lhead == None:
            self.lhead = node
            return
        tra = self.lhead
        while (tra.next):
            tra = tra.next
        tra.next = node
    def middleinsert(self, existdata, newdata):
        node = Node(newdata)
        tra = self.lhead
        if tra.val == existdata:
            node.next = tra.next
            self.lhead.next = node
            return
        while tra.val != existdata:
            tra = tra.next
        if tra.val == existdata:
            node.next = tra.next
            tra.next = node
    def delete(self, existdata):
        tra = self.lhead
        if tra.val == existdata:
            self.lhead = self.lhead.next
            return
        while tra.val != existdata:
            pre = tra
            tra = tra.next
        if tra.val == existdata:
            pre.next = tra.next
            return
    def caculatelength(self):
        length = self.lhead
        i = 0
        while length is not None:
            length = length.next
            i += 1
        return i

A = link()
B = Node(2)
C = Node(3)
A.lhead = Node(1)
#A.lhead.next = B
#A.lhead.next.next = C
#A.middleinsert(2, 100)
#A.delete(1)
#A.travel()
#print(A.caculatelength())

