import suffix_tree as st
import sys
import suffix_array as sa

txt = open(sys.argv[1])
fulltext = txt.read()
array =  sa.suffixArray(fulltext)

print(array)
root = st.Trie()
for w in array:
    root.insert(fulltext[w:])
    root.insert('')
print(root)