# Identifying Rhyming Words

## Introduction
This project aims to identify phonetically similar words. Given a word, along with a list of words, this program outputs the word (if any) in the list which best rhymes with that given word.

**NOTE**: This was done as a personal project.

## Tasks Overview
Firstly, we must address what makes 2 words rhyme. According to [1], ”rhyme by definition is based on a regular recurrence of equivalent phonemes or phonemic groups”. As previous works, [2], have focussed primarily on identifying syllables within words, it seems a natural choice to have the main focus here. However, the task of decomposing a word into its constituent syllables is not an easy one, [3], and algorithms are not perfect in defining the boundaries for the syllables. Not only that, but, given the time constraints, it seems unreasonable to attmept this approach. I have therefore decided to split the word into it’s phonetic alphabet representation and compare against this. From Antimoon (http://www.antimoon.com/how/pronunc-soundsipa.htm), I have obtained a list of the phonetic alphabet, and their corresponding English equivalent.

## Decomposing Words Into Phonetics
I defined all of the phonetics in a constant, `PHONETIC_ALPHABET`. `PHONETIC_ALPHABET` is a dictionary representing English equivalent: phonetic alphabet index. I have chosen to represent the phonetic alphabet as numbers surrounded by slashes, this is due to the nature in which I find-and-replace characters in a given string. If I were to use the actual phonetic alphabet, it may end up replacing elements within the alphabet (say we are replacing all a’s, if we have a phonetic /a/, the a would be replaced) – this would mean we would need extra checks in place in order to determine if the substring is surrounded by slashes.

Each phoneme will contain literal letters (either a vowel or consonant, always lowercase), however, phonemes may contain modifiers. Modifiers allow for a rule to be in place. Modifiers which are either ”S” or ”E” specify that the substring in the phenome must appear at the start or end respectively. For example, the phenome ”easE” specifies that the substring ”eas” must appear at the end of the target word for that phonetic type to be valid. Modifiers can also take on the values ”V” and ”C”, meaning vowels and consonants. This is a wildcard which specifies that the phenome is valid iff the target word has the appropriate character in the position specified by the phenome. For example, ”Cear” specifies that the phenome is only valid within the string if the substring ”ear” exists in the string and any consonant immediately preceeds it.
Given this, when we run through the list, we take the original word in the list and create a copy – the phonetic word, which replaces the original word slowly with the phonemes. It’s important to note that we go through the phonetic list largest (in terms of length) first. This is done as we want to fit the most specific phenomes first in order to prevent falsely fitting smaller, and perhaps incorrect, phenomes.

## Identifying the Best Rhyming Words
Now that we have a list of the phonetic representation of the words, we now have to identify which ones fit the target word best. In order to do this, we begin by splitting the word into a list, remove the slashes surrounding each phenome, and remove any leftover whitespace. We then reverse the word such that we give precendence towards the ending of the word as this is what (most likely) determines which words rhyme. Once we have done that, we need to determine if the phenome exists approximately in the same position in both the tested word and the target word. If they are within a distance of 2 (in terms of index), we can say that they have enough influence on each other that they could impact their rhyming ability. We also ensure that, using number incorrect at beginning, there is at least 1 similar phenome in the last 1/3 of the target word (again, the ending being most important). Words are assigned a score based on their similarity in terms of phenomes, with the lowest score being the best scoring.

We then pick a random word from a list of the best scoring words in order to display to the user.

## References
* [1] Roman Jakobson. Linguistics and poetics. In Style in language, pages 350–377. MA: MIT Press, 1960.
* [2] Franklin Mark Liang. Word hy-phen-a-tion by com-put-er. Technical report, Calif. Univ. Stanford. Comput. Sci. Dept., 1983.
* [3] Yannick Marchand, Connie R Adsett, and Robert I Damper. Evaluating automatic syllabifi- cation algorithms for english. 2007.
