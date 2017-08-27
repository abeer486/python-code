''' movies  = ['batman','dark knight', 'inception']
movies[0].title
movies.insert(0,'inception')
movies[0].lower()

movie_0 = {'title' : 'Inception', 'director': 'Nolan', 'Year':2010}
print(movie_0['title'])
 '''


## Defining a basic function
def greet_user(username):
    ""'Display a sample greeting'""
    print("Hello, " + username.title())

# greet_user("Abeer")

## Designing a function with default parameters
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type +"'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='Harry', animal_type='hamster')

## Designing a function with a return value
def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name = first + ' ' + last
    return full_name.title()

musician = get_formatted_name('hans', 'zimmer')
print(musician)

## Designing a function passing in lists
def greet_users(names):
    """Print a sample greeting to each user in the list. """

    # note: names is a list
    for name in names:
        msg = "Hello, " + name.title() +"!"
        print(msg)

    last_person = names.pop()
    msg = "Last person is: " + last_person
    print(msg)
    print('Remaining number of items: ' + str(len(names)))

usernames = ['Nolan', 'Bale', 'Zimmer']
greet_users(usernames)


## Designing a function passing a COPY of the list
def greet_users_again(new_names):
    """Print a sample greeting to each user in the list, but don't modify the list"""

    names = new_names[:]

    # note: names is a list
    for name in names:
        msg = "Hello, " + name.title() +"!"
        print(msg)

    last_person = names.pop()
    msg = "Last person is: " + last_person
    print(msg)
    print('Remaining number of items: ' + str(len(new_names)))

usernames = ['Nolan', 'Bale', 'Zimmer']
greet_users_again(usernames)


## Designing a function to pass in an artibary number of arguments
## Also having a standard argument 
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print('\nMaking a pizza of size ' + str(size) + ' with the following toppings')
    print(toppings)

make_pizza(12, 'mushrooms', 'cheeze')
