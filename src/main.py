
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
    'u': '/ʌ/',
    'ar': '/ɑ/',
    'Cath': '/ɑ/',
    'a': '/æ/',
    'easE': '/æ/',
    'e': '/e/',
    'Sa': '/ə/',
    'ur': '/ɜ/',
    'Cear': '/ɜ/',
    'i': '/ɪ/',
    'ee': '/e/',
    'ea': '/e/',
    'Cey': '/e/',
    'o': '/ɒ/',
    'Cour': '/ɔ/',
    'all': '/ɔ/',
    'ut': '/ʊ/',
    'pu': '/ʊ/',
    'ue': '/u/',
    'oo': '/u/',
    'iCe': '/aɪ/',
    'eye': '/aɪ/',
    'ow': '/aʊ/',
    'ou': '/aʊ/',
    'ay': '/eɪ/',
    'eigh': '/eɪ/',
    'onV': '/oʊ/',
    'omV': '/oʊ/',
    'oE': '/oʊ/',
    'oy': '/ɔɪ/',
    'oi': '/ɔɪ/',
    'Chere': '/eə/',
    'air': '/eə/',
    'ear': '/ɪə/',
    'ere': '/ɪə/',
    'ure': '/ʊə/',
    'ourA': '/ʊə/',

    # Consonants
    'b': '/b/',
    'd': '/d/',
    'f': '/f/',
    'g': '/g/',
    'h': '/h/',
    'y': '/j/',
    'c': '/k/',
    'ck': '/k/',
    'l': '/l/',
    'm': '/m/',
    'n': '/n/',
    'ing': '/ŋ/',
    'p': '/p/',
    'r': '/r/',
    's': '/s/',
    'ss': '/s/',
    'sh': '/ʃ/',
    't': '/t/',
    'tt': '/t/',
    'ch': '/tʃ/',
    'thin': '/θ/',
    'oth': '/θ/',
    'th': '/ð/',
    'v': '/v/',
    'w': '/w/',
    'z': '/z/',
    'eas': '/ʒ/',
    'is': '/ʒ/',
    'j': '/dʒ/',
    'ge': '/dʒ/',


    # testing
    'Comp': '/yassss/',
    # 'ooo': '/yes/',
    'Sooo': '/hello/',
    'oooE': '/hello/'
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

def split_words_into_syllables(target_word, word_list):
    phonetic_word_list = []
    # We are fitting the word to the phonetics to the fullest extent, such that largest phonetics are fitted first
    phonetic_largest = sorted([x for x in PHONETIC_ALPHABET], key=len, reverse=True)

    for word in word_list:
        word = word.lower()
        phonetic_word = word
        print()
        print(word)
        # Checking what exists (MOVE THIS TO OUTER LOOP)
        for phonetic in phonetic_largest:

            settt = set(word)

            # No further chars left
            if set(word) == {'*'}:
                phonetic_word_list.append(phonetic_word)
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

                substr_indexes = indexes_in_which_phonetic_appears(word, phonetic)

                for index in substr_indexes:
                    if modifiers:
                        for mod in modifiers:
                            if modifiers[mod]:
                                # If modifier is S
                                if mod == 'S':
                                    char_in_mod_pos = word[0]
                                else:
                                    char_in_mod_pos = word[index - 1]
                            else:
                                # If modifier is E
                                if mod == 'E':
                                    char_in_mod_pos = word[-1]
                                else:
                                    char_in_mod_pos = word[index + len(mod)]
                            if check_char_mod_validity(char_in_mod_pos, mod):
                                # Replaces the substring with * in the word, and replaces the substring with the
                                # phonetic representation in the phonetic_word
                                word = word.replace(char_in_mod_pos + phonetic, '*')
                                phonetic_word = phonetic_word.replace(char_in_mod_pos + phonetic,
                                                                  PHONETIC_ALPHABET[mod + phonetic])
                            elif check_pos_mod_validity(mod, phonetic, word, index):
                                word = word.replace(phonetic, '*')
                                phonetic_word = phonetic_word.replace(phonetic,
                                                                  PHONETIC_ALPHABET[mod + phonetic])
                else:
                    word = word.replace(phonetic, '*')
                    phonetic_word = phonetic_word.replace(phonetic, PHONETIC_ALPHABET[phonetic])

        phonetic_word_list.append(phonetic_word)

    # print(phonetic_largest)
    pass

    # Idea, go through each letter and write down the phonetics for that letter. Compare the number of similar phonetics

if __name__ == '__main__':
    split_words_into_syllables(WORD, WORD_LIST)