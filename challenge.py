#function to add "un"
def add_prefix_un(word):
    return "un" + word

#function to group words with prefixes
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return ' :: '.join([prefix] + prefixed_words)

#fuction to remove the suffixes ness
def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4] #removes the ness
        if root_word.endswith("i"):
            root_word += "ness" 
            return root_word
        else:
            return word
        

#function to extract acjective and make a verb
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    if adjective.endswith("y"):
        return adjective[:-1] + "en"
    else:
        return adjective + "en"

#testing phase
print(add_prefix_un("happy"))
print(add_prefix_un("managable"))
print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))
print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))
print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))
