import pytest
from classes import *

# słowa mogą składać się tylko z liter 
@pytest.mark.parametrize("word, expected_value", [("mleko", True), ("m1eko", False)])
def test_is_alpha(word, expected_value):
    assert Validator.only_letters(word) == expected_value

# wprowadzone słowa muszą być tej samej długości, inaczej wprowadzenie słowa nie będziemiało sensu 
@pytest.mark.parametrize("word, to_guess", [("mleko", "okelm", True), ("mleko", "mlek", False)])
def test_words_equal(word, to_guess):
    assert Validator.check_words_lenght(word, to_guess)
    if((len(word) == len(to_guess))) == True:
        return True
    else:
        return False
# test_words_equal("mleko", "mle")

# słowo wprowadzone przez użytkownika musi być izogramem, bo na tym polega gra
def test_isogram(word):
    word = word.lower()
    assert Validator.is_isogram(word)
    letter_list = []
    for letter in word:
        if letter in letter_list:
            return False
        letter_list.append(letter)
    return True
# test_isogram("mall")
    
    
        

    

