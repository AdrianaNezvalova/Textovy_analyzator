"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Adriána Nezvalová
email: adriana.nezvalova@gmail.com
"""

# source texts for the project
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

''' SECONDARY VARIABLES '''
dashes = " ----------------------------------------"

''' USER LOGIN '''
# user input
print("\n")
user = input(" username: ")
password = input(" password: ")

# registered users
registered_users = {"bob": "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

# if registered user - welcome the user
if user in registered_users and password == registered_users[user]:
    print(dashes)
    print(f" Welcome to the app, {user.capitalize()}!\n We have 3 texts to be analyzed.")
    print(dashes)

# if unregistered user - terminate the program
else:
    print(f" unregistered user, terminating the program..")
    exit()

''' CHOOSING TEXT '''
# let the user choose the text to analyse
choice = input(" Enter a number btw. 1 and 3 to select: ")
print(dashes)

# if user chooses anything else than 1-3 - warning, terminate the program
if not choice.isdigit() or int(choice) not in range(1, 4):
    print(f" Invalid choice, terminating the program..")
    exit()

# if user chooses 1, 2 or 3 - assign the text to be analysed
else:
    analysed_text = TEXTS[int(choice) - 1]

'''TEXT ANALYSIS'''
# word and number count
text_list = analysed_text.split()
word_count = len(text_list)
titlecase_count = sum(1 for word in text_list if word.istitle())
uppercase_count = sum(1 for word in text_list if word.isupper())
lowercase_count = sum(1 for word in text_list if word.islower())
numbers_count = sum(1 for word in text_list if word.isdigit())
numbers_sum = sum(int(word) for word in text_list if word.isdigit())

# word lenghts count
word_length_count = {}
for word in text_list:
    if len(word) not in word_length_count:
        word_length_count[len(word)] = 1
    else:
        word_length_count[len(word)] += 1

''''PRINT RESULTS'''
print(f" There are {word_count} words in the selected text.")
print(f" There are {titlecase_count} titlecase words.")
print(f" There are {uppercase_count} uppercase words.")
print(f" There are {lowercase_count} lowercase words.")
print(f" There are {numbers_count} numeric strings.")
print(f" The sum of all the numbers is {numbers_sum}.")
print(dashes)
print(f" LEN|  OCCURENCES  |NR.")
print(dashes)
for key, value in sorted(word_length_count.items()):
    print(f"{key:>3}|{'*' * value:<15}|{value}")
print("\n")
    