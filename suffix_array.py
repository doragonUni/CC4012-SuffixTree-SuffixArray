'''
IDEA OF SUFFIX ARRAY
given a string, let say: 'abracadabra$'

We do the following:

0 abracadabra
1 bracadabra
2 racadabra
3 acadabra
4 cadabra
5 adabra
6 dabra
7 abra
8 bra
9 ra
10 a
11 $

then we sort the elements
and the suffix array is completed as shown:
10-7-0-3-5-8-1-4-6-9-2
'''

#[10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

import sys

#if len(sys.argv) != 2:
  #  print('Use: '+sys.argv[0]+' archivo.txt')
    #sys.exit(1)
s='banana'

#Momentanio, solucion sacada de google

txt = open(sys.argv[1])
fulltext = txt.read()

# recordar cambiarlo
def suffixArray(s):
    suffixes = [(s[i:], i) for i in range(len(s))] # o(n)
    suffixes.sort(key=lambda x: x[0]) #nlog(n)
    return [s[1] for s in suffixes] #o(n)

array =  suffixArray(fulltext)
print(array)

""" def search_in_array(phrase, full_text, suffix_array):
    
    left = 0
    right = len(suffix_array)-1
    while(right>=left):
        mid = (left+right)//2
        if fulltext[suffix_array[mid]:]<phrase:
            left = mid + 1 
        else:
            right = mid
    if not full_text[suffix_array[left]:].startwith(phrase):
        print("Not found")
    return suffix_array[left] """

def search_in_array(sa, phrase, text):
    left = 0
    right = len(sa)
    while right > left:
        mid = (right+left)//2
        if text[sa[mid]:] < phrase:
            left = mid+1
        else: 
            right = mid
    if not text[sa[left]:].startswith(phrase): 
        # i suppose text[a[lo]:a[lo]+len(x)] == x could be a faster check
        raise IndexError('not found')
    return sa[left]


def search_all(array, phrase, seq):
    l = 0
    r = len(array)
    while l < r: 
        mid = (l+r)//2 #set the middle to binary search
        if seq[array[mid]:] < phrase:
            l = mid+1
        else:
            r = mid

    def match_at(i):
        return seq[i: i + len(phrase)] == phrase

    # array[lo] is one match
    # now we walk backwards to find the first match
    first = l
    while first > 0 and match_at(array[first - 1]):
        first -= 1

    # and walk forwards to find the last match
    last = r
    while match_at(array[last]):
        last += 1

    return array[first:last]

print(search_all(array, "platano", fulltext))
