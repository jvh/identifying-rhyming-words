
WORD = 'Disputing'
WORD_LIST = ['Computing', 'Polluting', 'Diluting', 'Commuting', 'Recruiting', 'Drooping']

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
    'air': 'eə',
    'ear': 'ɪə',
    'ere': 'ɪə',
    'ure': 'ʊə',
    'ourA': 'ʊə',

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
    'ing': 'ŋ',
    'p': '/p/',
    'r': '/r/',
    's': '/s/',
    'ss': '/s/',
    'sh': 'ʃ',
    't': '/t/',
    'tt': '/t/',
    'ch': 'tʃ',
    'thin': 'θ',
    'oth': 'θ',
    'th': 'ð',
    'v': 'v',
    'w': 'w',
    'z': 'z',
    'eas': 'ʒ',
    'is': 'ʒ',
    'j': 'dʒ',
    'ge': 'dʒ'
}


def split_words_into_syllables(target_word, word_list):
    # We are fitting the word to the phonetics to the fullest extent, such that largest phonetics are fitted first
    phonetic_largest = sorted([x for x in PHONETIC_ALPHABET], key=len, reverse=True)

    for word in word_list:
        print()
        print(word)
        # Checking what exists (MOVE THIS TO OUTER LOOP)
        for phonetic in phonetic_largest:

            # If the phonetic contains a modifier

            modifiers = {}
            for i in range(len(phonetic)):
                char = phonetic[i]
                if char.isupper():
                    if i == 0:
                        modifiers[char] = True
                    else:
                        modifiers[char] = False

            for char in modifiers.values():
                phonetic = phonetic.replace(char, '')

            if phonetic in word:
                substr_index = word.index(phonetic)
                if modifiers:
                    for mod in modifiers:
                        modifiers[mod]
                    print(phonetic)

    # print(phonetic_largest)
    pass

    # Idea, go through each letter and write down the phonetics for that letter. Compare the number of similar phonetics

if __name__ == '__main__':
    split_words_into_syllables(WORD, WORD_LIST)