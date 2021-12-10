import suffix_tree as st
import patricia_tree as pt
import sys
import suffix_array as sa

txt = open(sys.argv[1])
fulltext = txt.read()
array = sa.suffixArray(fulltext)

print(array)
root = pt.Patricia()
for w in array:
    root.insert(fulltext[w:]+'$')
root.insert('$')
root.pre_count_sons()
root.pre_most_popular()
print(root)