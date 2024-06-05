# Accept user input to create a list of integers
user_input = input("Enter a list of integers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

# Compute the sum of all integers in the list
total_sum = sum(numbers)
print("Sum of integers:", total_sum)


# Create a tuple containing the names of five favorite books
favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")

# Print each book name on a separate line using a for loop
print("Favorite Books:")
for book in favorite_books:
    print(book)


# Create an empty dictionary to store person information
person_info = {}

# Ask the user for input and store the information in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = int(input("Enter your age: "))
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("Person Information:")
print(person_info)


# Accept user input to create two sets of integers
set1 = set(input("Enter elements for set 1 separated by spaces: ").split())
set2 = set(input("Enter elements for set 2 separated by spaces: ").split())

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)


# Store a list of words
word_list = ["apple", "banana", "orange", "kiwi", "grape"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
