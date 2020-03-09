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


def test_science():
    main.INPUT_WORD = 'Science'
    main.INPUT_WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

    _, words = main.run()

    assert not words


def test_twist():
    main.INPUT_WORD = 'Twist'
    main.INPUT_WORD_LIST = ['Cyst', 'Fist', 'Kissed', 'Midst']

    _, words = main.run()

    assert set(words) == {'Fist', 'Cyst'}


def test_list():
    main.INPUT_WORD = 'List'
    main.INPUT_WORD_LIST = ['Cyst', 'Fist', 'Kissed', 'Midst']

    _, words = main.run()

    assert set(words) == {'Fist', 'Cyst'}


def test_missed():
    main.INPUT_WORD = 'Missed'
    main.INPUT_WORD_LIST = ['Cyst', 'Fist', 'Kissed', 'Midst']

    _, words = main.run()

    assert set(words) == {'Kissed'}


def test_coding():
    main.INPUT_WORD = 'Coding'
    main.INPUT_WORD_LIST = ['Cyst', 'Fist', 'Kissed', 'Midst']

    _, words = main.run()

    assert not words
