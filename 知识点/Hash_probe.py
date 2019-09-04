SIZE = 10
table = [None]*SIZE

def hash_function(k):
    return k % SIZE


def insert(table, key, value):
    # linear probe
    if table[hash_function(key)] is None:
        table[hash_function(key)] = value
        return
    insert(table, key+1,value)

insert(table,41,'apple')
insert(table,41,'orange')
insert(table,41,'pear')
print(table)
