# PRINT THE COMMON ELEMENTS IN TWO SETS.
# PRINT THE NUMBER OF UNIQUE ELEMENTS IN TWO SETS.
# PRINT ELEMENTS IN SET 2 THAT ARE NOT IN SET 1.

set_1={'A','B','E','J','L','O','K','Y','N'}
set_2={'C','B','D','N','P','Y','A','J','M'}
print(f'The common elements in both sets are {set_1&set_2}')
print(f'The total number of unique elements in both sets is "{len(set_1|set_2)}"')
print(f'The alphabets that are in set_2 but not in set_1 are {set_2-set_1}')

# ELEMENT WISE SUM OF GIVEN TUPLE

x = (2,5,7)
y = (3,8,4)
z = (5,7,12)
result = tuple(map(sum,zip(x,y,z)))
print(result)
