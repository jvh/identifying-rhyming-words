
WORD = 'Disputing'
WORD_LIST = ['ooohooo', 'Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

# The phonetic language in the form letters: phonetic sound.
# Phonetic alphabet taken from http://www.antimoon.com/how/pronunc-soundsipa.htm
# C denotes that there must be a consonant in this position
# S denotes it must appear at the beginning of sentence
# E denotes end of the sentence
# V denotes a vowel
PHONETIC_ALPHABET = {

    # Vowels
    'u': '/1/',
    'ar': '/2/',
    'Cath': '/2/',
    'a': '/3/',
    'easE': '/3/',
    'Sa': '/4/',
    'ur': '/5/',
    'Cear': '/5/',
    'i': '/6/',
    'e': '/7/',
    'ee': '/7/',
    'ea': '/7/',
    'Cey': '/7/',
    'o': '/8/',
    'Cour': '/9/',
    'all': '/9/',
    'ut': '/10/',
    'pu': '/10/',
    'ue': '/11/',
    'oo': '/11/',
    'iCe': '/12/',
    'eye': '/12/',
    'ow': '/13/',
    'ou': '/13/',
    'ay': '/14/',
    'eigh': '/14/',
    'onV': '/15/',
    'omV': '/15/',
    'oE': '/15/',
    'oy': '/16/',
    'oi': '/16/',
    'Chere': '/17/',
    'air': '/17/',
    'ear': '/18/',
    'ere': '/19/',
    'ure': '/20/',
    'ourA': '/20/',

    # Consonants
    'b': '/21/',
    'd': '/22/',
    'f': '/23/',
    'g': '/24/',
    'h': '/25/',
    'y': '/26/',
    'c': '/27/',
    'ck': '/27/',
    'l': '/28/',
    'm': '/29/',
    'n': '/30/',
    'ing': '/31/',
    'p': '/32/',
    'r': '/33/',
    's': '/34/',
    'ss': '/34/',
    'sh': '/35/',
    't': '/36/',
    'tt': '/36/',
    'ch': '/37/',
    'thin': '/38/',
    'oth': '/38/',
    'th': '/39/',
    'v': '/40/',
    'w': '/41/',
    'z': '/42/',
    'eas': '/43/',
    'is': '/43/',
    'j': '/44/',
    'ge': '/44/',


    # # testing
    # 'Comp': '/420/',
    # # 'ooo': '/yes/',
    'Sooo': '/100/',
    'oooE': '/101/'
}

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiou'


def check_char_mod_validity(char, modifier, index_of_substr=-1):
    if modifier == 'C':
        if char in CONSONANTS:
            return True
    elif modifier == 'V':
        if char in VOWELS:
            return True
    return False


def check_pos_mod_validity(modifier, phonetic, word, index_of_substr):
    if modifier == 'S':
        if index_of_substr == 0:
            return True
    # Ensuring phonetic in correct place in word
    elif modifier == 'E':
        a = len(word)
        b = len(phonetic)+index_of_substr
        if len(phonetic)+index_of_substr == len(word):
            return True
    return False


def indexes_in_which_phonetic_appears(word, phonetic):
    substr_indexes = []
    temp = word
    total_index = 0
    while len(temp) > 0:
        index = temp.index(phonetic)
        end_of_phonetic = (index + len(phonetic))
        temp = temp[end_of_phonetic:]
        if total_index == 0:
            substr_indexes.append(index)
        else:
            substr_indexes.append(total_index + index)
        total_index += end_of_phonetic

        if len(temp) < len(phonetic):
            break

    return substr_indexes

def replace_word_with_phonetic(before, word, phonetic_word, phonetic, mod, char_in_mod_pos=-1, modifiers=[],
                               maximum_number_replacements=-1):
    if before:
        mod_phonetic_order = mod + phonetic
    else:
        mod_phonetic_order = phonetic + mod

    if maximum_number_replacements != -1:
        word = word.replace(phonetic, '*', maximum_number_replacements)
        phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[mod_phonetic_order],
                                              maximum_number_replacements)
    else:
        word = word.replace(char_in_mod_pos + phonetic, '*')
        if modifiers[mod]:
            phonetic_word = phonetic_word.replace(char_in_mod_pos + phonetic,
                                                  PHONETIC_ALPHABET[mod + phonetic])

def split_words_into_syllables(word_list):
    phonetic_word_list = []
    # We are fitting the word to the phonetics to the fullest extent, such that largest phonetics are fitted first
    phonetic_largest = sorted([x for x in PHONETIC_ALPHABET], key=len, reverse=True)

    for word in word_list:
        word_added = False
        original = word
        word = word.lower()
        phonetic_word = word
        # Checking what exists (MOVE THIS TO OUTER LOOP)
        for phonetic in phonetic_largest:

            settt = set(word)

            # No further chars left
            if set(word) == {'*'}:
                phonetic_word_list.append(phonetic_word)
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

            if phonetic in word:

                # substr_indexes = indexes_in_which_phonetic_appears(word, phonetic)
                index = word.index(phonetic)
                # for index in substr_indexes:
                if modifiers:
                    for mod in modifiers:

                        # If the substring within the word should be replaced with its phonetic representation
                        replace = False

                        if mod == 'S':
                            replace = word.startswith(phonetic)
                            if replace:
                                word = word.replace(phonetic, '*', 1)
                                phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[mod + phonetic], 1)
                        elif mod == 'E':
                            replace = word.endswith(phonetic)
                            if replace:
                                word = word.replace(phonetic, '*', 1)
                                phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[phonetic + mod], 1)
                        else:
                            if modifiers[mod]:
                                char_in_mod_pos = word[index - 1]
                            else:
                                char_in_mod_pos = word[index + len(mod)]
                            if check_char_mod_validity(char_in_mod_pos, mod):
                                # Replaces the substring with * in the word, and replaces the substring with the
                                # phonetic representation in the phonetic_word
                                word = word.replace(char_in_mod_pos + phonetic, '*')
                                if modifiers[mod]:
                                    phonetic_word = phonetic_word.replace(char_in_mod_pos + phonetic,
                                                                          PHONETIC_ALPHABET[mod + phonetic])
                                else:
                                    phonetic_word = phonetic_word.replace(char_in_mod_pos + phonetic,
                                                                          PHONETIC_ALPHABET[phonetic + mod])

                else:
                    word = word.replace(phonetic, '*')
                    phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[phonetic])

        if not word_added:
            phonetic_word_list.append(phonetic_word)

    # print(phonetic_largest)
    return phonetic_word_list

    # Idea, go through each letter and write down the phonetics for that letter. Compare the number of similar phonetics

def find_best_matches(word_list):
    best_matches = []

    input_word = word_list[0]
    # Splits the word into phonetics, removing the /x/ either side
    formatted_input_word = list(filter(None, input_word.split('/')))

    print(formatted_input_word)
    print()

    for i in range(1, len(word_list)):
        print(WORD_LIST[i - 1])
        word = word_list[i]
        word = list(filter(None, word.split('/')))
        print(word)

    return best_matches


if __name__ == '__main__':
    phonetic_word_list = split_words_into_syllables([WORD] + WORD_LIST.copy())
    best_matches = find_best_matches(phonetic_word_list)