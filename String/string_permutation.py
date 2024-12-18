import itertools

a_string = 'abc'
permutations = itertools.permutations(a_string)
permutations_list = [' '.join(p) for p in permutations]
print(permutations_list)

def get_permutations(string, i=0):
    if i == len(string):
        print("".join(string))
    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        get_permutations(words, i + 1)

get_permutations('abc')