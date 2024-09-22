class Tree:
    data: int
    height:int 
    left: object | None
    rigth: object | None

    def __init__(self) -> None:
        self.height = 0
        self.data = 0
        self.left = None
        self.rigth = None

    def append(self, d:int) -> object:
        if self.getData() == 0:
            self.data = d
            self.left = Tree()
            self.rigth = Tree()
            return self
            
        if d < self.getData() :
           self.left = self.left.append(d)
        elif d > self.getData():
            self.rigth = self.rigth.append(d)
        
        self.height = 1 + self.max(self.left.getHeight(),self.rigth.getHeight())
        fe = self.bf()

        if fe > 1:
            if d < self.left.getData():
                return self.rightRotation()
            
            elif d > self.left.getData():
                self.left = self.left.leftRotation()
                return self.rightRotation()
        
        if fe < -1:
            if d > self.rigth.getData():
                return self.leftRotation()
            elif d < self.rigth.getData():
                self.rigth = self.rigth.rightRotation()
                return self.leftRotation()
        
        return self
       

    def getData(self) -> int:
        return self.data
    
    def getHeight(self) -> int:
        return self.height


    def remove(self, node:object, d:int) -> None:
        if node == None:
            return None

        if node.data == d:
            node.data = 0
            return None

        node.remove(node.left,d)
        node.remove(node.rigth,d)


    def printTree(self, space = 0) -> None:
        if self.data == 0 :
            return 
        
        self.left.printTree(space + 1)
        for i in range(space):
            print(" ", end="")

        print(self.getData())
        self.rigth.printTree(space + 1)


    def bf(self) -> int: 
        return self.left.getHeight() - self.rigth.getHeight()
    
    def max(self, x, y) -> int:
        if x > y : return x
        return y
    

    def rightRotation(self) -> object:
        head = self.left
        t = head.rigth
        head.right = self 
        self.left = t
        self.height = self.max(self.left.getHeight(), self.rigth.getHeight()) + 1
        head.height = head.max(head.left.getHeight(), head.right.getHeight()) + 1
        return head
    
    def leftRotation(self) -> object:
        head = self.rigth
        t = head.left 
        head.left = self
        self.rigth = t
        self.height = self.max(self.left.getHeight(), self.rigth.getHeight()) + 1
        head.height = head.max(head.left.getHeight(), head.right.getHeight()) + 1
        return head