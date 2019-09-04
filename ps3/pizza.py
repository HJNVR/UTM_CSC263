'''
CSC263 Winter 2019
Problem Set 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries

def num_pizza_kinds(pizzas):
    '''
    Pre: pizzas is a list of pizza 5-tuples
      Post: return number of kinds of pizzas
    '''
    count = 0
    temp_pizzas = []
    for pizza in pizzas:
        if not is_pizza_in(pizza, temp_pizzas):
            temp_pizzas += [pizza]
            count += 1
        
    return count
    

def is_pizza_in(tup, pizzas):
    '''
    determine whether a tuple is in the given list of tuples
    Post:return true if tuple is in pizzas
    '''
    if len(pizzas) == 0:
        return False
    for pizza in pizzas:
        if compare_two_pizza(pizza, tup):
            return True
    return False
def compare_two_pizza(tup1, tup2):
    '''
    Pre: tup1 and tup2 are two tuples in pizzas
    Post: return true if tup2 is the right rotation of tup1
    '''
    first_tup2 = tup2[0]
    if(first_tup2 not in tup1):
        return False
    num_right_rotation = tup1.index(first_tup2)
    temp_tuple = ()

    for i in range(num_right_rotation, len(tup1)):
        temp_tuple += (tup1[i],)

    for j in range(0,num_right_rotation):
        temp_tuple += (tup1[j],)

    return temp_tuple == tup2

if __name__ == '__main__':

  # some small test cases
  # Case 1
  pizzas = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 1), (5, 4, 3, 2, 1), (4, 3, 2, 1, 5), (20, 10, 2, 9, 1)]
  assert 3 == num_pizza_kinds(pizzas)

  # Case 2
  pizzas = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 1), (4, 5, 1, 2, 3), (20, 10, 2, 9, 1)]
  assert 2 == num_pizza_kinds(pizzas)

  # Case 3
  pizzas = []
  assert 0 == num_pizza_kinds(pizzas)

  # Case 2
  pizzas = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 1), (4, 5, 1, 2, 3)]
  assert 1 == num_pizza_kinds(pizzas)
