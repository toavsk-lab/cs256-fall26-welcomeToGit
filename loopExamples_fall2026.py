# ***************************************************************************************************
#   Fall 2026 - Example for Intro to Git In-class Assignment
#   Created by Maggie Vanderberg on Nov. 4th 2026
#   This file contains examples from the loops lecture given during Week 6 of the Fall term.
# ***************************************************************************************************

def loop_through_it(data_structure):
    ''' prints each item in structure that was passed in. None is returned.'''
    for item in data_structure:
        print(item, end="\t")

def num_vowels(input_text):
    ''' count and return the number of vowels in the input text'''
    count = 0
    for character in input_text:
        # check if character should be counted
        # assumes y is not a vowel
        if character.lower() in ['a','e','i','o','u']:
            count += 1
    return count

def nested_loops(i,j):
    ''' prints a grid of X's with i rows and j columns. Nothing is returned.'''
    for row in range(i):
        for col in range(j):
            print("X", end="\t")
        print()  # print a new line after each row
    print()

def test_loop_through_it():
    ''' This function doesn't take any input or return any values. Instead it executes the loop_through_it function
    with various types of input (i.e.., a list, a typle, a string, a set, a dictionary) '''
    print("Looping through structures")
    print("List... ")
    loop_through_it([1,2,3,4,5])    # list
    print("\nTuple... ")
    loop_through_it(('a','b','c'))  # tuple
    print("\nString... ")
    loop_through_it("hello")        # string
    print("\nSet... ")
    loop_through_it({2,10,3,20})    # set (order is not guarenteed)
    print("\nDictionary... ")
    loop_through_it({'discussion':10, 'attendance':5, 'zybook':30}) #dictionary

def test_count_vowels():
    ''' This function doesn't take any input or return any values. It tests the count_vowels function with two 
    different strings.'''
    print("\n\nExecuting count vowel function... ")
    print("And, printing value(s) returned for first execution with 'Hello! My name is Agie O.' :")
    print(num_vowels("Hello! My name is Agie O."))
    text = "How many vowels?"
    print("And, printing value(s) returned for second execution: ", text)
    print(num_vowels(text))
    print()

def test_nested_loops():
    ''' This function doesn't take any input or return any values. It tests the nested_loops function with two 
    different sets of parameters.'''
    print("\nExecuting nested loops function... ")
    print("And, printing value(s) returned for first execution with parameters 3 and 5 :")
    nested_loops(3,5)
    print("And, printing value(s) returned for second execution with parameters 4 and 2 :")
    nested_loops(4,2)
    print()

def main():
    ''' This function is called when this file is executed directly.
    It does not take in any parameters and it will return None '''
    # test loop through structures
    test_loop_through_it()
    # testing count vowels
    test_count_vowels()
    # test nested loops
    test_nested_loops()

if __name__ == "__main__":
    # execute the main function
    main()