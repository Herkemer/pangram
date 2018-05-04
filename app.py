'''
app.py - Pangram checker API

This API allows the user to check strings to see if they are pangrams:
https://en.wikipedia.org/wiki/Pangram

Multiple implementations are provided.

This runs in the chalice framework which provides an easy method for setting
up AWS API Gateway/Lambda functions.

See https://github.com/aws/chalice for more information.
'''

import string

from chalice import Chalice

app = Chalice(app_name='pangram')

alphabet = frozenset(string.ascii_lowercase)


def is_pangram(input_string):
    '''
    Function to return if input string is a pangram, using english alphabet.

    Args:
        input_string (str): Input string of characters to check.

    Returns:
        bool: True if input string is a pangram, False otherwise.
    '''

    # This checks to make sure the input forms a superset.
    # Lowercase all characters and because we are checking if we can form
    # a superset of the alphabet numbers/symbols are ignored.
    # return set(input_string.lower()).issuperset()
    return set(input_string.lower()) >= alphabet


def is_pangram2(input_string):
    '''
    Function to return if input string is a pangram.

    Uses knowledge of english alphabet (ie 26 characters).

    Args:
        input_string (str): Input string of characters to check.

    Returns:
        bool: True if input string is a pangram, False otherwise.
    '''
    pg = set()

    for char in input_string:
        # Have to pay attention to each character, can't safely ignore numbers
        # and symbols using this method.
        if char.isalpha():
            pg.add(char.lower())

    return len(pg) == 26


@app.route('/')
def index():
    '''
    Basic "Hello World" endpoint to use as validation/testing during development.

    Returns:
        JSON: Just a basic JSON structure
    '''
    return {'hello': 'world'}


@app.route('/pangram/{input_string}')
def pangram(input_string):
    '''
    Endpoint that checks input to see if it is a pangram.

    Args:
        input_string (str): Input string of characters to check.

    Returns:
        JSON: Key is pangram, value is true or false.
    '''

    pangram_p = is_pangram(input_string)

    return {'pangram': pangram_p}


@app.route('/pangram2/{input_string}')
def pangram2(input_string):
    '''
    Endpoint that checks input to see if it is a pangram.

    This function calls the alternative pangram checker.

    Args:
        input (str): Input string of characters to check.

    Returns:
        JSON: Key is pangram, value is true or false.
    '''

    pangram_p = is_pangram2(input_string)

    return {'pangram': pangram_p}
