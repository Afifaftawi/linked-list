class LinkedList:
    class Node:
        def __init__(self, item):
            self.item = item  
            self.next = None  
    
    def __init__(self):
        self.head = None  
    
    def append(self, item):
        new_node = self.Node(item)
        if not self.head:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  
    
    def delete(self, index):
        if not self.head:
            print("List kosong")
            return
        if index == 0:
            self.head = self.head.next  
        else:
            current = self.head
            for _ in range(index - 1):
                if not current.next:
                    print("Index di luar jangkauan")
                    return
                current = current.next
            if current.next:
                current.next = current.next.next  
    
    def get(self, index):
        current = self.head
        for _ in range(index):
            if not current:
                print("Index di luar jangkauan")
                return None
            current = current.next
        return current.item if current else None


linked_list = LinkedList()


linked_list.append(10)
linked_list.append(20)
linked_list.append(30)


print(linked_list.get(0))  
print(linked_list.get(1)) 


linked_list.delete(1) 


print(linked_list.get(1)) 
