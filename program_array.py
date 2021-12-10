import suffix_array as sa
import sys

if len(sys.argv) != 2:
    print('Use: '+sys.argv[0]+' archivo.txt')
    sys.exit(1)

txt = open(sys.argv[1]) #The text is given when the file is called
fulltext = txt.read()

s_array = sa.suffix_array(fulltext) # we get de suffix array of the given text
print("------------------------------------------")
while True:
    print("Press Enter to exit")
    word = input("What word do you want to search?") # we get de input of the user
    
    if word=="": #to finish the loop
        break
    occurrences=sa.search_all(s_array, word, fulltext) # we found all the ocurrences
    print("We found "+str(len(occurrences))+ " occurrences","\n")
    for c in occurrences: # we show all the occurrences in screen
        suffix = c.get_suffix()
        lentext = len(suffix)
        if lentext > 5:
            text = fulltext[c.get_index()-5:c.get_index()+lentext+5]
        else:
            text =  c.get_suffix()
        print("> "+text)
    print("------------------------------------------")