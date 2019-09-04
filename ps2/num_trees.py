'''
CSC263 Winter 2019
Problem Set 2, Question 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def num_trees(nodes, leaves):
    result = 1
    if leaves % 2 == 0:
        return 0
    else:
        while(leaves != 2):
            leaves = leaves //2 +1
            result = result*leaves
    return result

if __name__ == '__main__':

  # some small test cases
  # Case 1
  assert 2 == num_trees(5, 3)
