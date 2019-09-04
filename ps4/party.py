'''
CSC263 Winter 2019
Problem Set 4 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def find_student(student,settle_info):
    '''
    Pre: an int that represents the specific student and a dictionary   
    Post: return -100 if we can not find the student in the dictionary
    return the specific key if we can find the student in the dictionary
    '''
    represent =  -100
    if len(settle_info) == 0:
        return represent
    for key, value in settle_info.items():
        if student in value:
            return int(key)
    return represent

def get_first_element(s):
    '''
    Prep: a set
    Post: return the first element in the given set
    '''
    l = []
    for i in s:
        l.append(i)
    return l[0]

def get_second_element(s):
    '''
    Pre: a set
    Post: return the second element in the given set
    '''
    l = []
    for i in s:
        l.append(i)
    return l[1]

def union_info(all_info, settle_info):
    '''
    Pre: a list of all 'add' information and a dctionary of different sets
    Post: update the settle_info: put all students who belong to same party into
    one set
    '''
    for i in range(len(all_info)-1):
        for j in range(i+1, len(all_info)):
            if not all_info[i].isdisjoint(all_info[j]):
                #every time we have two 'add' info, if they share one student
                #we union them together
                intersection = all_info[i].intersection(all_info[j])
                union_set = all_info[i].union(all_info[j])
                union_set.remove(get_first_element(intersection))
                element = get_first_element(union_set)

                #determine which element should be the representative of set
                if len(settle_info) == 0:
                    settle_info[element] = union_set
                else:
                    key = find_student(element, settle_info)
                    if key > 0:
                        settle_info[str(key)] = settle_info[str(key)].union(union_set)

                    else:
                        element2 = get_second_element(union_set)
                        key2 = find_student(element2, settle_info)
                        if key2 > 0:
                            settle_info[str(key2)] = settle_info[str(key2)].union(union_set)
                        else:
                            settle_info[element] = union_set
                        
def solve_party(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of 'tell' results
  '''
  result = []
  all_info = [] # record all 'add' info
  settle_info = {} #record all students who attend same party refer to current all_info
  for command in commands:
      info = command.split()
      
      if info[0] == 'add':
          if find_student(info[1],settle_info) < 0 or find_student(info[2],settle_info) < 0:
              all_info.append({info[1],info[2]}) # record all 'add' info
              if len(all_info) >= 2:
                  union_info(all_info,settle_info)
      elif info[0] == 'tell':
          # if we can find two both students' inof in settle_
          represent1 = find_student(info[1],settle_info)
          represent2 = find_student(info[2], settle_info)
          if (represent1 > 0 and represent2 > 0):
              if represent1 == represent2:
                  result.append('same')
              else:
                  result.append('different')
          else:
              if {info[1], info[2]} in all_info:
                  result.append('different')
              else:
                  result.append('unknown')
  return result 

if __name__ == '__main__':

  # some small test cases
  # Case 1
  assert ['unknown', 'different', 'same'] == solve_party(
    ['tell 1 3',
     'add 1 3',
     'tell 1 3',
     'add 3 4',
     'tell 1 4'
    ])
  
