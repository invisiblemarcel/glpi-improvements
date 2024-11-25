/*
 * This Python script removes the max height of ITILCategories dropdown in all css styles
*/
from os import listdir
directory = '/glpi/path/go/here/glpi/css_compiled/'
word = '.select2-container--default .select2-results > .select2-results__options {'
word_del_me = 'max-height: 200px;'
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
    if posOfWord != -1 and word_del_me in lines[posOfWord]:
        print('\ŧRemoved:', lines[posOfWord])
        lines.pop(posOfWord)
        with open(directory + f, 'w') as file:
            for line in lines:
                file.write(line)
