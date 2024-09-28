#s = 'It is a herbaceous perennial which produces flowers in the typical aroid structure: a densely crowded inflorescence called a spadix is subtended by one large bract called a spathe (occasionally two spathes are produced, with the upper spathe smaller). The spadix is generally cream or ivory when young, and turns green with age; the spathe is generally white or white with green nerves distally from the margin, turning green with age. Leaves are basal, glossy and somewhat deeply veined, ovate and acuminate. The petioles are long and the leaves arch gracefully. The plant produces offsets at the base and in time becomes a dense clump. Spathiphyllum wallisii is one of approximately 40 species in a genus of tropical evergreens. It was discovered in the late 19th century growing wild in Colombia. A number of cultivars, many of hybrid origin, are commercially available, such as the larger hybrids "Mauna Loa", named after the Hawaiian volcano, and the even larger “Sensation", which are both popular indoor plants. "Domino" is a finely variegated variety of intermediate size. Its wide natural range includes parts of Mexico, the Caribbean Islands, and northern South America.'
#s = 'Strings implement all of the common sequence operations, along with the additional methods described below. Strings also support two styles of string formatting, one providing a large degree of flexibility and customization (see str.format(), Format String Syntax and Custom String Formatting) and the other based on C printf style formatting that handles a narrower range of types and is slightly harder to use correctly, but is often faster for the cases it can handle (printf-style String Formatting). The Text Processing Services section of the standard library covers a number of other modules that provide various text related utilities (including regular expression support in the re module).'
from collections import Counter

s = input()
exclude_symbols = '!,.?;:#$%^&*(),'
# clear string of excluded symbols
input_string = s.translate(s.maketrans({x: '' for x in exclude_symbols})).lower()
# get Counter of symbols in string
counter_sym = Counter(input_string)
# remove symbols than less common than 2 times
counter_sym_common = {k: v for k, v in counter_sym.items() if v > 2 and k != " "}

# make words counter
input_string = input_string.split()
counter_word = Counter(input_string)

result_words_list = list()
for word in input_string:
    if len(word) >= 5 and len(set(word)) >= 4 and counter_word[word] > 2:
        if word not in result_words_list:
            result_words_list.append(word)
print('\n'.join(sorted(result_words_list)))
