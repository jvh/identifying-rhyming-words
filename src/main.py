#############################################################################################
# File: main.py                                                                             #
#                                                                                           #
# Given a list of words (the first being the word in which we are searching for others that #
# rhyme), find the rhyming words to the specified input                                     #
#############################################################################################


import random

INPUT_WORD = 'List'
INPUT_WORD_LIST = ['Cyst', 'Fist', 'Kissed', 'Midst']

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
    'ie': '/6/', 'yC': '/6/',
    'e': '/7/', 'ee': '/7/', 'ea': '/7/', 'Cey': '/7/', 'i': '/7/',
    'o': '/8/',
    'Cour': '/9/', 'all': '/9/',
    'ut': '/10/', 'pu': '/10/',
    'ue': '/11/', 'oo': '/11/',
    'eye': '/12/',
    'ow': '/13/', 'ou': '/13/',
    'ay': '/14/', 'eigh': '/14/',
    'onV': '/15/', 'omV': '/15/', 'oE': '/15/',
    'oy': '/16/', 'oi': '/16/',
    'Chere': '/17/', 'air': '/17/',
    'ear': '/18/',
    'ere': '/19/',
    'ure': '/20/', 'ourE': '/20/',

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
    'eas': '/43/', 'is': '/43/', 'ys': '/43/',
    'j': '/44/', 'ge': '/44/',
}

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiou'

phonetics_with_modifiers = {}


def find_phonetics_with_modifiers():
    """
    This finds all those phonetics with modifiers existing in them

    :return {str: (str, [{str: bool}])}: The phoneme, containing a tuple which specifies its trimmed version (without
    the modifiers) as it's first element along with, as its second element, a dict containing the modifiers existing
    within and a corresponding bool where True specifies that the modifier begins at the start.
    """
    global phonetics_with_modifiers

    for phoneme in PHONETIC_ALPHABET:
        # If the phoneme contains a modifier
        modifiers = {}
        for i in range(len(phoneme)):
            char = phoneme[i]
            if char.isupper():
                # True if modifier at start of phoneme, false if at end (or otherwise)
                if i == 0:
                    modifiers[char] = True
                else:
                    modifiers[char] = False

        if modifiers:
            trimmed = ''
            for char in modifiers:
                trimmed = phoneme.replace(char, '')

            phonetics_with_modifiers[phoneme] = (trimmed, modifiers)


def check_char_mod_validity(char, modifier):
    """
    Given a modifier to a char (checking if either consonant -- C, or vowel -- V), return is letter in position is
    indeed a vowel or consonant

    :param (str) char: The character held in the word
    :param (str) modifier: The modifier which we're comparing against
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

    :param ([str]) word_list: List of the words, first word being the INPUT_WORD.
    :return {str: str}: The original word along with its phoneme representation
    """
    phonetic_word_list = {}
    # We are fitting the word to the phonetics to the fullest extent, such that largest phonetics are fitted first
    phonetic_largest = sorted([x for x in PHONETIC_ALPHABET], key=len, reverse=True)

    for w in word_list:

        word_added = False
        original = w
        w = w.lower()
        # This stores the phoneme equivalent, we take the original and replace as we go along
        phonetic_word = w

        for phoneme in phonetic_largest:

            # No further chars left
            if set(w) == {'*'}:
                phonetic_word_list[original] = phonetic_word
                word_added = True
                break

            # If phoneme contains modifier, get trimmed version and corresponding modifiers
            if phoneme in phonetics_with_modifiers:
                phoneme, modifiers = phonetics_with_modifiers[phoneme]
            else:
                modifiers = []

            if phoneme in w:

                index = w.index(phoneme)

                if modifiers:
                    for mod in modifiers:
                        # If mod S or E, ensure the modifier is met in word
                        if mod == 'S':
                            replace = w.startswith(phoneme)
                            if replace:
                                w = w.replace(phoneme, '*', 1)
                                phonetic_word = phonetic_word.replace(phoneme, PHONETIC_ALPHABET[mod + phoneme], 1)
                        elif mod == 'E':
                            replace = w.endswith(phoneme)
                            if replace:
                                w = w.replace(phoneme, '*', 1)
                                phonetic_word = phonetic_word.replace(phoneme, PHONETIC_ALPHABET[phoneme + mod], 1)
                        else:
                            # If modifier is anything else, ensure that condition is met by checking the character in
                            # the word which is specified by the boolean held by the mod dict (True meaning mod is
                            # at beginning of phoneme)
                            if modifiers[mod]:
                                char_in_mod_pos = w[index - 1]
                            else:
                                char_in_mod_pos = w[index + len(mod)]

                            if check_char_mod_validity(char_in_mod_pos, mod):
                                # Replaces the substring with * in the word, and replaces the substring with the
                                # phoneme representation in the phonetic_word
                                w = w.replace(char_in_mod_pos + phoneme, '*')
                                if modifiers[mod]:
                                    phonetic_word = phonetic_word.replace(char_in_mod_pos + phoneme,
                                                                          PHONETIC_ALPHABET[mod + phoneme])
                                else:
                                    phonetic_word = phonetic_word.replace(char_in_mod_pos + phoneme,
                                                                          PHONETIC_ALPHABET[phoneme + mod])

                else:
                    # If no mods, just do regular replacement
                    w = w.replace(phoneme, '*')
                    phonetic_word = phonetic_word.replace(phoneme, PHONETIC_ALPHABET[phoneme])

        if not word_added:
            # Add to list even if it hasn't been fully replaced by phonetics
            phonetic_word_list[original] = phonetic_word

    return phonetic_word_list


def find_best_matches(words_list):
    """
    Given all possible matches, finds only the best ones

    :param ({}) words_list: Represents the original word: phonetic representation
    :return ([{}]): A list of the best scoring words, held in a dict with original word: phonetic representation
    """
    # The scores of eligible words
    scores, input_len = find_possible_matches(words_list)

    best_matched_words = []
    best_scores = list(sorted(scores))
    # Only chooses those scores which are better than the input length of the input phoneme word * 10
    limited_scores = [scores[key] for key in best_scores if key < (input_len * 10)]

    if not limited_scores:
        return []

    # If there are more than 1 word with the same best score, take these as being best matched
    elif len(limited_scores[0]) > 1:
        best_matched_words = [limited_scores[0]]

    else:
        difference = max(scores) - min(scores)
        best = best_scores[0] + 5

        # Compare scores against best score. They will be included if within 1/2 difference or within 5, whatever is \
        # largest
        compare = max(difference/2, best)

        best_within_range = [scores[key] for key in scores if key < compare]
        best_matched_words += best_within_range

    return best_matched_words


def find_possible_matches(words_list):
    """
    Given all phonetic representation of words, score them based on likelihood of rhyming. Lower score is better.

    :param ({}) words_list: Represents the original word: phonetic representation
    :return ({{}}): Returns the score of each of the words given, given that they are eligible
    """
    # Assigned a score with score: [corresponding values]. Lower is better.
    scores = {}

    input_word = words_list[INPUT_WORD]
    # Splits the word into phonetics (list representation), removing the /x/ either side
    formatted_input_word = list(filter(None, input_word.split('/')))
    # Reverses the phonetic word as rhymes are more often determined by the ending of the word
    formatted_input_word.reverse()
    input_len = len(formatted_input_word)

    i = 0

    for key, word in words_list.items():
        # Skips first item
        if i == 0:
            i = -1
            continue
        i += 0

        # Holds the total score for that phonetic word
        total = -1

        word = list(filter(None, word.split('/')))
        word.reverse()

        # Timeout feature which determines eligibility of the word given that there is a match within the last 1/3 of
        # the word
        number_incorrect_at_beginning = 0

        # Describes if the word is eligible to be considered for validity
        eligible = True

        # The number of successive correct inputs in a row
        successive_inputs = 0

        for phonetic_type in word:

            if phonetic_type in formatted_input_word:
                # The word is valid
                number_incorrect_at_beginning = -1

                # Successive matching strings are rewarded by not suffering any penalisation
                index_in_input = formatted_input_word.index(phonetic_type)
                distance = abs(index_in_input - word.index(phonetic_type))

                if successive_inputs > 0:
                    score = distance
                else:
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
                # Phonetics do not match, penalise
                if number_incorrect_at_beginning != -1:
                    number_incorrect_at_beginning += 1
                    # Must have a matching phonetic within the last 1/3 of input, otherwise presumed not to rhyme
                    if number_incorrect_at_beginning == round(input_len / 3):
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

        # If phonetic word is eligible, add score to list
        if total > -1 and eligible:
            if total in scores:
                scores[total].update({key: word})
            else:
                scores[total] = {key: word}

    return scores, input_len


def run():
    """
    Kicks off the running of the program.

    :return (str): [one of] The word which rhymes the best
    """
    # Finding those phonetics with modifiers
    find_phonetics_with_modifiers()

    phonetic_list = split_words_into_phonetics([INPUT_WORD] + INPUT_WORD_LIST.copy())
    best_matches = find_best_matches(phonetic_list)

    word_selection = []

    if best_matches:
        for w in best_matches:
            word_selection += [k for k in w.keys()]
        chosen_word = random.choice(word_selection)
    else:
        chosen_word = "NOTHING (there are no rhyming words)"

    return chosen_word, word_selection


if __name__ == '__main__':
    best_word, _ = run()
    print("With input word {}, the best rhyming match is {}.".format(INPUT_WORD, best_word))
