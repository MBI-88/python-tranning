from cmd.list import NewCircularList



if __name__ == "__main__":
    l = NewCircularList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print()
    print("Len: ",l.len())

    print()
    l.append(4)
    l.append(5)
    print("Len: ",l.len())

    l.delete(1)
    l.print()
    print("Len: ",l.len())