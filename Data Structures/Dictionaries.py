# WRITE A FUNCTION THAT TAKES NAME AND AGE FROM USER AND UPDATES AN EXISTING DICTIONARY

new_dict={'name': 'xyz','age': 0}
def update_new_dict():
    print('Before Update: ', new_dict)
    name=input('Please enter your name: ')
    age=int(input('Please enter your age: '))
    new_dict['name']=name
    new_dict['age']=age
    print('After Update: ',new_dict)
update_new_dict()

# CREATE A FUNCTION THAT FINDS A PERSON'S PHONE NUMBER FROM A PHONE BOOK.

people_dict={'zain':123,'zain1':123,'zain2':123,'zain3':123,'zain4':123}
def find_person():
    person=input('\nWho are you looking for? ')
    if person in people_dict:
        print(f'The phone number of {person} is {people_dict[person]}')
    else:
        print("The user doesn't exist")
find_person()

