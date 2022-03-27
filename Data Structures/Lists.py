"""
Question No. 1: WRITE A FUNCTION THAT RETURNS TRUE IF A LIST IS SORTED

THIS FUNCTION TAKES A LIST AS AN ARGUMENT AND TELLS YOU
IF IT IS SORTED OR NOT
"""
print('QUESTION NO.1\n')
def is_sorted(L):
    print(L)
    for i in range(len(L)-1):
        if L[i].lower()>L[i+1].lower():
            return False
    return True
f=['apple','banana','cherry','lemon']

# VARIANTS
def variant(num):
    l1=f.copy()
    l1.insert(num,'peach')
    return l1

list_variant=[f,variant(1),variant(2),variant(3),variant(4)]
for i in list_variant:
    print(is_sorted(i))

''' Question No.2:  WRITE A FUNCTION THAT RETURNS
THE FIRST ELEMENT THAT IS NOT IN ASCENDING ORDER
'''
print('\nQUESTION NO.2\n')
def find_not_sorted(num):
    print(num)
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            return num[i]
    return 'The list is in ascending order'
numbers=[1,4,3,4,5]
print(find_not_sorted(numbers))

# SOLUTION TO QUESTION NO. 2 WITH A SLIGHT MODIFICATION
print('\nsolution to question number 2 with slight modification')
def find_not_sorted_mod(num):
    for val, index in enumerate(range(len(num)-1)):
        if num[val]>num[val+1]:
            return f'The value: {num[val]} at index: {index} is problematic'
    return 'The list is in ascending order'
print(find_not_sorted_mod(numbers))

''' Question No.3:  WRITE A FUNCTION THAT REMOVES
ALL THE ELEMENTS THAT ARE NOT IN ASCENDING ORDER
'''
print('\nQUESTION NO.3\n')
def remove_not_sorted(num):
    sorted_list=[num[0]]
    for i in range(1,len(num)):
        if num[i]>=max(num[:i]):
            sorted_list.append(num[i])
    return f'Your list: {num}\nSorted list: {sorted_list}\n'
numbers=[1,2,4,3,5]
numbers1=[2,5,5,8,7,4,6,1,51,4,3]
print(remove_not_sorted(numbers))
print(remove_not_sorted(numbers1))

print('\nAlternative Solution QUESTION NO.3\n')
def remove_not_sorted_mod(lst):
    old_lst=lst[:]
    i=1
    while lst!=sorted(lst):
        if lst[i]<max(lst[:i]):
            del lst[i]
            i-=1
        else:
            i+=1
    return f'Your list: {old_lst}\nSorted list: {lst}\n'
numbers=[1,2,4,3,5]
numbers1=[2,5,5,8,7,4,6,1,51,4,3]
print(remove_not_sorted_mod(numbers))
print(remove_not_sorted_mod(numbers1))


''' Question No.4:  WRITE A FUNCTION THAT MOVES
THE OUT OF ORDER ELEMENTS TO ANOTHER LIST.
'''
print('\nQUESTION NO.4\n')
def move_not_sorted(num):
    sorted_list = [num[0]]
    unsorted_list = []
    for i in range(1,len(num)):
        if num[i] >= max(num[:i]):
            sorted_list.append(num[i])
        else:
            unsorted_list.append(num[i])
    return f'Your list: {num}\nSorted list: {sorted_list}\nUnsorted elements: {unsorted_list}\n'

numbers = [1, 2, 4, 3, 5]
numbers1 = [2, 5,5,8, 7, 4, 6, 1, 51, 4, 3]
cars= ['audi','chevrolet','bmw','ford','honda','gmc']
print(move_not_sorted(numbers))
print(move_not_sorted(numbers1))
print(move_not_sorted(cars))
