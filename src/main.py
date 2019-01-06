"""
Given a list of words (the first being the word in which we are searching for others that rhyme), find the rhyming
words to the specified input

:param word_list:
:return:
"""

import random

INPUT_WORD = 'orange'
INPUT_WORD_LIST = ['ooohooo', 'Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

# The phonetic language in the form substring: phonetic_sound_label. I have decided to use numbers within // in order to
#     denote a phonetic character. I shall be replacing the substrings in a given word with their phonetic equivalents.
# Phonetic alphabet taken from http://www.antimoon.com/how/pronunc-soundsipa.htm
# C denotes that there must be a consonant in this position
# S denotes it must appear at the beginning of sentence
# E denotes end of the sentence
# V denotes a vowel
PHONETIC_ALPHABET = {
    # Vowels
    'u': '/1/',
    'ar': '/2/', 'Cath': '/2/',
    'a': '/3/', 'easE': '/3/',
    'Sa': '/4/',
    'ur': '/5/', 'Cear': '/5/',
    'i': '/6/',
    'e': '/7/', 'ee': '/7/', 'ea': '/7/', 'Cey': '/7/',
    'o': '/8/',
    'Cour': '/9/', 'all': '/9/',
    'ut': '/10/', 'pu': '/10/',
    'ue': '/11/', 'oo': '/11/',
    'iCe': '/12/', 'eye': '/12/',
    'ow': '/13/', 'ou': '/13/',
    'ay': '/14/', 'eigh': '/14/',
    'onV': '/15/', 'omV': '/15/', 'oE': '/15/',
    'oy': '/16/', 'oi': '/16/',
    'Chere': '/17/', 'air': '/17/',
    'ear': '/18/',
    'ere': '/19/',
    'ure': '/20/', 'ourA': '/20/',

    # Consonants
    'b': '/21/',
    'd': '/22/',
    'f': '/23/',
    'g': '/24/',
    'h': '/25/',
    'y': '/26/',
    'c': '/27/', 'ck': '/27/',
    'l': '/28/',
    'm': '/29/',
    'n': '/30/',
    'ing': '/31/',
    'p': '/32/',
    'r': '/33/',
    's': '/34/', 'ss': '/34/',
    'sh': '/35/',
    't': '/36/', 'tt': '/36/',
    'ch': '/37/',
    'thin': '/38/', 'oth': '/38/',
    'th': '/39/',
    'v': '/40/',
    'w': '/41/',
    'z': '/42/',
    'eas': '/43/', 'is': '/43/',
    'j': '/44/', 'ge': '/44/',
}

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiou'


def check_char_mod_validity(char, modifier):
    """
    Given a modifier to a char (checking if either consonant -- C, or vowel -- V), return is letter in position is
    indeed a vowel or consonant

    :param (str) char:
    :param (str) modifier:
    :return (bool): Whether the corresponding char is appropriate according to the modifier
    """
    if modifier == 'C':
        if char in CONSONANTS:
            return True
    elif modifier == 'V':
        if char in VOWELS:
            return True
    return False


def split_words_into_phonetics(word_list):
    """
    Splits a given word into its phonetics.

    :param word_list:
    :return:
    """
    phonetic_word_list = {}
    # We are fitting the word to the phonetics to the fullest extent, such that largest phonetics are fitted first
    phonetic_largest = sorted([x for x in PHONETIC_ALPHABET], key=len, reverse=True)

    for w in word_list:
        word_added = False
        original = w
        w = w.lower()
        # This stores the phonetic equivalent, we take the original and replace as we go along
        phonetic_word = w

        for phonetic in phonetic_largest:

            # No further chars left
            if set(w) == {'*'}:
                phonetic_word_list[original] = phonetic_word
                word_added = True
                break

            # If the phonetic contains a modifier
            modifiers = {}
            for i in range(len(phonetic)):
                char = phonetic[i]
                if char.isupper():
                    # True if modifier at start of phonetic, false if at end (or otherwise)
                    if i == 0:
                        modifiers[char] = True
                    else:
                        modifiers[char] = False

            for char in modifiers:
                phonetic = phonetic.replace(char, '')

            if phonetic in w:

                # substr_indexes = indexes_in_which_phonetic_appears(word, phonetic)
                index = w.index(phonetic)
                # for index in substr_indexes:
                if modifiers:
                    for mod in modifiers:

                        # If the substring within the word should be replaced with its phonetic representation
                        replace = False

                        if mod == 'S':
                            replace = w.startswith(phonetic)
                            if replace:
                                w = w.replace(phonetic, '*', 1)
                                phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[mod + phonetic], 1)
                        elif mod == 'E':
                            replace = w.endswith(phonetic)
                            if replace:
                                w = w.replace(phonetic, '*', 1)
                                phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[phonetic + mod], 1)
                        else:
                            if modifiers[mod]:
                                char_in_mod_pos = w[index - 1]
                            else:
                                char_in_mod_pos = w[index + len(mod)]
                            if check_char_mod_validity(char_in_mod_pos, mod):
                                # Replaces the substring with * in the word, and replaces the substring with the
                                # phonetic representation in the phonetic_word
                                w = w.replace(char_in_mod_pos + phonetic, '*')
                                if modifiers[mod]:
                                    phonetic_word = phonetic_word.replace(char_in_mod_pos + phonetic,
                                                                          PHONETIC_ALPHABET[mod + phonetic])
                                else:
                                    phonetic_word = phonetic_word.replace(char_in_mod_pos + phonetic,
                                                                          PHONETIC_ALPHABET[phonetic + mod])

                else:
                    w = w.replace(phonetic, '*')
                    phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[phonetic])

        if not word_added:
            phonetic_word_list[original] = phonetic_word

    # print(phonetic_largest)
    return phonetic_word_list

    # Idea, go through each letter and write down the phonetics for that letter. Compare the number of similar phonetics


def find_best_matches(words_list):
    scores = {}

    # formatted_words = list(words_list.values())
    input_word = words_list[INPUT_WORD]
    # Splits the word into phonetics, removing the /x/ either side
    formatted_input_word = list(filter(None, input_word.split('/')))
    formatted_input_word.reverse()
    input_len = len(formatted_input_word)

    print(formatted_input_word)
    print()

    i = 0

    for key, word in words_list.items():
        # Skips first item
        if i == 0:
            i = -1
            continue

        total = -1

        word = list(filter(None, word.split('/')))
        word.reverse()

        # The number of successive correct inputs in a row
        successive_inputs = 0

        for phonetic_type in word:

            if phonetic_type in formatted_input_word:
                # Score is distance from each other from end of word, end of word is preferred so penalisation applied
                # to later indexes, unless there are correct successive phonetics, at which point no penalty is applied
                index_in_input = formatted_input_word.index(phonetic_type)
                if successive_inputs > 0:
                    score = abs(index_in_input - word.index(phonetic_type))
                else:
                    score = abs(index_in_input - word.index(phonetic_type)) + (index_in_input * 5)

                successive_inputs += 1

                if total == -1:
                    total = score
                else:
                    total += score
            else:
                successive_inputs = 0
                # Penalise by 10 points if doesn't exist, corrected for length
                word_len = len(word)

                score = (input_len / word_len) * 10
                if total == -1:
                    total = score
                else:
                    total += score

        if total > -1:
            if total in scores:
                scores[total].append({key: word})
            else:
                scores[total] = [{key: word}]

    best_matched_words = []

    # Returns those matches which received a score of 5 between themselves
    # best_matched_words = [scores[key] for key in sorted(scores) if key < sorted(scores)[0] + 5]

    best_scores = list(sorted(scores))
    sorted_scores = [scores[key] for key in best_scores if key < ((input_len - 1) * 10)]

    if not sorted_scores:
        return []
    # If there are more than 1 word with the same best score, take these as being best matched
    elif len(sorted_scores[0]) > 1:
        best_matched_words = best_scores
    else:
        # Otherwise find scores within 5 of best
        best = best_scores[0]
        best_within_range = [scores[key] for key in scores if key < (best + 5)]
        best_matched_words += best_within_range

    return best_matched_words


if __name__ == '__main__':
    phonetic_list = split_words_into_phonetics([INPUT_WORD] + INPUT_WORD_LIST.copy())
    best_matches = find_best_matches(phonetic_list)

    if best_matches:
        word_selection = []
        for selection in best_matches:
            for word in selection:
                word_selection.append(list(word.keys())[0])
        chosen_word = random.choice(word_selection)
    else:
        chosen_word = "NOTHING (there are no rhyming words)"

    print("With input word {}, the best rhyming match is {}.".format(INPUT_WORD, chosen_word))