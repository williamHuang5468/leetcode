first_row = 'qwertyuiop'
second_row = 'asdfghjkl'
third_row = 'zxcvbnm'
letter_dict = {}

for i in first_row:
    letter_dict[i] = 1
for i in second_row:
    letter_dict[i] = 2
for i in third_row:
    letter_dict[i] = 3

def findWords(words):
    return [word for word in words if (letterInSameRow(word))]

def letterInSameRow(word):
    if len(word) == 0: # Assume '' will get False
        return False
    word = word.lower()
    num = letter_dict[word[0]] # Get first number of word
    for letter in word:
        if letter_dict[letter] is not num:
            return False
    return True

# findwords

# True
assert findWords(["Dad", "Hello", "Peace"]) == ["Dad"]
assert findWords(["Dad", "Hello", "Peace", "Alaska"]) == ["Dad", "Alaska"]
assert findWords(["Dad", "Hello", "Peace", "quote"]) == ["Dad", "quote"]

# False
assert findWords([""]) == []
assert findWords(["hELLO"]) == []
assert findWords(["mark", "pig"]) == []
assert findWords(["Hello", "Peace"]) == []

# letterInSameRow

# True
assert letterInSameRow('asdf') == True
assert letterInSameRow('qwer') == True
assert letterInSameRow('zxcv') == True
assert letterInSameRow('as') == True
assert letterInSameRow('a') == True
# False
assert letterInSameRow('asdv') == False
assert letterInSameRow('qwef') == False
assert letterInSameRow('zxcr') == False
assert letterInSameRow('') == False
