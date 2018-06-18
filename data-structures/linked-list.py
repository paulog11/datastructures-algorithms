import argparse
import sys

class Node:
    def __init__(self, data):
        self.data = data   # Assign data
        self.next = None   # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, newNode):
        newHead = newNode
        newHead.next = self.head
        self.head = newHead

    def insertAfter(self, prevNode, newNode):
        if prevNode is None:
            print("The given previous node must be in the Linked List")
            return
        newNode.next = prevNode.next
        prevNode.next = newNode

    def insertAtEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        travNode = self.head
        while(travNode.next):
            travNode = travNode.next
        travNode.next = newNode

    def deleteFirst(self, valueToDelete):
        if self.head is not None:
            if self.head.data == valueToDelete:
                self.head = self.head.next
                return
        prevNode = self.head
        travNode = self.head
        while(travNode.data != valueToDelete):
            prevNode = travNode
            if travNode.next:
                travNode = travNode.next
            else:
                print("Could not find node to delete!")
                return
        prevNode.next = travNode.next

    def deleteNode(self, targetNode):
        if self.head==targetNode:
            self.head = self.head.next
            return
        prevNode = self.head
        travNode = self.head
        while(travNode != targetNode):
            prevNode = travNode
            if travNode.next:
                travNode = travNode.next
            else:
                print("Could not find node to delete!")
                return
        prevNode.next = travNode.next
    
    def printList(self):
        currNode = self.head
        while(currNode):
            print(currNode.data, end=" ") 
            currNode = currNode.next
        print("")

if __name__=='__main__':
    # parser = argparse.ArgumentParser(description='Tests Linked List class implementations.')
    # parser.add_argument('insert', )
    # parser.add_argument('delete', )
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    print("First nodes of Linked List:")
    llist.printList()

    if len(sys.argv)==1:
        print("No args given, exiting...")
    elif sys.argv[1]=='insert':
        print("Testing insertions...")

        testNode1 = Node(15)
        print("Inserting Node = 15 at beginning")
        llist.insertAtBeginning(testNode1)
        llist.printList()

        testNode2 = Node(17)
        print("Inserting Node = 17 at end")
        llist.insertAtEnd(testNode2)
        llist.printList()

        testNode3 = llist.head
        testNode4 = Node(30)
        print("Inserting Node = 30 at second place from beginning")
        llist.insertAfter(testNode3, testNode4)
        llist.printList()
    elif sys.argv[1]=='delete':
        llist.insertAtBeginning(Node(40))
        llist.insertAtEnd(Node(41))
        llist.insertAtEnd(Node(42))
        llist.insertAtEnd(Node(43))
        testTargetNode = Node(44)
        llist.insertAtEnd(testTargetNode)
        print("Node list:")
        llist.printList()

        print("Deleting Node with data = 40")
        llist.deleteFirst(40)
        llist.printList()
        print("Deleting Node with data= 41")
        llist.deleteFirst(41)
        llist.printList()

        print("Deleting Target Node = 42")
        llist.deleteNode(testTargetNode)
        llist.printList()

        
