# daily-learning-log
coding 100 days of Python

{

Date - 4/16/2026
================

Pandas and NumPy for Data Analysis
TensorFlow and Scikit for ML and AI model

In Web Development - Django, FastAPI, and Flask (Python Framework for building scalable and secure back-end with minimal effort)

In Cybersecurity - to detect vulnerabilities like malware and other viruses and can build automated security scans and analyze threats

In DevOps (software development methodology) - for writing CI/CD scripts and managing infrastructure across development pipelines. It is also commonly used to build back-end services and internal APIs.

In Software Testing - Using pytest

For UI and manage Cloud Deployments for project - Selenium and BeautifulSoup libraries use


================================

1st - Variables and Data Types
------------------------------

eg 1 

- print('My favorite colors are', 'blue', 'green', 'red')
output : My favorite colors are blue green red

Cuz - Python automatically adds a space between each item when you separate them with commas. This is helpful when you want to print several pieces of information together.
    
  
------------------------------------------

here's are all the data types covered in this lesson, along with their types in the terminal:

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

----------------------------------------------

The built-in isinstance() function lets you check if a variable matches a specific data type. It takes in an object and the type you want to check it against, then returns a boolean. Here are some examples:

isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False

==================================================================

2nd -  Introduction to Strings
------------------------------

-> If you need a multi-line string, you can use triple double quotes or single quotes:

Example Code

my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''


-> If your string contains either single or double quotation marks, then you have two options -

-->   Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:

Example Code

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

-->  Escape the single or double quotation mark in the string with a backslash (\). With this method, you can use either single or double quotation marks to wrap the string itself:

Example Code

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

-> And you have to check if you have a lot of quot - 

Example Code

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False


-> If you want to count length

Example Code

my_str = 'Hello world'
print(len(my_str))  # 11

-> If you want position call -

Example Code

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1])  # d
print(my_str[-2]) # l


-> Python doesn't draw a hard line between those two groups. Instead, all data gets treated as objects, and some objects are immutable while others are mutable. Immutable data types can't be modified or altered once they're declared. You can point their variables at something new, which is called reassignment, but you can't change the original object itself by adding, removing, or replacing any of its elements.

	Strings are immutable data types in Python. This means that you can reassign a different string to a variable:

Example Code

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

But direct modification of a string isn't allowed

Example Code

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

---------------------------------------------------------

What Are String Concatenation and String Interpolation?
-------------------------------------------------------

-> string concatenation (+)

Example Code

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World


if Example Code

name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

--> But can change type

Example Code

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26


--> And you can also use augmented assignment operator (+=)

Example Code

name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26


-> string interpolation (F-string with {})

Example Code
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

---------------------------------------------------------

What Is String Slicing and How Does It Work?
-------------------------------------------------------


In a previous lesson, you learned how each character in a string can be identified by its index (starting from zero), and accessed using the bracket notation:

Example Code

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

-> String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax:

Example Code

string[start:stop]

-> If you want to extract characters from a certain index to another, you just separate the start and stop indices with a colon:

Example Code

my_str = 'Hello world'
print(my_str[1:4]) # ell

Note that the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to, but not including, the character at index 4.


-> You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively. For example, here's what happens if you omit the start index:

Example Code

my_str = 'Hello world'
print(my_str[:7])  # Hello w

-> This extracts everything from index 0 up to (but not including), the character at index 7. And here's what happens if you omit the stop index:

Example Code

my_str = 'Hello world'
print(my_str[8:])  # rld

This extracts everything from the character at index 8 until the end of the string.


Note that slicing a string does not modify the original string:

Example Code

my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world

-> You can also omit both the start and stop indices, which will extract the whole string:

Example Code

my_str = 'Hello world'
print(my_str[:])  # Hello world

-> Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.

Here's the syntax for that:

Example Code

string[start:stop:step]

-> In the example below, the slicing starts at index 0, stops before 11, and extracts every second character:

Example Code

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

-> A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:

Example Code

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH

---------------------------------------------------------

What Are Some Common String Methods?
-------------------------------------------------------

upper(): Returns a new string with all characters converted to uppercase.

Example Code

my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

lower(): Returns a new string with all characters converted to lowercase.

Example Code

my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.

Example Code

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

replace(old, new): Returns a new string with all occurrences of old replaced by new.

Example Code

my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

Example Code

my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

join(iterable): Joins elements of an iterable into a string with a separator.

Example Code

my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

Example Code

my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.

Example Code
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.

Example Code

my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6

count(substring): Returns the number of times a substring appears in a string.

Example Code

my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2

capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.

Example Code

my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

isupper(): Returns True if all letters in the string are uppercase and False if not.

Example Code

my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

islower(): Returns True if all letters in the string are lowercase and False if not.

Example Code

my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True

title(): Returns a new string with the first letter of each word capitalized.

Example Code

my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World


}

{

Date - 4/16/2026
================

How Do You Work With Integers and Floating Point Numbers? (Numbers and Mathematical Operations)
---------------------------------------------------------

(+)  for addition
(-)  for subtraction
(*)  for multiplication
(/)  for division
(%)  for remainder
(//) for Floor Division !That output will be integer division
(**) for power

-> Floor Division Example -

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0


-> round(): Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer, and returns a whole number with no decimal places:

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

-> abs(): returns the absolute value of a number,

num = -15

absolute_value = abs(num)
print(absolute_value) # 15

-> pow(): raises a number to the power of another or performs modular exponentiation.

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3

-----------------------------------------------------------------------

How Do Augmented Assignments Work? (Numbers and Mathematical Operations)
----------------------------------

Main - 

The basic syntax of an augmented assignment looks like this:

variable <operator>= value

Which is a more efficient way of doing this:

variable = variable <operator> value

---------------------------------

+= , -=, *=, /=, //=, %=, *rrinn*=

---------------------------------

-> You can use some augmented assignment operators with strings.

Example Code

greet = 'Hello'
greet += ' World'

print(greet) # Hello World

--> And the multiplication assignment operator can be used to repeat a string

greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello

----------------------------------

Increment and decrement operators (++ and --) -> They are not work in Python

Example Code - 

my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6

}




