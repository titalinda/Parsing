# Program: Recursive Descent Parser
# Author: Alyssa
# Date: 10/22/2023
# Description: A recursive descent parser for 
# the language of Kalee, using {q,c,u}
#
# Grammar:
# S -> cC
# S -> qQ
# S -> uU
# S -> empty
# C -> qC
# C -> uC
# C -> cC
# C -> empty
# Q -> qB
# Q -> uQ'
# Q -> cC
# Q -> empty
# Q' -> uQ'
# Q' -> qQ
# Q' -> cC
# Q' -> empty
# U -> uB
# U -> qU'
# U -> cC
# U -> empty
# U' -> qU'
# U' -> uU
# U' -> cC
# U' -> empty
# B -> qB
# B -> uB
# B -> cC

import sys

# Get command line input
Word = sys.argv[1]

Next_token = Word[0]
Word = Word[1:]

def S():

    global Next_token
    global Word
 
    # Check for which production rule to use
    if Next_token == '-':
        match('-')
        S()
    if Next_token == 'c':
        match('c')
        C()
    if Next_token == 'q':
        match('q')
        Q()
    if Next_token == 'u':
        match('u')
        U()
    else:
        # Empty
        pass

def C():

    global Next_token
    global Word

    # Check for which production rule to use
    if Next_token == 'q':
        match('q')
        C()
    if Next_token == 'u':
        match('u')
        C()
    if Next_token == 'c':
        match('c')
        C()
    else:
        # Empty
        pass

def Q():

    global Next_token
    global Word

    # Check for which prodction rule to use
    if Next_token == 'q':
        match('q')
        B()
    if Next_token == 'u':
        match ('u')
        Q2()
    if Next_token == 'c':
        match('c')
        C()
    else:
        # Empty
        pass

def Q2():

    global Next_token
    global Word

    # Check for which production rule to use
    if Next_token == 'u':
        match('u')
        Q2()
    if Next_token == 'q':
        match('q')
        Q()
    if Next_token == 'c':
        C()
    else:
        # Empty
        pass

def U():

    global Next_token
    global Word

    # Check for which production rule to use
    if Next_token == 'u':
        match('u')
        B()
    if Next_token == 'q':
        match('q')
        U2()
    if Next_token == 'c':
        match('c')
        C()
    else:
        # Empty
        pass

def U2():

    global Next_token
    global Word

    if Next_token == 'q':
        match('q')
        U2()
    if Next_token == 'u':
        match('u')
        U()
    if Next_token == 'c':
        match('c')
        C()
    else:
        # Empty
        pass

def B():

    global Next_token
    global Word

    # Check for which production rule to use
    if Next_token == 'q':
        match('q')
        B()
    if Next_token == 'u':
        match('u')
        B()
    if Next_token == 'c':
        match('c')
        C()
    else:
        # Empty
        pass


def match(token):

    global Next_token
    global Word

    # If the tokens match
    if Next_token == token:
        
        # If the string is not empty
        if len(Word) > 0:
            Next_token = Word[0]
            Word = Word[1:]
        else:

            # Set Next_token to be empty for "Accept" in main
            Next_token = ' '
    else:
        error()

def error():
    print("Reject")
    quit()


def main():
    
    global Word
    global Next_token

    # Call the first state, this is how it always will start
    S()

    if Next_token == ' ':
        print("Accept")
    else:
        print("Reject")


main()