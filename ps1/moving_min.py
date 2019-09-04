'''
CSC263 Winter 2019
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def solve_moving_min(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of get_min results
  '''
  index_get_min_calls = 0
  List = []
  result = []
  for command in commands:
      if command[0:6] == "insert":
          if command[7] != '-':
              insert(List, int(command[7:]))
          else:
              insert(List, -int(command[8:]))
      elif command == "get_min":
          result.append(get_min(sort_list(List)[index_get_min_calls:]))
          index_get_min_calls += 1
  return result

def sort_list(L):
    L.sort()
    L_copy = L
    return L_copy

def get_min(arr):
    if len(arr) == 0:
        return
    min_value = arr[0]
    start, end = 0, (len(arr) - 1)
    while start <= end:
        mid = (start + end) // 2
        if min_value == arr[mid]:
            return min_value
        if min_value < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

def insert(arr, element):
    if(len(arr)>1):
        max_index = len(arr) - 1
        start, end = 0, (len(arr) - 1)
        while start <= end:
            mid = (start + end) // 2
            if max_index == mid:
                arr += [element]
            if max_index < mid:
                end = mid - 1
            else:
                start = mid + 1
    else:
        arr += [element]
if __name__ == '__main__':

    # some small test cases
    # Case 1
  assert [10, 5, 10] == solve_moving_min(
    ['insert 10',
     'get_min',
     'insert 5',
     'insert 2',
     'insert 50',
     'get_min',
     'get_min',
     'insert -5'
    ])

    # Case 2
  assert [10,5,10,10] == solve_moving_min(
    ['insert 10',
     'get_min',
     'insert 5',
     'insert 2',
     'insert 50',
     'get_min',
     'get_min',
     'insert -5',
     'get_min'
    ])

