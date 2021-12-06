import suffix_array as sa
import sys

txt = open(sys.argv[1])
fulltext = txt.read()
array =  sa.suffixArray(fulltext)
print("------------------------------------------")
while True:
    word = input("What word do you want to search?")
    if word=="":
        break
    coincidences=sa.search_all(array, word, fulltext)
    print("We found "+str(len(coincidences))+ " coincidences","\n")
    for c in coincidences:
        if c>10:
            text=fulltext[c-10:c+10]
        else:
            text=fulltext[c:c+20]
        print("> "+text)
    print("------------------------------------------")


