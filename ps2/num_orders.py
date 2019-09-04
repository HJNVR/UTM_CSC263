'''
CSC263 Winter 2019
Problem Set 2, Question 2  Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
def find_probability(n,r):
    above = 1
    bottom = 1
    for i in range(r):
        above = above * n
        n = n - 1
        bottom = bottom * r
        r = r- 1
    return above//bottom

def num_orders(lst):
    if(len(lst)<=1):
        return 1
    else:
        left_lst = []
        right_lst = []
        for i in range(1,len(lst)):
            if(lst[i]<lst[0]):
                left_lst+=[lst[i]]
            else:
                right_lst+=[lst[i]]
    return num_orders(left_lst) * num_orders(right_lst) * find_probability(len(lst)-1,len(left_lst))

if __name__ == '__main__':

  # some small test cases
  # Case 1
  assert 2 == num_orders([2, 1, 3])
  # Case 2
  assert 8 == num_orders([4, 2, 1, 5, 3])
