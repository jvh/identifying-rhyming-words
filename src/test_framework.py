#############################################################################################
# File: test_framework.py                                                                   #
#                                                                                           #
# Given an input, tests for the correct output. Uses pytest as the testing framework        #
#############################################################################################

from src import main


def test_disputing():
    main.INPUT_WORD = 'Disputing'
    main.INPUT_WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

    _, words = main.run()

    assert words == ['Computing']


def test_shooting():
    main.INPUT_WORD = 'Shooting'
    main.INPUT_WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

    _, words = main.run()

    assert set(words) == {'Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting'}


def test_orange():
    main.INPUT_WORD = 'Orange'
    main.INPUT_WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

    _, words = main.run()

    assert words == []


def test_convoluting():
    main.INPUT_WORD = 'Convoluting'
    main.INPUT_WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

    _, words = main.run()

    assert set(words) == {'Polluting', 'Diluting'}


