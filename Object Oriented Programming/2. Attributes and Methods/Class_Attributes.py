class Orange:
    count = 0
    total_weight = 0

    def __init__(self, weight):
        self.weight = weight
        Orange.count += 1
        Orange.total_weight += self.weight


first = Orange(180)
second = Orange(200)
third = Orange(220)

x = 0
for i in [first, second, third]:
    lst = ['first','second','third']
    print(f'The weight of the {lst[x]} orange is {i.weight} grams.')
    x+=1
print('Total Count:', Orange.count)


def add_weight(a, b, c):
    return a + b + c

print('Total weight from an outside function:',add_weight(first.weight, second.weight, third.weight),'grams')
print('Total weight from class variable:', Orange.total_weight,'grams')
