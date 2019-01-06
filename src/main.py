#############################################################################################
# File: main.py                                                                             #
#                                                                                           #
# Given a list of words (the first being the word in which we are searching for others that #
# rhyme), find the rhyming words to the specified input                                     #
#############################################################################################


import random

INPUT_WORD = 'kiki'
INPUT_WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

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
    'ie': '/6/',
    'e': '/7/', 'ee': '/7/', 'ea': '/7/', 'Cey': '/7/', 'i': '/7/',
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
    'c': '/27/', 'ck': '/27/', 'k': '/27',
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

        i += 0

        total = -1

        word = list(filter(None, word.split('/')))
        word.reverse()

        # This tracks the number of cumulative phonetic characters which don't appear in both words, only counted
        # from the end of the word (once a character is correctly matched, this is set to -1). This determines if the
        # word is eligible to be considered
        number_incorrect_at_beginning = 0

        # Describes if the word is eligible to be considered for validity
        eligible = True

        # The number of successive correct inputs in a row
        successive_inputs = 0

        for i in range(len(word)):

            phonetic_type = word[i]

            if phonetic_type in formatted_input_word:
                # The word is valid
                number_incorrect_at_beginning = -1

                # Score is distance from each other from end of word, end of word is preferred so penalisation applied
                # to later indexes, unless there are correct successive phonetics, at which point no penalty is applied
                index_in_input = formatted_input_word.index(phonetic_type)
                if successive_inputs > 0:
                    score = abs(index_in_input - word.index(phonetic_type))
                else:
                    distance = abs(index_in_input - word.index(phonetic_type))
                    # Too far away to be considered applicable
                    if distance > 2:
                        word_len = len(word)
                        score = (input_len / word_len) * 10
                    else:
                        score = distance + (index_in_input * 6)

                successive_inputs += 1

                if total == -1:
                    total = score
                else:
                    total += score
            else:
                if number_incorrect_at_beginning != -1:
                    number_incorrect_at_beginning += 1
                    # Must have a matching phonetic within the last half of input, otherwise does not match
                    if number_incorrect_at_beginning == round(input_len / 2):
                        # Remove from the list of possible items to consider as this is no longer a valid choice
                        eligible = False
                        break

                successive_inputs = 0
                # Penalise by 10 points if doesn't exist, corrected for length
                word_len = len(word)

                score = (input_len / word_len) * 10
                if total == -1:
                    total = score
                else:
                    total += score

        if total > -1 and eligible:
            if total in scores:
                scores[total].append({key: word})
            else:
                scores[total] = [{key: word}]

    best_matched_words = []

    # Returns those matches which received a score of 5 between themselves
    # best_matched_words = [scores[key] for key in sorted(scores) if key < sorted(scores)[0] + 5]

    best_scores = list(sorted(scores))
    look = ((input_len) * 10)
    sorted_scores = [scores[key] for key in best_scores if key < look]

    if not sorted_scores:
        return []
    # If there are more than 1 word with the same best score, take these as being best matched
    elif len(sorted_scores[0]) > 1:
        best_matched_words = best_scores
    else:
        difference = max(scores) - min(scores)
        best = best_scores[0] + 5

        # Compare scores against best score. They will be included if within 1/2 difference or within 5, whatever is \
        # largest

        compare = max(difference/2, best)

        # Otherwise find scores within 5 of best
        best_within_range = [scores[key] for key in scores if key < compare]
        best_matched_words += best_within_range

    return best_matched_words


def run():
    """
    Kicks off the running of the program.

    :return (str): [one of] The word which rhymes the best
    """
    phonetic_list = split_words_into_phonetics([INPUT_WORD] + INPUT_WORD_LIST.copy())
    best_matches = find_best_matches(phonetic_list)

    if best_matches:
        word_selection = []
        for selection in best_matches:
            for word in selection:
                word_selection.append(list(word.keys())[0])
        chosen_word = random.choice(word_selection)
    else:
        word_selection = []
        chosen_word = "NOTHING (there are no rhyming words)"

    return chosen_word, word_selection


if __name__ == '__main__':
    best_word, _ = run()
    print("With input word {}, the best rhyming match is {}.".format(INPUT_WORD, best_word))
