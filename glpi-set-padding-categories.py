#
# This Python script sets the padding of ITILCategories dropdown in all css styles
#
from os import listdir
directory = '/home/marcel/Schreibtisch/Docker/glpi/glpi/css_compiled/'
# Search for this unique CSS selector
word = '.select2-results__option {'
# The string 1 Line below the CSS selector, which shall be replaced
word_find_me = 'padding: 6px;'
# The string that replaces the string above
word_set_me = 'padding: 1px;'
print('Directory:', directory)
for f in listdir(directory):
    print('File:', f)
    lines = []
    posOfWord = -1
    with open(directory + f, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(word) != -1:
                posOfWord = (lines.index(line)+1)
                break
    if posOfWord != -1 and word_find_me in lines[posOfWord]:
        print('\tReplaced ', word_find_me, "with", word_set_me)
        lines[posOfWord] = lines[posOfWord].replace(word_find_me, word_set_me)
        with open(directory + f, 'w') as file:
            for line in lines:
                file.write(line)
