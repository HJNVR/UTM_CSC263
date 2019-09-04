class Queue:
    # 后入前出
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        item = self.items[0]
        self.item.remove(item)
        return item

    def size(self):
        return len(self.items)
    
