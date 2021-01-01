'''
Singly linked list and node classes by Saadkhalid913
'''

class node():
    '''
    node class for implementation purposes 
    '''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 
    def __repr__(self):
        return str(self.data)
    def __str__(self):
        return str(self.data)




class LinkedList(object):
    '''
    Singly linked list class with 
    '''

    def __init__(self):
        self.first_node = None
        self.last_node = None 
    
    def __repr__(self):
        return str(self.ToArray())
    
    def __getitem__(self, index: int):
        '''
        indexing method runs in O(i) time complexity and O(1) space complexity
        returns data of node object
        '''
        i = index
        Node = self.first_node
        while i > 0:
            Node = Node.next
            if Node == None:
                raise IndexError
            i -=1
        return Node.data

    def __iter__(self):
        return iter(self.ToArray())

    def __len__(self):
        i = 0
        node = self.first_node
        while node != None:
            i +=1 
            node = node.next 
        return i 
    
    def isempty(self):
        return self.first_node == None

    def add(self, data):
        newnode = node(data)
        if self.first_node == None:
            self.first_node = newnode
            self.last_node = newnode 
        else:
            self.last_node.next = newnode 
            self.last_node = newnode 
        
    def remove(self, index):
        '''
        Removes a node at a given index
        '''
        # edge cases 
        if self.isempty():
            return
        if index == 0:
            self.first_node = None
            self.last_node = None
            return
        
        # main loop
        node = self.first_node
        prevnode = None 

        for i in range(index):
            prevnode = node
            node = node.next
            if node == None:
                raise IndexError
            i +=1 
        
        # case when len == 2 
        if prevnode == None:
            self.first_node = node.next
            del node 
        # else case 
        else:
            prevnode.next = node.next
            del node 

    def add_first(self, data):
        '''
        Adds a Node to index 0 of linked list, all other items are shifted to the right
        '''
        newnode = node(data, self.first_node)
        if self.first_node == None:
            self.first_node = newnode
            self.last_node = newnode 
        else:
            self.first_node = newnode
    
    def ToArray(self):
        '''
        Returns a new array of varying datatypes
        Does not modify the existing instance of class 
        '''

        arr = []
        node = self.first_node

        while node != None:
            arr.append(node)
            node = node.next
        return list(map(lambda node: node.data, arr))
    
    def reverse(self):
        prevnode = self.first_node
        node = prevnode.next
        while node != None:
            nex = node.next
            node.next = prevnode
            prevnode = node
            node = nex
        self.first_node, self.last_node = self.last_node, self.first_node 
        self.last_node.next = None

L = LinkedList()

for i in range(1,6):
    L.add(10*i)

L.reverse()

pass