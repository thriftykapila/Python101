# explaination -> https://www.csestack.org/group-anagrams-list-coding-challenge/

words = ['cat', 'dog', 'god', 'cat']
uniqueWords = list(set(words))  # ['dog', 'cat', 'god']
print('Unique Words ', uniqueWords)
anagramWords = [''.join(sorted(x))
                for x in uniqueWords]  # ['dgo', 'act', 'dgo']
print('Anagram Words ', anagramWords)

finalOut = []
for word in set(anagramWords):
    # find the index for all occurences of string word
    ind = [i for i, x in enumerate(anagramWords) if x == word]  # [1] #[0,2]
    # make the list of all the string which is anagram to each other
    tempOut = []
    for i in ind:
        tempOut.append(words[i])
        temp2 = set(tempOut)  # {'cat'} #{'god','dog'}
    # append all the set to the final output list
    finalOut.append(temp2)  # [{'cat'}, {'dog', 'god'}]

print('Output ', finalOut)
