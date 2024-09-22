
from tree import Tree



if __name__ == "__main__":
    t = Tree()
    t = t.append(8)
    t = t.append(6)
    t = t.append(1)
    t = t.append(2)
    t = t.append(10)
    t = t.append(20)
    t = t.append(15)
    t.remove(t, 6)
    t.printTree()
    