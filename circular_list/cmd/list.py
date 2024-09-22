from abc import ABC, abstractmethod


class ListInt(ABC):

    @abstractmethod
    def isEmpty(self) -> bool:
        pass

    @abstractmethod
    def append(self, data:int) -> None:
        pass

    @abstractmethod
    def delete(self, data:int) -> None:
        pass

    @abstractmethod
    def delete(self, data:int) -> None:
        pass
    
    @abstractmethod
    def len(self) -> int:
        pass

    @abstractmethod
    def print(self) -> None:
        pass



class Node:
    data:int 
    next:object

    def __init__(self, data:int, next:object) -> None:
        self.data = data 
        self.next = next
    
    


class List(Node, ListInt):
    __head:object
    __tail:object
    __size:int

    def __init__(self) -> None:
        self.__head = Node(0,Node(0,None))
        self.__tail = Node(0,Node(0,None))
        self.__size = 0

    def isEmpty(self) -> bool:
        return self.__size == 0
    
    def append(self, data:int) -> None:
        node = Node(data,None)
        if self.isEmpty():
            self.__head = node
            node.next = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
            self.__tail.next = self.__head
        
        self.__size += 1
    
    def delete(self, data:int) -> None:
        if self.isEmpty():
            return
        if self.__head.data == data:
            self.__head = self.__head.next
            self.__tail = self.__head
        
        elif self.__tail.data == data:
            new__tail = self.__head
            while new__tail != self.__tail:
                new__tail = new__tail.next
            new__tail.next = self.__head
            self.__tail = new__tail
        
        else:
            current = self.__head 
            print(current)
            while current.data != data:
                current = current.data
            current.data = current.next.data 
            current.next = current.next.next
        
        self.__size -= 1
    
    def len(self) -> int:
        return self.__size
    
    
    def print(self) -> None:
        if self.isEmpty():
            return
        
        current = self.__head 
        for i in range(self.__size):
            print("{}".format(current.data))
            current = current.next



def NewCircularList() -> ListInt:
    l = List()
    return l