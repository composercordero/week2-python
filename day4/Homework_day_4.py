#Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book
# Steps

#     Create a function that will ask user for name and addresses and stores them in a dictionary
#     Define an empty dictionary with which to work (global or local variable?)
#     Begin a loop that will continue to ask a user for information until the user "quits"
#     If the user does not quit, ask for a name and address and store the values into variables
#     Add information to the dictionary with name as the key and address as the value
#     If the user does quit, end the loop
#     Print out the information from the dictionary in a formatted way
#     Execute/Call the function


address_book = {"Carlos": {"addres": 444, "phone": 555}}

def add_user():
    while True:
        
        # Questions
        name = input('Input name: ').title().strip()
        address = input(f"Input {name}'s address: ").title().strip()
        phone = input(f"Input {name}'s phone: ").strip(' -')
        
        # Append answers to the dict
        address_book[name] = {"address":address, "phone": phone}
        
        # Continue
        add_more = input("Add another one? y/n: ")
        
        # Break the loop
        if add_more == 'n':
            break
     
    # Print number of users
    if len(address_book) == 1:
        print(f'\nYou have successfully added 1 person to the address book:\n')
    else:   
        print(f'\nYou have successfully added {len(address_book)} people to the address book:\n')

    # Formatted list of users added
    print_address_book()
    
    # Options to edit users
    edit_user()

    #Do I need a return here?
        
def edit_user():
    what_else = input("\nadd, delete, quit: ").lower().strip()
    
    if what_else == 'add':
        add_user()
    elif what_else == 'delete':
        del_user()
        edit_user()
    elif what_else == 'quit':
        print("/nThank you for updating your address book!")
        return print_address_book()
    #Why is quit not working well?
    else:
        print("select a valid option!\n")
        edit_user()

def del_user():
    delete_user = input("what user would you like to delete? ").title().strip()
    if delete_user in address_book:
        del address_book[delete_user]
        print(f'\nYou have successfully deleted {delete_user} from the address book.\n')
        print(f'This is your address_book: \n')
        print_address_book()
        edit_user()
    else:
        print("User not in the address book.")
        del_user()
        
def print_address_book():
    for key,value in address_book.items():
        print(f"{key}: Address - {value['address']} / Phone - {value['phone']}")
        
print(add_user())


# Best Time to Meet

# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a list of times they are available ('HH:MM' 24-hour). Create a function that will take in an original list plus any number of lists of teammate's available times (remember *args) and return a list/set/dict/tuple of times where everyone can meet.

person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# person5 = ['12:00'] # to test with more arguments
# Available Times: '12:00' and '14:30'

def meeting(*args):
    set1 = set(args[0])
    for i in range(len(args)):
        set1 = set1.intersection(set(args[i]))
    return (set1)


print(meeting(person1, person2, person3, person4))

# set(person1).intersection(set(person2)).intersection(set(person3).intersection(set(person4)))
# Probably convert to set and check intersection