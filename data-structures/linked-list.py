class Node:
    def __init__(self, data):
        self.data = data   # Assign data
        self.next = None   # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
    
    def printList(self):
        currNode = self.head
        while(currNode):
            print(currNode.data) 
            currNode = currNode.next

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.insertAtBeginning(15)
    llist.printList()