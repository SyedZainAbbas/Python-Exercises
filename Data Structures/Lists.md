**Lists** can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed! Lists are
ordered sequence meaning they can be called with the indexes. Lists are used when order of a sequence is important, for instance you want to keep track of a queue so that
everyone gets served in an orderly manner.

### Assign a list to an variable named my_list
my_list = [1,2,3]

### Lists can contain different types of data
my_list = ['A string',23,100.232,'o']

### Indexing and Slicing
Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:

my_list = ['one','two','three',4,5]

#### Grab element at index 0
my_list[0]

#### Grab index 1 and everything past it
my_list[1:]

#### Grab everything UP TO index 3
my_list[:3]

#### Concatenation
We can also use + to concatenate lists, just like we did for strings.

my_list + ['new item']

Note: This doesn't actually change the original list!
You would have to reassign the list to make the change permanent.

#### Reassign
my_list = my_list + ['add new item permanently']

We can also use the * for a duplication method similar to strings:

#### Make the list double
my_list * 2
