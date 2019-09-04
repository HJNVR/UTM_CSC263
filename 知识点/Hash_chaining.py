# this it the version with chaining
SIZE = 10
#table = [L_NONE]*SIZE
class LinkedList:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
L_NONE = LinkedList()
table = [L_NONE]*SIZE
def has_function(x):
    """
    this function returns the index where the key is storted
    this is = search funciton
    """
    return x%10 # since the size of the table is right now 10

def insert(table, key, value):
    # instead of using = value, we make value into linked list
    L = LinkedList(value)
    L.next = table[has_function(key)]
    table[has_function(key)] = L
    #table[has_function(key)] = value
insert(table,41,'apple') # 41%10 = 1 => at index 1 position, table[1] = 'apple'
insert(table,93,'banana') # 93%10 = 3 => at index 3 position, table[3] = 'banana'
insert(table,41, 'orange')
print(table[1].value)
print(table[1].next.value)
# then we have a question here
# if at index 1,we now have more than one values
# we need chaining here to fix collision
# look in insert function

def delete(table, key, value):
    if table[has_function(key)] is None:
        return
    current = table[has_function(key)]
    temp = None
    while current:
        if (current.value == value):
            if temp is None:
                temp = current.next
                break
            else:
                temp.next = current.next
        if temp is None:
            temp = LinkedList(current.value)
        else:
            temp.next = LinkedList(current.value)
        current = current.next
    table[has_function(key)] = temp

delete(table,41,'apple')

#print(table)
print(table[1].value)
print(table[1].next.value)


