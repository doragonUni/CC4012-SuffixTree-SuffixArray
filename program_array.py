import suffix_array as sa
import sys

txt = open(sys.argv[1]) #The text is given when the file is called
fulltext = txt.read()
s_array =  sa.suffixArray(fulltext)

print("------------------------------------------")
while True:
    print("Press Enter to exit")
    word = input("What word do you want to search?")
    
    if word=="":
        break
    occurrences=sa.search_all(s_array, word, fulltext)
    print("We found "+str(len(occurrences))+ " occurrences","\n")
    for c in occurrences:
        if c>10:
            text=fulltext[c-10:c+10]
        else:
            text=fulltext[c:c+20]
        print("> "+text)
    print("------------------------------------------")


