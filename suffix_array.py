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


# recordar cambiarlo
def suffixArray(s):
    '''
    Given a string, the function returns the suffix_array of the string
    '''
    suffixes = [(s[i:], i) for i in range(len(s))] # o(n)
    suffixes.sort(key=lambda x: x[0]) #nlog(n)
    return [s[1] for s in suffixes] #o(n)

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


def search_all(sa, phrase, fulltext):
    '''
    parameters: suffix array, phrase, full text
    Given a suffix array, a phrase and the full text
    The function uses binary search to find all the ocurrencies of the phrase in the text 
    returns an array of indexes of the phrase found in the text
    '''
    l = 0
    r = len(sa)
    while l < r:  #We do a binary search
        mid = (l+r)//2 
        if fulltext[sa[mid]:] < phrase:
            l = mid+1
        else:
            r = mid

    def match_at(i):
        return fulltext[i: i + len(phrase)] == phrase

    first = l
    while first > 0 and match_at(sa[first - 1]):
        first -= 1

    last = r
    while match_at(sa[last]):
        last += 1

    return sa[first:last]


